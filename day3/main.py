def extract_data() -> list[str]:
    batteries = []
    with open('data/realdata', 'r') as file:
        for line in file:
            batteries.append(line.strip())
    return batteries

def find_largest_number(battery: str) -> int:
    largest_decimal = 0
    decimal_index = 0
    for idx, char in enumerate(battery[:-1]):
        if int(char) > largest_decimal:
            largest_decimal = int(char)
            decimal_index = idx

    largest_singular = 0
    for idx, char in enumerate(battery[decimal_index+1:]):
        if int(char) > largest_singular:
            largest_singular = int(char)
    ldc = str(largest_decimal)
    lsc = str(largest_singular)
    lns = ldc + lsc
    return int(lns)

def find_largest_battery(battery: str) -> int:
    building_str = ""
    cursor = 0
    digits = 12
    n = len(battery)

    for i in range(digits):
        digits_left = digits - i

        max_start = n - digits_left

        biggest_current = -1
        best_pos = cursor

        for pos in range(cursor, max_start + 1):
            d = int(battery[pos])
            if d > biggest_current:
                biggest_current = d
                best_pos = pos
                if biggest_current == 9:
                    break

        building_str += str(biggest_current)
        cursor = best_pos + 1

    return int(building_str)

def main():
    data = extract_data()
    sum = 0
    for battery in data:
        print(find_largest_battery(battery))
        sum += find_largest_battery(battery)
    print(sum)

if __name__ == "__main__":
    main()
