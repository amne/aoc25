def compute_all_areas(red_tiles):
    areas = []
    for i in range(len(red_tiles)):
        for j in range(i + 1, len(red_tiles)):
            x1, y1 = red_tiles[i]
            x2, y2 = red_tiles[j]
            area = (abs(x1 - x2)+1) * (abs(y1 - y2)+1)
            areas.append(area)
    areas.sort(reverse=True)
    # [print(area) for area in areas]
    print(areas[0] if areas else 0)


def compute_largest_area(red_tiles):
    # get left most tile
    left_most = min(red_tiles, key=lambda t: t[0])
    # get top most tile
    top_most = min(red_tiles, key=lambda t: t[1])
    # get right most tile
    right_most = max(red_tiles, key=lambda t: t[0])
    # get bottom most tile
    bottom_most = max(red_tiles, key=lambda t: t[1])
    # 
    # print(left_most, top_most, right_most, bottom_most)
    # print((abs(left_most[0] - right_most[0]) + 1) * (abs(left_most[1] - right_most[1])+1))

    compute_all_areas([left_most, top_most, right_most, bottom_most])


def main():
    red_tiles = []
    with open("biginput.txt") as f:
        for line in f:
            red_tiles.append(list(map(int, line.strip().split(','))))
    # print(red_tiles)
    compute_all_areas(red_tiles)
    # compute_largest_area(red_tiles)


if __name__ == "__main__":
    main()
