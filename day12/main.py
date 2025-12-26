import numpy as np


def extract_data(
    file_path: str,
) -> tuple[dict[int, np.ndarray], list[tuple[int, int, list[int]]]]:

    shapes: dict[int, np.ndarray] = {}
    regions: list[tuple[int, int, list[int]]] = []

    with open(file_path, "r") as f:
        lines = f.read().strip().split("\n")

    i = 0
    while i < len(lines):
        line = lines[i]

        if "x" in line and ":" in line:
            # Parse region
            header = line.split(": ")
            dimensions = header[0].split("x")
            width = int(dimensions[0])
            height = int(dimensions[1])
            grid = [int(x) for x in header[1].split()]
            regions.append((width, height, grid))
            i += 1
        elif line and ":" in line and "x" not in line:
            # Parse shape
            shape_id = int(line.rstrip(":"))
            shape_lines = []
            i += 1
            while (
                i < len(lines)
                and lines[i]
                and "x" not in lines[i]
                and ":" not in lines[i]
            ):
                row = [1 if c == "#" else 0 for c in lines[i]]
                shape_lines.append(row)
                i += 1
            shapes[shape_id] = np.array(shape_lines)
        else:
            i += 1


    return shapes, regions



def main():
    shapes, regions = extract_data('data/testdata')
    for shape in shapes:
        print(shape)
        print(shapes[shape])
    print(regions)
if __name__ == '__main__':
    main()