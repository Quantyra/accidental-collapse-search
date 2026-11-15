"""S261 fixed exact diagnostics. See preregistration; no parameter search."""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
import time
import traceback
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "artifacts/s261-exact-diagnostic-2026-11-14.json"
assert not OUT.exists(), "One preregistered run only"
started = time.monotonic()
counts = {}


def check(ok, category):
    assert time.monotonic() - started < 120, "Aggregate cap reached"
    assert bool(ok), category
    counts[category] = counts.get(category, 0) + 1


def success(p, e, r):
    a = (1-p)*(1-e)
    return p*sum((a**j for j in range(r)), F(0))


receipt = {"story": "S261", "status": "running", "exact": True,
           "scope": "Fixed algebra, recurrence and projector fixtures; not universal proof certification."}
try:
    for p in map(F, [0, F(1,16), F(1,4), F(1,2), 1]):
        for e in map(F, [0, F(1,64), F(1,8), F(1,2), 1]):
            # Probability tree aggregated into alive, failed-collapsed and success states.
            alive, failed, hit = F(1), F(0), F(0)
            for r in range(1, 9):
                hit += alive*p
                failed += alive*(1-p)*e
                alive *= (1-p)*(1-e)
                check(alive+failed+hit == 1, "probability_conservation")
                check(hit == success(p,e,r), "geometric_success")
                if e == 0:
                    check(hit == 1-(1-p)**r, "ideal_endpoint")
                if e == 1:
                    check(hit == p, "collapse_endpoint")

    A,B,r,e = s.symbols("A B r e", real=True)
    k=1/e
    before=1-k+k*r
    after=(1-e)*A*before+e*((1-k)*A+k*B)
    c=-(1-e)*(1-r)/e
    check(s.simplify(after-before-c*(A-1)-(B-r)) == 0, "general_noisy_identity")
    check(s.simplify((1-k)*A+k*B-before-(1-k)*(A-1)-k*(B-r)) == 0,
          "general_ordinary_identity")

    v2=[s.Matrix(x) for x in [(1,0),(0,1),(s.Rational(3,5),s.Rational(4,5)),
                              (s.Rational(3,5),4*s.I/5)]]
    v4=[s.kronecker_product(v2[i],v2[j]) for i,j in [(0,0),(2,0),(2,2),(3,2)]]
    v4 += [s.Matrix([s.Rational(3,5),0,0,s.Rational(4,5)]),
           s.Matrix([s.Rational(3,5),0,0,4*s.I/5])]
    for states,partitions in [(v2, [[[0],[1]],[[0,1]]]),
                              (v4, [[[0,1],[2,3]],[[0,2],[1,3]],[[0],[1],[2],[3]]])]:
        for u in states:
            check((u.conjugate().T*u)[0] == 1, "state_normalization")
        for i,u in enumerate(states):
            # Fixed neighboring and self pairs include phase cancellation and zero branches.
            for j in [i,(i+1)%len(states)]:
                v=states[j]
                ov=s.Abs((u.conjugate().T*v)[0])
                for partition in partitions:
                    affinity=s.Integer(0)
                    block_overlap=s.Integer(0)
                    for block in partition:
                        pu=sum(s.conjugate(u[z])*u[z] for z in block)
                        pv=sum(s.conjugate(v[z])*v[z] for z in block)
                        affinity += s.sqrt(pu*pv)
                        block_overlap += s.Abs(sum(s.conjugate(u[z])*v[z] for z in block))
                    affinity=s.simplify(affinity)
                    block_overlap=s.simplify(block_overlap)
                    check(affinity <= 1, "classical_affinity_bound")
                    check(s.simplify(block_overlap-ov) >= 0, "projector_triangle_bound")
                    for eps in map(s.Rational, [F(1,64),F(1,8),F(1,2),F(1)]):
                        gain=-(1-eps)*(1-ov)/eps*(affinity-1)+(block_overlap-ov)
                        check(s.simplify(gain) >= 0, "noisy_score_monotonicity")
                        gain2=(1-1/eps)*(affinity-1)+(block_overlap-ov)/eps
                        check(s.simplify(gain2) >= 0, "ordinary_score_monotonicity")

    # Data differs, sampled ancilla is |0>: projection does not erase the data.
    proj=s.diag(1,0,1,0)
    for data in v2:
        joint=s.kronecker_product(data,v2[0])
        check(proj*joint == joint, "protected_workspace_counterexample")

    fixtures=[]
    for N in [16,64,256,1024]:
        for eps in [F(0),F(1,64),F(1,8),F(1,2),F(1)]:
            # Exact ceiling of max(cuberoot(N), sqrt(eps*N)).
            m=1
            while m**3 < N or m*m < eps*N:
                m+=1
            t=m//4
            repeats=(N+m*m-1)//(m*m)
            a=b=F(1)
            for _ in range(t):
                a,b=(1-F(2,N))*a+F(2*(N-1),N)*b, -F(2,N)*a+(1-F(2,N))*b
                check(a*a+(N-1)*b*b == N, "grover_normalization")
            p=a*a/N
            prob=success(p,eps,repeats)
            check(F(0) <= prob <= 1, "grover_success_range")
            if N>=256:
                check(p >= F(m*m,40*N), "explicit_marked_weight")
                check(prob >= F(1,3280), "explicit_attempt_success")
            fixtures.append({"N":N,"epsilon":str(eps),"t":t,"r":repeats,
                             "p":str(p),"success":str(prob)})
    check(sum(F(4)**j / s.factorial(j) for j in range(3)) > 12,
          "fixed_repetition_failure_bound")
    receipt.update(status="passed", fixtures=fixtures)
except BaseException as exc:
    receipt.update(status="failed", error=repr(exc), traceback=traceback.format_exc())
finally:
    receipt.update(assertions=sum(counts.values()), categories=counts,
                   elapsed_seconds=round(time.monotonic()-started,6),
                   script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   preregistration_sha256=hashlib.sha256((ROOT / "artifacts/s261-preregistration-2026-11-14.json").read_bytes()).hexdigest())
    OUT.write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8",newline="\n")
    print(json.dumps({k:v for k,v in receipt.items() if k not in {"fixtures","traceback"}}))
if receipt["status"] != "passed":
    raise SystemExit(1)
