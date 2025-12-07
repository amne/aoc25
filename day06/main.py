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
    # padded_numbers = [s.zfill(max_len) for s in str_numbers]
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

def main():
    homework = []
    # with open("biginput.txt") as f:
    with open("input.txt") as f:
        for line in f:
            # check if first char is a number
            if line and not line.strip().split()[0].isdecimal():
                break
            homework.append(list(map(int, line.strip().split())))
        # last line should be the operations
        homework.append(line.strip().split())
    homework = transpose(homework)
    # print(do_operation(homework[0][:-1], homework[0][-1]))
    # for h in homework:
    #     print(do_operation(h[:-1], h[-1]))
    [print(part2_transformation(h[:-1]), h[-1]) for h in homework]
    print(sum(do_operation(part2_transformation(h[:-1]), h[-1]) for h in homework))

if __name__ == "__main__":
    main()
