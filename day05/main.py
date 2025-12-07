def dedup_ranges(ranges):
    if not ranges:
        return []
    # sort ranges
    ranges.sort(key=lambda x: x[0])
    deduped = [ranges[0]]
    for current in ranges[1:]:
        last = deduped[-1]
        if current[0] <= last[1]:  # overlapping so just extend
            deduped[-1] = (last[0], max(last[1], current[1]))
        else:
            deduped.append(current)
    return deduped

def is_valid_ingredient(ingredient, fresh_ranges):
    for low, high in fresh_ranges:
        if low <= ingredient <= high:
            return True
    return False

def main():
    fresh_ranges = []
    ingredients = []
    with open("biginput.txt") as f:
    # with open("input.txt") as f:
        for line in f:
            if line.strip() == "":
                break
            fresh_ranges.append(tuple(map(int, line.strip().split("-"))))
        for line in f:
            ingredients.append(int(line.strip()))
    print(fresh_ranges)
    print(ingredients)
    print(len(list(filter(lambda x: is_valid_ingredient(x, fresh_ranges), ingredients))))
    fresh_ranges = dedup_ranges(fresh_ranges)
    print(sum(map(lambda x: x[1]-x[0]+1, fresh_ranges)))


if __name__ == "__main__":
    main()
