import pprint
from dataclasses import dataclass

with open("test.txt", "r") as f:
    data = f.readlines()

relationships = {}
for row in data:
    n, _, c, v, *o, t = row.split(" ")
    t = t.strip().strip(".")
    if n not in relationships:
        relationships[n] = {}
    if t not in relationships[n]:
        relationships[n][t] = 0
    if c == "gain":
        relationships[n][t] += int(v)
    else:
        relationships[n][t] -= int(v)
    print(n, c, v, t)

for k, v in relationships.items():
    relationships[k] = sorted(v.items(), key=lambda x: x[1], reverse=True)

sorted_relationships = sorted(
    relationships.items(), key=lambda x: sum(y[1] for y in x[1]), reverse=True
)


@dataclass
class Person:
    left: 'Person'  # Use string annotation for forward reference


pprint.pprint(sorted_relationships)
print(len(relationships))
