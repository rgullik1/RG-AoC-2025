def check_repeat(my_str: str) -> bool:
    str_len = len(my_str)
    check_for = my_str[0:int(str_len/2)]
    check_in = my_str[int(str_len/2):str_len]
    return check_for == check_in

def check_repeated_at_least_twice(my_str: str) -> bool:
    str_len = len(my_str)
    for pattern_len in range(1, str_len // 2 + 1):
        if str_len % pattern_len == 0:
            pattern = my_str[:pattern_len]
            repetitions = str_len // pattern_len
            if pattern * repetitions == my_str:
                return True
    return False



def interval_iterator(interval: str) -> list[str]:
    ranges = interval.split("-")
    left = int(ranges[0])
    right = int(ranges[1])
    return [str(n) for n in range(left, right + 1)]

def ranges_to_pnumbs(ranges: list[str]) -> list[str]:
    output = []
    for range_str in ranges:
        output.extend(interval_iterator(range_str))
    return output

def extract_data() -> list[str]:
    ranges = []
    with open('data/realdata', 'r') as file:
        for line in file:
            ranges.append(line.strip().split(","))
    return ranges[0] if ranges else []

def check_repeat_in_range(ranges: list[str]) -> list[str]:
    return [number for number in ranges if check_repeated_at_least_twice(number)]

def main():
    ranges = extract_data()
    pnumbs = ranges_to_pnumbs(ranges)
    invalids = check_repeat_in_range(pnumbs)
    print("invalids")
    print(invalids)
    int_invalids = [int(s) for s in invalids]
    suminvalids = sum(int_invalids)
    print("suminvalids")
    print(suminvalids)

if __name__ == "__main__":
    main()
