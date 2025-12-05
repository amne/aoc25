def part1(rotations):
    start = 50
    hitszero = 0
    for rotation in rotations:
        start = (start + rotation) % 100 
        if start == 0:
            hitszero += 1
    print(start)
    print(hitszero)

def part2(rotations):
    passeszero = 0
    hitszero = 0
    start = 50
    for rotation in rotations:
        before = start
        if rotation < 0:    
            passeszero += abs(rotation) // 100
            rotation += 100 * (abs(rotation) // 100)
        else:
            passeszero += abs(rotation) // 100
            rotation -= 100 * (abs(rotation) // 100)
        # if start + rotation < 0 or start + rotation > 100:
        #     passeszero += 1
        start += rotation
        if start < 0 and before > 0:
            passeszero += 1
        elif start > 100 and before < 100:
            passeszero += 1
        start = start % 100
        if start == 0:
            hitszero += 1
    print(start)
    print(passeszero)
    print(hitszero)
    print(passeszero + hitszero)


def main():
    rotations = []
    with open("biginput.txt") as f:
        for line in f:
            if line[0] == 'R':
                rotations.append(int(line[1:]))
            elif line[0] == 'L':
                rotations.append(-int(line[1:]))
    part1(rotations)
    part2(rotations)


if __name__ == "__main__":
    main()
