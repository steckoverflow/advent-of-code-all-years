def load_data(use_test_data: bool = False) -> tuple[dict[str, int], list[str]]:
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
    data = test if use_test_data else data
    for row in data.split("\n"):
        if not row:
            continue
        wires[row.split(" ")[-1]] = None
        instructions.append(row.strip())
    return wires, instructions


def single_action(task, dest, wires) -> bool:
    if task.isnumeric():
        wires[dest] = int(task)
        return True
    ref = wires.get(task)
    if ref:
        wires[dest] = ref
        return True
    return False


def two_actions(tasks, dest, wires) -> bool:
    if not tasks[0] == "NOT" or wires[tasks[-1]] is None:
        return False
    # NOTE: As integers are variable length I need to somehow force it into a 16bit length
    wires[dest] = (~wires[tasks[-1]]) & 0xFFFF
    return True


def three_actions(tasks, dest, wires) -> bool:
    v1, inst, v2 = tasks
    if inst == "AND":
        if v1.isnumeric():
            if not wires[v2] is None:
                wires[dest] = int(v1) & wires[v2]
                return True
            return False
        elif not wires[v1] is None and not wires[v2] is None:
            wires[dest] = wires[v1] & wires[v2]
            return True
        else:
            return False
    elif inst == "OR":
        if not wires[v1] is None and not wires[v2] is None:
            wires[dest] = wires[v1] | wires[v2]
            return True
        return False
    elif inst == "RSHIFT":
        if not wires[v1] is None:
            wires[dest] = wires[v1] >> int(v2)
            return True
        return False
    elif inst == "LSHIFT":
        if not wires[v1] is None:
            wires[dest] = wires[v1] << int(v2)
            return True
        return False


def process_tasks(dest: str, tasks: list, wires: dict[str, int | None]) -> bool:
    if len(tasks) == 1:
        return single_action(tasks[0], dest, wires)
    elif len(tasks) == 2:
        return two_actions(tasks, dest, wires)
    elif len(tasks) == 3:
        return three_actions(tasks, dest, wires)


def process_instructions(instructions: list[str], wires: dict[str, int | None]):
    # print(f"Number of instructions: {len(instructions)}")
    line = instructions.pop(0)
    if not line:
        return
    inst, dest = line.split(" -> ")
    tasks = inst.split(" ")
    # print(f"Attempting to perform instruction: {inst} on destination: {dest}")
    success = process_tasks(dest, tasks, wires)
    if not success:
        instructions.append(line)
    # print(f"Success: {success}, Wires: {wires}")


if __name__ == "__main__":
    wires, instructions = load_data(use_test_data=False)
    # print("Before processing: ", wires)
    while len(instructions):
        process_instructions(instructions, wires)
    print("Part 1: ", wires["a"])
