def is_valid_id(id_num):
    # make the number a string
    id_str = str(id_num)
    # if length is odd then it's valid
    if len(id_str) % 2 != 0:
        return True
    # if first half == second half then it's invalid
    half_len = len(id_str) // 2
    if id_str[:half_len] == id_str[half_len:]:
        return False
    return True 
    
def is_valid_id_p2(id_num):
    id_str = str(id_num)
    # we can slice a number into equal parts, two, three, more
    for k in range(len(id_str)//2, 0, -1):
        # if we can't slice perfectly, skip the slice length
        if len(id_str) % k != 0:
            continue
        # if we can slice in equal parts and they are all the same, it's invalid
        if len(set([id_str[i:i+k] for i in range(0, len(id_str), k)])) == 1:
            return False
    return True

def extract_invalid_ids_in_range(id_range):
    invalid_ids = []
    for id_num in range(id_range[0], id_range[1] + 1):
        if not is_valid_id_p2(id_num):
            invalid_ids.append(id_num)
    return invalid_ids

def main():
    ranges = []
    with open("biginput.txt") as f:
    # with open("input.txt") as f:
        for line in f:
            ranges = list(map(lambda x: tuple(map(int, x.split("-"))), line.strip().split(",")))
    print(ranges)
    all_invalid_ids = []
    for r in ranges:
        invalid_ids = extract_invalid_ids_in_range(r)
        all_invalid_ids.extend(invalid_ids)
        print(f"Invalid IDs in range {r}: {invalid_ids}")
    print(sum(all_invalid_ids))


if __name__ == "__main__":
    main()
