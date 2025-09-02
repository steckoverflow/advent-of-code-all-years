import random

with open("9.txt", "r") as f:
    data = f.readlines()

nodes = {}

for row in data:
    fr = row.split(" to ")[0]
    to = row.split(" to ")[1].split(" = ")[0]
    dist = int(row.split(" to ")[1].split(" = ")[1].strip())
    if nodes.get(fr):
        nodes[fr][to] = dist
    else:
        nodes[fr] = {to: dist}
    if nodes.get(to):
        nodes[to][fr] = dist
    else:
        nodes[to] = {fr: dist}

answer = None
i = 0

# Using heuristics search, picking random starting point i times
while i < 10_000:
    current = random.choice(list(nodes.keys()))
    visited = [current]
    total_dist = 0

    while len(visited) != len(nodes):
        paths = nodes[current]
        min_path = None
        min_dist = None

        for path in paths:
            if path in visited:
                continue

            dist = nodes[current][path]
            if min_dist is None or dist > min_dist:
                min_dist = dist
                min_path = path

        if min_dist is not None and min_path not in visited:
            visited.append(min_path)
            total_dist += min_dist
            current = min_path

    if answer is None or total_dist > answer:
        answer = total_dist

    i += 1

print("Part 2: ", answer)
