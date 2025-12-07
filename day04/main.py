def count_neighbours(grid, x, y):
    # count all "@" chars in all 8 directions
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] == "@":
                    count += 1
    return count

def main():
    papergrid = []
    with open("biginput.txt") as f:
    # with open("input.txt") as f:
        for line in f:
            papergrid.append([c for c in line.strip()])
    [print("".join(row)) for row in papergrid]
    total_breakable = 0
    breakable = 1
    while breakable:
        breakable = 0
        to_break = []
        for i in range(len(papergrid)):
            for j in range(len(papergrid[0])):
                if papergrid[i][j] == "@":
                    neighbours = count_neighbours(papergrid, i, j)
                    if neighbours < 4:
                        breakable += 1
                        to_break.append((i, j))
        for (i, j) in to_break:
            papergrid[i][j] = "."
        total_breakable += breakable
    print(total_breakable)


if __name__ == "__main__":
    main()
