import portion as p
import portion
def extract_fresh_only(file_path: str) -> list[p.Interval]:
    with open(file_path, "r") as f:
        content = f.read().strip().split("\n\n")
    fresh_ranges = content[0].split("\n")
    fresh_ranges_list_portions = []
    for range in fresh_ranges:
        first, second = range.split("-")
        fresh_ranges_list_portions.append(p.closed(int(first), int(second)))
    return fresh_ranges_list_portions

def extract_data(file_path: str) -> tuple[list[tuple[int, int]], list[int]]:
    with open(file_path, "r") as f:
        content = f.read().strip().split("\n\n")
    fresh_ranges = content[0].split("\n")
    ingredients = content[1].split("\n")
    fresh_ranges_list_tuple = []
    ingredients_list_tuple = []
    for range in fresh_ranges:
        fresh_ranges_list_tuple.append(tuple(map(int, range.split("-"))))
    for ingredient in ingredients:
        ingredients_list_tuple.append(int(ingredient))
    print(fresh_ranges_list_tuple)
    print(ingredients_list_tuple)
    return fresh_ranges_list_tuple, ingredients_list_tuple

def is_in_range(ingredient: int, range: tuple[int, int]) -> bool:
    if range[0] <= ingredient <= range[1]:
        return True
    return False

def is_in_any_range(ingredient: int, ranges: list[tuple[int, int]]) -> bool:
    for range in ranges:
        if is_in_range(ingredient, range):
            return True
    return False

def expand_range(r: tuple[int, int]) -> set[int]:
    start, end = r
    return set(range(start, end + 1))

def main():
    # Day 1
    fresh, availables = extract_data("data/realdata")
    fresh_count = 0
    for available in availables:
        if is_in_any_range(available, fresh):
            fresh_count += 1
    print(fresh_count)

    # Day 2
    fresh_set_list: list[p.Interval] = extract_fresh_only("data/realdata")
    print(f"fresh_set_list: {fresh_set_list}")
    fresh_set: p.Interval = p.empty()
    for fresh_item in fresh_set_list:
        fresh_set = fresh_set | fresh_item

    fresh_count = 0
    for interval in fresh_set:
        fresh_count += interval.upper - interval.lower + 1

    print(f"fresh_count: {fresh_count}")
if __name__ == "__main__":
    main()
