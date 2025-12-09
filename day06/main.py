def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def part2_transformation(numbers):
    # split each number by digits
    # right justify
    # build new numbers by reading columns
    str_numbers = [str(n) for n in numbers]
    max_len = max(len(s) for s in str_numbers)
    # pad with spaces

    padded_numbers = [s.ljust(max_len) for s in str_numbers]
    transposed = transpose([list(s) for s in padded_numbers])
    new_numbers = [int("".join(col)) for col in transposed]
    return new_numbers


def do_operation(numbers, op):
    if op == "+":
        return sum(numbers)
    elif op == "*":
        prod = 1
        for n in numbers:
            prod *= n
        return prod
    else:
        raise ValueError(f"Unsupported operation: {op}")

def readfile(filename):
    homework = []
    with open(filename) as f:
        for line in f:
            # check if first char is a number
            if line and not line.strip().split()[0].isdecimal():
                break
            homework.append(list(map(int, line.strip().split())))
        # last line should be the operations
        homework.append(line.strip().split())
    homework = transpose(homework)
    return homework

def process_homework_part2(homework):
    processed = []
    ops = homework[-1]
    # ops is now a string like "+    *    +         *"
    # with a specific number of spaces between each operator
    # find the number of spaces for each operator
    # also pad ops to the right to match the length of the longest numbers line
    padright = max(len(str(n)) for n in homework)
    ops = ops.ljust(padright)

    op_positions = []
    index = 0
    for index in range(len(ops)):
        op = ops[index]
        if op != " ":
            if len(op_positions) > 0:
                op_positions[-1] = (op_positions[-1][0], op_positions[-1][1], index - op_positions[-1][1] - 1)
            op_positions.append((op, index, 0))
    op_positions[-1] = (op_positions[-1][0], op_positions[-1][1], index + 1 - op_positions[-1][1])
    print(op_positions)
    [print(f"Operation: {op}, Start: {start}, Length: {length}") for op, start, length in op_positions]

    results = []
    for op, start, length in op_positions:
        numbers = [h[start:start + length] for h in homework[:-1]]
        numbers = transpose(numbers)
        print(op)
        numbers = [int("".join(n)) for n in numbers]
        result = do_operation(numbers, op)
        print(f"Numbers: {numbers} => Result: {result}")
        results.append(result)
    print(sum(results))


def readfile2(filename):
    homework = []
    with open(filename) as f:
        for line in f:
            homework.append(line.strip("\n"))
    [print(h) for h in homework]

    process_homework_part2(homework)
    return homework




def main():
    homework = readfile2("biginput.txt")

if __name__ == "__main__":
    main()
