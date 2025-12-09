def extract_data(file_path: str) -> tuple[str, ...]:
    rows: list[str] = []
    with open(file_path, "r") as f:
        for line in f:
            rows.append(line.strip())
    return tuple(rows)


def count_timelines(grid: tuple[str, ...]) -> int:
    height = len(grid)
    width = len(grid[0])

    start_row = start_col = None
    for r, row in enumerate(grid):
        c = row.find("S")
        if c != -1:
            start_row, start_col = r, c
            break

    initial_counts = [0] * width

    initial_counts[start_col] = 1


    def quantum_propagator(row_idx: int, counts_tuple: tuple[int, ...]) -> int:
        if row_idx == height:
            return sum(counts_tuple)

        row = grid[row_idx]
        counts = counts_tuple

        next_counts = [0] * width
        for c, count in enumerate(counts):
            if count == 0:
                continue

            cell = row[c]

            if cell == ".":  # straight down
                next_counts[c] += count
            elif cell == "^":  # splits left/right
                if c - 1 >= 0:
                    next_counts[c - 1] += count
                if c + 1 < width:
                    next_counts[c + 1] += count

        return quantum_propagator(row_idx + 1, tuple(next_counts))

    return quantum_propagator(start_row + 1, tuple(initial_counts))


def main():
    grid = extract_data("data/realdata")
    timelines = count_timelines(grid)
    print(timelines)


if __name__ == "__main__":
    main()
