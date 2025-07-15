import json
from core import add_tool
from features import evaluate
with open('examples/input.json') as stream: cases=json.load(stream)
print(json.dumps(evaluate(cases,{'add':add_tool}),sort_keys=True))
