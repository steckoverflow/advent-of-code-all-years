import pprint

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

for k, v in relationships.items():
    relationships[k] = sorted(v.items(), key=lambda x: x[1], reverse=True)

sorted_relationships = sorted(
    relationships.items(), key=lambda x: sum(y[1] for y in x[1]), reverse=True
)


class Node:
    nodes = []

    def __init__(self, name):
        self.name = name
        self.left: "Node" = None
        self.right: "Node" = None
        self.happiness = 0
        self.add_node()

    def set_neighbour(self, n, dir, h):
        if dir == "l":
            self.left = n
            self.happiness += h
        elif dir == "r":
            self.right = n
            self.happiness += h

    def add_node(self):
        Node.nodes.append(self)


for v in enumerate(sorted_relationships):
    rn, rl = v
    n = Node(rn)
    if not n.left:
        print(rl)
        l, lh = rl[1][0]
        ln = Node(l)
        n.set_neighbour(ln, "l", lh)


print(Node.nodes)
pprint.pprint(sorted_relationships)
