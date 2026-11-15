"""Check draft artifact identities and metadata; does not execute research tests."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import unicodedata
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
local_deps = ROOT / '.build/check-deps'
if local_deps.is_dir():
    sys.path.insert(0, str(local_deps))
import pymupdf
import yaml
from jsonschema import Draft7Validator


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(ok, message):
    if not ok:
        raise SystemExit(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    receipt_path = ROOT / 'verification/package.json'
    files = sorted(p for p in ROOT.rglob('*') if p.is_file() and not any(
        part in {'.git', '.build', '.venv', '__pycache__'}
        for part in p.relative_to(ROOT).parts) and p != receipt_path)
    cff = yaml.safe_load((ROOT / 'CITATION.cff').read_text(encoding='utf-8'))
    schema_path = ROOT / '.build/cff-1.2.0-schema.json'
    schema_path.parent.mkdir(exist_ok=True)
    if not schema_path.exists():
        url = 'https://raw.githubusercontent.com/citation-file-format/citation-file-format/1.2.0/schema.json'
        with urllib.request.urlopen(url, timeout=30) as response:
            schema_path.write_bytes(response.read())
    require(sha(schema_path) == '0b8d22140da702d766df318dcff3a91af2f39521298dcf36d76315fd99cc169b',
            'CFF schema identity mismatch')
    schema = json.loads(schema_path.read_text(encoding='utf-8'))
    Draft7Validator.check_schema(schema)
    Draft7Validator(schema).validate(cff)
    zenodo = json.loads((ROOT / '.zenodo.json').read_text(encoding='utf-8'))
    require(cff['version'] == zenodo['version'] == '0.2.0', 'Release version mismatch')
    require(cff['preferred-citation']['title'] == zenodo['title'], 'Title mismatch')
    require(cff['license'] == zenodo['license'] == 'CC-BY-4.0', 'License mismatch')
    require(zenodo['upload_type'] == 'publication' and zenodo['publication_type'] == 'preprint',
            'Archive type mismatch')
    require(zenodo['creators'] == [{'name': 'Fredriksen, Daniel', 'affiliation': 'Quantyra Inc.',
                                  'orcid': '0009-0002-9123-7435'}], 'Author mismatch')
    require(cff['authors'][0]['orcid'] == 'https://orcid.org/0009-0002-9123-7435', 'ORCID mismatch')
    public_receipt = ROOT / ('publication/zenodo-v'+zenodo['version']+'-verification.json')
    if public_receipt.exists():
        published = json.loads(public_receipt.read_text(encoding='utf-8'))
        require(published['result'] == 'PASS' and published['all_files_match_tag'], 'Unverified DOI')
        require(cff.get('doi') == cff['preferred-citation'].get('doi') == published['version_doi'], 'DOI mismatch')
    else:
        require('doi' not in cff and 'doi' not in cff['preferred-citation'], 'Unissued manuscript DOI')
    require('doi' not in zenodo, 'Do not override the GitHub integration DOI')

    source_hash, pdf_hash = sha(ROOT / 'manuscript/main.tex'), sha(ROOT / 'manuscript/main.pdf')
    build = json.loads((ROOT / 'verification/build.json').read_text())
    visual = json.loads((ROOT / 'verification/visual.json').read_text())
    review = json.loads((ROOT / 'verification/internal-review.json').read_text())
    require(build['source_sha256'] == review['source_sha256'] == source_hash, 'Stale source record')
    require(build['pdf_sha256'] == visual['pdf_sha256'] == pdf_hash, 'Stale PDF record')
    require(review['record_sha256'] == sha(ROOT / review['record']), 'Changed internal review record')
    require(not any(review[k] for k in ['independent_human_review',
                                        'formal_certification', 'new_diagnostic_execution']),
            'Unsupported human/formal certification or new diagnostic claim')
    manifest_path = ROOT / 'reviews/feedback-v0.2.0/manifest.json'
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        require(manifest['status'] == 'COMPLETE' and not manifest['unresolved_blocking_findings'],
                'Three-lens review is incomplete or has unresolved blockers')
        bridge = json.loads((ROOT / 'verification/release-source-bridge.json').read_text(encoding='utf-8'))
        reviewed_hash = bridge['reviewed_source_sha256']
        require(bridge['release_source_sha256'] == source_hash, 'Stale release bridge')
        restored = (ROOT / 'manuscript/main.tex').read_text(encoding='utf-8')
        for item in reversed(bridge['replacements']):
            require(restored.count(item['after']) == 1, 'Non-unique release substitution')
            restored = restored.replace(item['after'], item['before'])
        require(hashlib.sha256(restored.encode('utf-8')).hexdigest() == reviewed_hash,
                'Scientific source changed after review')
        require(manifest['final_source_sha256'] == reviewed_hash, 'Review source mismatch')
        require(sha(ROOT / manifest['disposition']) == manifest['disposition_sha256'],
                'Changed review disposition')
        require({x['lens'] for x in manifest['reviews']} == {
            'proof-adversarial', 'complexity/resource', 'non-claims/attribution'}, 'Missing lens')
        require(len(manifest['reviews']) == 3 and len({
            x['phases'][-1]['report'] for x in manifest['reviews']}) == 3,
            'The three lenses require three separate final reports')
        require(all(x['provider'] in {'claude', 'grok', 'agy'} for x in manifest['reviews']),
                'Unrecorded provider type')
        for item in manifest['reviews']:
            require(item['last_source_sha256'] == reviewed_hash, 'Reviewer has not covered final source')
            require(item['phases'][-1]['verdict'] in {'GO', 'GO-WITH-NOTES'},
                    'Final reviewer verdict does not clear this draft')
            for phase in item['phases']:
                require(phase['completion_verified'], 'Unverified review completion')
                require(sha(ROOT / phase['input_packet']) == phase['input_packet_sha256'],
                        'Changed immutable review input')
                require('Source SHA-256: '+phase['source_sha256'] in (
                    ROOT / phase['input_packet']).read_text(encoding='utf-8'),
                    'Review packet source identity mismatch')
                report = ROOT / phase['report']
                require(report.stat().st_size > 200 and sha(report) == phase['report_sha256'],
                        'Missing or changed review report')
                require(phase['source_sha256'] in report.read_text(encoding='utf-8'),
                        'Reviewer did not identify the reviewed source')
        require(review['external_model_review'], 'Review status has not been updated')
    else:
        require(not review['external_model_review'], 'External review has no manifest')
    require(build['final_log_diagnostics'] == [], 'TeX diagnostics remain')
    document = pymupdf.open(ROOT / 'manuscript/main.pdf')
    require(document.metadata['title'] == zenodo['title'], 'PDF title mismatch')
    require(len(document) == build['pages'], 'Page count mismatch')
    require(visual['result'] == 'PASS' and visual['pages_inspected'] == list(range(1, len(document)+1)),
            'Incomplete visual inspection')
    font_ids = {font[0] for page in document for font in page.get_fonts(full=True)}
    require(font_ids and all(document.extract_font(x)[3] for x in font_ids), 'Unembedded font')
    pdf_text = unicodedata.normalize('NFKC', ' '.join(p.get_text() for p in document))
    pdf_text = re.sub(r'(?<=\w)-\n(?=\w)', '', pdf_text)
    pdf_text = re.sub(r'\s+', ' ', pdf_text)
    for phrase in ['0.2.0', 'OpenAI Codex', 'Amira Abbas', 'Release and DOI details']:
        require(phrase in pdf_text, 'Missing PDF text: '+phrase)
    provenance = json.loads((ROOT / 'evidence/provenance.json').read_text())
    for name, expected in provenance['files'].items():
        require(sha(ROOT / name) == expected, 'Changed preserved evidence: '+name)
    for stem, script in [('s261-exact', 's261_exact'), ('s261-power-potential', 's261_power_potential')]:
        result = json.loads((ROOT / f'evidence/artifacts/{stem}-diagnostic-2026-11-14.json').read_text())
        require(result['status'] == 'passed', 'Historical diagnostic not passed')
        require(result['script_sha256'] == sha(ROOT / f'evidence/scripts/{script}_diagnostic.py'),
                'Diagnostic source mismatch')
        prereg = 's261' if stem == 's261-exact' else stem
        require(result['preregistration_sha256'] == sha(
            ROOT / f'evidence/artifacts/{prereg}-preregistration-2026-11-14.json'),
            'Diagnostic preregistration mismatch')
    for p in files:
        if p.suffix.lower() in {'.pdf', '.png'}:
            continue
        content = p.read_text(encoding='utf-8')
        require(not re.search(r'[A-Za-z]:[\\/](?:Users|Windows)[\\/]', content),
                'Machine path in '+p.name)
        require(not re.search(r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,}', content),
                'Possible credential in '+p.name)
        require(not re.search(r'Quantyra-(?:Quantum-)?Planning[/\\]', content),
                'Private planning reference in '+p.name)
        if p.suffix == '.md':
            for target in re.findall(r'\]\(([^)]+)\)', content):
                if target.startswith(('http:', 'https:', '#', 'mailto:')):
                    continue
                require((p.parent / target.split('#', 1)[0]).exists(),
                        'Broken local link: '+p.name+' -> '+target)
    result = {'result': 'PASS', 'scope': 'Preprint package identities, metadata and recorded checks only; not mathematical certification',
              'source_sha256': source_hash, 'pdf_sha256': pdf_hash, 'pages': len(document),
              'embedded_fonts': len(font_ids), 'citation_schema_sha256': sha(schema_path),
              'historical_diagnostics_rerun': False,
              'files': {p.relative_to(ROOT).as_posix(): sha(p) for p in files}}
    if args.write:
        receipt_path.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8', newline='\n')
    else:
        require(json.loads(receipt_path.read_text()) == result, 'Package changed: inspect before --write')
    print(json.dumps({'package': 'PASS', 'files': len(files), 'pages': len(document),
                      'embedded_fonts': len(font_ids)}))


if __name__ == '__main__':
    main()
