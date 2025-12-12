def read_splitters(filename):
    with open(filename) as f:
        splitters = [line.strip() for line in f]
    splitters = [list(s) for s in splitters]
    return splitters


def split_beam(splitters):
    # beam starts from char "S"
    beam_pos = splitters[0].index("S")
    [print("".join(s)) for s in splitters]
    splitters[0][beam_pos] = "|"
    split_count = 0
    for l in range(1, len(splitters)):
        for c in range(len(splitters[l])):
            if splitters[l-1][c] == "|":
                if splitters[l][c] == "^":
                    split_count += 1
                    if c > 0:
                        splitters[l][c-1] = "|"
                    splitters[l][c] = " "
                    if c < len(splitters[l]) - 1:
                        splitters[l][c+1] = "|"
                else:
                    splitters[l][c] = "|"
    print("======")
    [print("".join(s)) for s in splitters]
    print(f"Total splits: {split_count}")

def split_beam2(splitters):
    # beam starts from char "S"
    beam_pos = splitters[0].index("S")
    [print("".join(s)) for s in splitters]
    splitters[0][beam_pos] = "1"
    split_count = 0
    timelines = 0
    max_splitter_number = "1"
    for l in range(1, len(splitters)):
        for c in range(len(splitters[l])):
            if splitters[l-1][c].isnumeric():
                if splitters[l][c] == "^":
                    split_count += 1
                    if c > 0:
                        if splitters[l][c-1].isnumeric():
                            splitters[l][c-1] = str(int(splitters[l-1][c]) + int(splitters[l][c-1]))
                        else:
                            splitters[l][c-1] = str(int(splitters[l-1][c]) + 0)
                    if c < len(splitters[l]) - 1:
                        if splitters[l][c+1].isnumeric():
                            splitters[l][c+1] = str(int(splitters[l-1][c]) + int(splitters[l][c+1]))
                        else:
                            splitters[l][c+1] = str(int(splitters[l-1][c]) + 0)
                else:
                    if splitters[l][c].isnumeric():
                        splitters[l][c] = str(int(splitters[l-1][c]) + int(splitters[l][c]))
                    else:
                        splitters[l][c] = splitters[l-1][c]
            if splitters[l][c].isnumeric():
                if int(splitters[l][c]) > int(max_splitter_number):
                    max_splitter_number = splitters[l][c]
        # if l % 2 == 0:
        #     timelines += len([s for s in splitters[l] if s == "|"])
    print("======")
    # print the grid with right aligned numbers
    [print("".join(s.rjust(len(max_splitter_number) + 2) for s in line)) for line in splitters]

    #[print("".join(list(s.map(lambda c: c.rjust(len(max_splitter_number))))) for s in splitters]
    print(f"Total splits: {split_count}")
    print(f"Total timelines: {timelines}")
    print(f"f:", sum([int(s) for s in splitters[-1] if s.isnumeric()]))




def main():
    filename = "biginput.txt"
    # filename = "input.txt"
    splitters = read_splitters(filename)
    split_beam2(splitters)


if __name__ == "__main__":
    main()
