from core import run
def evaluate(cases,tools):
    ids=[case['id'] for case in cases]
    if len(set(ids))!=len(ids): raise ValueError('Unique case ids required')
    results=[]
    for case in cases:
        actual=run(case['script'],tools,case.get('max_calls',4),case.get('max_steps',8))
        expected=case['expected']
        passed=all(actual.get(key)==value for key,value in expected.items())
        results.append({'id':case['id'],'passed':passed,'actual':actual})
    count=sum(r['passed'] for r in results)
    return {'passed':count,'total':len(results),'pass_rate':count/len(results) if results else None,'results':results}
