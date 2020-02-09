import json
from sys import stdin

with open("scoring.json", "r", encoding="utf-8") as fh:
    scoring = json.loads(fh.read())
results = {}
for i, row in enumerate(stdin):
    if row.replace('\n', '') == 'ok':
        results[i + 1] = row.replace('\n', '')

c = 0
for el in results.keys():
    for res in scoring["scoring"]:
        if el in res['required_tests']:
            c += res["points"] / len(res['required_tests'])

print(int(c))
