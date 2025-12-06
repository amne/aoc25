def find_max_jolts_r(battery_bank, num_batteries = 0):
    if num_batteries == 11:
        return str(max(battery_bank))
    if len(battery_bank) == 1:
        return str(battery_bank[0])
    max_jolts = max(battery_bank[:-11+num_batteries])
    max_index = battery_bank.index(max_jolts)
    return str(max_jolts) + find_max_jolts_r(battery_bank[max_index+1:], num_batteries + 1)

def naive_find_max_jolts(battery_bank):
    max1 = 0
    max1_index = -1
    max2 = 0
    max1 = max(battery_bank)
    max1_index = battery_bank.index(max1)
    if max1_index == len(battery_bank) - 1:
        max2 = max(battery_bank[:max1_index])
        return int(str(max2) + str(max1))
    else:
        max2 = max(battery_bank[max1_index+1:])
        return int(str(max1) + str(max2))

def main():
    battery_banks = []
    with open("biginput.txt") as f:
        for line in f:
            battery_banks.append(list(map(int,list(line.strip()))))
    jolts = []
    for bank in battery_banks:
        jolts.append(find_max_jolts_r(bank, 0))

    print(sum(map(int, jolts)))

if __name__ == "__main__":
    main()
