"""One preregistered supplemental exact check of the new power potential."""
from pathlib import Path
import hashlib, json, time, traceback
import sympy as s

root=Path(__file__).resolve().parents[1]
out=root/'artifacts/s261-power-potential-diagnostic-2026-11-14.json'
assert not out.exists()
prior=json.loads((root/'artifacts/s261-exact-diagnostic-2026-11-14.json').read_text())
started=time.monotonic()
counts={}
def check(ok,category):
    assert time.monotonic()-started+prior['elapsed_seconds']<120, 'aggregate cap'
    assert bool(ok), category
    counts[category]=counts.get(category,0)+1

receipt={'story':'S261','status':'running','exact':True,'scope':'New power potential; not independent or formal proof certification.'}
try:
    a=s.symbols('a')
    for k in [2,3,4,8,64]:
        lhs=(k-1)*a**k-k*a**(k-1)+1
        rhs=(1-a)**2*sum((j+1)*a**j for j in range(k-1))
        check(s.expand(lhs-rhs)==0,'general_scalar_polynomial')
    states=[s.Matrix(x) for x in [(1,0,0,0),
            (s.Rational(3,5),0,0,s.Rational(4,5)),
            (s.Rational(3,5),0,0,4*s.I/5),
            (s.Rational(9,25),s.Rational(12,25),12*s.I/25,16*s.I/25)]]
    for i,u in enumerate(states):
        check((u.conjugate().T*u)[0]==1,'normalization')
        v=states[(i+1)%len(states)]
        r=s.Abs((u.conjugate().T*v)[0])
        for partition in [[[0,1],[2,3]],[[0,2],[1,3]],[[0],[1],[2],[3]],[[0,1,2,3]]]:
            weights=[]
            for block in partition:
                p=sum(s.conjugate(u[j])*u[j] for j in block)
                q=sum(s.conjugate(v[j])*v[j] for j in block)
                weight=s.sqrt(p*q)
                z=s.Abs(sum(s.conjugate(u[j])*v[j] for j in block))
                if weight!=0:
                    weights.append((weight,s.simplify(z/weight)))
                else:
                    check(z==0,'zero_branch')
            A=sum((w for w,_ in weights),s.Integer(0))
            for k,eps in [(1,s.Integer(1)),(2,s.Rational(1,2)),(8,s.Rational(1,8)),(64,s.Rational(1,64))]:
                C=sum((w*ry**k for w,ry in weights),s.Integer(0))
                check(s.simplify(C-r**k)>=0,'ordinary_power_monotonicity')
                check(s.simplify((1-eps)*A*r**k+eps*C-r**k)>=0,'noisy_power_monotonicity')
            for k in [2,3,4]:
                C=sum((w*ry**(k-1) for w,ry in weights),s.Integer(0))
                check(s.simplify(A*r**(k-1)-r**k)>=0,'ideal_power_decrement')
                for eps in [s.Integer(0),s.Rational(1,8),s.Integer(1)]:
                    check(s.simplify((1-eps)*A*r**(k-1)+eps*C-r**k)>=0,'noisy_power_decrement')
    for prob in [s.Integer(0),s.Rational(1,64),s.Rational(1,8),s.Rational(1,2),s.Rational(3,4),s.Integer(1)]:
        for k in [1,2,3,8,64]:
            check(1-abs(1-2*prob)**k<=2*k*prob,'query_self_distance')
    check(2-s.sqrt(3)>s.Rational(1,4),'final_distance_constant')
    receipt['status']='passed'
except BaseException as exc:
    receipt.update(status='failed',error=repr(exc),traceback=traceback.format_exc())
finally:
    elapsed=time.monotonic()-started
    receipt.update(assertions=sum(counts.values()),categories=counts,elapsed_seconds=round(elapsed,6),
                   aggregate_seconds=round(elapsed+prior['elapsed_seconds'],6),
                   script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   preregistration_sha256=hashlib.sha256((root/'artifacts/s261-power-potential-preregistration-2026-11-14.json').read_bytes()).hexdigest())
    out.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:v for k,v in receipt.items() if k!='traceback'}))
if receipt['status']!='passed': raise SystemExit(1)
