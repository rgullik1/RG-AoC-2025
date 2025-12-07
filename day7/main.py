def extract_data(file_path) -> list[list[int]]:
    rows: list[list[str]] = []
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            line = line.replace(".", "0")
            line = line.replace("^", "1")
            line = line.replace("S", "1")
            row = list(line)
            print(row)
            rows.append(row)

    return [[int(x) for x in row] for row in rows]

def main():
    tot_collisions = 0
    rows = extract_data("data/testdata")
    print(rows)
    for i, row in enumerate(rows):

        rows[i] = [a + b for a, b in zip(rows[i], rows[i+1])]
        for i in range(1, len(rows)):
            if
        tot_collisions += 1
        print(top_row)
    print(rows)

    print(tot_collisions)
if __name__ == "__main__":
    main()
