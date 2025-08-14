test = """
123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
"""

with open("7.txt", "r") as f:
    data = f.read()


wires = {}
instructions = []

for row in test.split("\n"):
    if not row:
        continue
    wires[row.split(" ")[-1]] = None
    instructions.append(row)


# NOTE: yikes. quick and dirty turned into this mess.
# Okay... slightly more clean?
# Basically, since switches don't power on until their input is ready we keep parsing the inputs until this is the case
# and only remove one instruction after it actually executed.

while len(instructions):
    print(f"Number of instructions: {len(instructions)}")
    line = instructions.pop(0)
    inst, dest = line.split(" -> ")
    tasks = inst.split(" ")

    # Direct assignment
    if len(tasks) == 1:
        if tasks[0].isnumeric():  # direct
            wires[dest] = int(tasks[0])
            print(f"-> {dest} set value {tasks[0]}")
            continue

        lkp = wires.get(tasks[0])
        if lkp:  # lookup
            wires[dest] = lkp
            print(f"-> {dest} set value {lkp}")
            continue

        instructions.append(line)

    # Inverse
    elif len(tasks) == 2:
        if tasks[0] == "NOT":
            if wires[tasks[-1]]:
                wires[dest] = ~wires[tasks[-1]]
                print(f"{dest} inverted value {~wires[tasks[-1]]}")
                continue

        # TODO: Add info about else clauses

        instructions.append(line)

    # Binary ops
    elif len(tasks) == 3:
        v1, inst, v2 = tasks
        if inst == "AND":
            if (
                not v1.isnumeric()
                and wires[v1] is None
                or not v2.isnumeric()
                and wires[v2] is None
            ):
                instructions.append(line)
                continue
            if not v1.isnumeric() and not v2.isnumeric():
                print(f"{dest} binary and {wires[v1] & wires[v2]}")
                wires[dest] = wires[v1] & wires[v2]
            elif v1.isnumeric():
                print(f"{dest} binary and {int(v1) & wires[v2]}")
                wires[dest] = int(v1) & wires[v2]
            elif v2.isnumeric():
                print(f"{dest} binary and {int(v2) & wires[v1]}")
                wires[dest] = int(v2) & wires[v1]

        elif inst == "OR":
            if (
                not v1.isnumeric()
                and wires[v1] is None
                or not v2.isnumeric()
                and wires[v2] is None
            ):
                instructions.append(line)
                continue
            if not v1.isnumeric() and not v2.isnumeric():
                print(f"{dest} binary or {wires[v1] | wires[v2]}")
                wires[dest] = wires[v1] | wires[v2]
            elif v1.isnumeric():
                print(f"{dest} binary or {int(v1) | wires[v2]}")
                wires[dest] = int(v1) | wires[v2]
            elif v2.isnumeric():
                print(f"{dest} binary or {int(v2) | wires[v1]}")
                wires[dest] = int(v2) | wires[v1]
        elif inst == "RSHIFT":
            if not v2.isnumeric() and wires[v1] is None:
                instructions.append(line)
                continue
            print(f"{dest} rightshift {wires[v1] >> int(v2)}")
            wires[dest] = wires[v1] >> int(v2)
        elif inst == "LSHIFT":
            if not v2.isnumeric() and wires[v1] is None:
                instructions.append(line)
                continue
            print(f"{dest} leftshit {wires[v1] << int(v2)}")
            wires[dest] = wires[v1] << int(v2)

print("Part 1: ", wires)
