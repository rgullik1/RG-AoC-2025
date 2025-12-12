from itertools import combinations
from typing import List, Tuple

def extract_data(file_path: str) -> List[Tuple[int, int]]:
    points: List[Tuple[int, int]] = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = [p.strip() for p in line.split(",")]
            if len(parts) != 2:
                continue
            x, y = map(int, parts)
            points.append((x, y))
    return points

def calc_area(corner1: Tuple[int, int], corner2: Tuple[int, int]) -> int:
    corner1x, corner1y = corner1
    corner2x, corner2y = corner2
    return (abs(corner1x - corner2x) + 1) * (abs(corner1y - corner2y) + 1)




def fill_green(reds: List[Tuple[int, int]]) -> list[Tuple[int, int]]:
    greens: list[Tuple[int, int]] = []

    def add_segment(a: Tuple[int, int], b: Tuple[int, int]):
        ax, ay = a
        bx, by = b

        if ax == bx:
            step = 1 if by > ay else -1
            for y in range(ay + step, by, step):
                greens.append((ax, y))
        elif ay == by:
            step = 1 if bx > ax else -1
            for x in range(ax + step, bx, step):
                greens.append((x, ay))


    for i in range(len(reds) - 1):
        add_segment(reds[i], reds[i + 1])


    add_segment(reds[-1], reds[0])

    return greens

from typing import List, Tuple, Set

Point = Tuple[int, int]


def fill_interior(reds: List[Point], greens: List[Point]) -> List[Point]:
    boundary = set(reds) | set(greens)

    xs = [x for x, _ in boundary]
    ys = [y for _, y in boundary]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)


    min_x -= 1
    max_x += 1
    min_y -= 1
    max_y += 1

    outside: Set[Point] = set()
    q = deque()

    start = (min_x, min_y)
    outside.add(start)
    q.append(start)


    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx < min_x or nx > max_x or ny < min_y or ny > max_y:
                continue
            if (nx, ny) in boundary or (nx, ny) in outside:
                continue
            outside.add((nx, ny))
            q.append((nx, ny))


    interior: List[Point] = []
    for x in range(min_x + 1, max_x):
        for y in range(min_y + 1, max_y):
            p = (x, y)
            if p not in boundary and p not in outside:
                interior.append(p)

    return interior
from collections import deque
from typing import List, Tuple

Point = Tuple[int, int]

def fill_interior_fast(reds: List[Point], greens: List[Point]) -> List[Point]:

    boundary_points = set(reds) | set(greens)


    xs = [x for x, _ in boundary_points]
    ys = [y for _, y in boundary_points]
    min_x = min(xs) - 1
    max_x = max(xs) + 1
    min_y = min(ys) - 1
    max_y = max(ys) + 1

    width  = max_x - min_x + 1
    height = max_y - min_y + 1



    boundary = [[False] * width for _ in range(height)]
    outside  = [[False] * width for _ in range(height)]

    for (x, y) in boundary_points:
        ix = x - min_x
        iy = y - min_y
        boundary[iy][ix] = True


    q = deque()
    start_ix, start_iy = 0, 0
    outside[start_iy][start_ix] = True
    q.append((start_ix, start_iy))


    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= width or ny < 0 or ny >= height:
                continue
            if boundary[ny][nx] or outside[ny][nx]:
                continue
            outside[ny][nx] = True
            q.append((nx, ny))


    interior: List[Point] = []

    for iy in range(1, height - 1):
        for ix in range(1, width - 1):
            if not boundary[iy][ix] and not outside[iy][ix]:
                x = ix + min_x
                y = iy + min_y
                interior.append((x, y))

    return interior

def top_rectangle_area(points: List[Tuple[int, int]]) -> int:
    top_area = 0
    for a, b in combinations(points, 2):
        area = calc_area(a, b)
        if area > top_area:
            top_area = area
    return top_area

def top_rectangle_area_constricted(points: List[Point], boundary: set[Point]) -> int:
    top_area = 0
    for a, b in combinations(points, 2):
        area = calc_area(a, b)
        if area > top_area:
            if all_valid_two(a, b, boundary, points):
                top_area = area
    return top_area


def all_valid(a: tuple[int,int], b: tuple[int,int], valid_points: set[tuple[int,int]]) -> bool:
    x1, y1 = a
    x2, y2 = b

    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if (x, y) not in valid_points:
                return False
    return True

from typing import Iterable, Tuple, Optional

Point = Tuple[int, int]

def print_grid(
    reds: Iterable[Point],
    greens: Iterable[Point] = (),
    rect: Optional[Tuple[Point, Point]] = None,
) -> None:
    reds = set(reds)
    greens = set(greens)

    rect_points: set[Point] = set()
    if rect is not None:
        (x1, y1), (x2, y2) = rect
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                rect_points.add((x, y))


    all_points = reds | greens | rect_points
    xs = [x for x, _ in all_points]
    ys = [y for _, y in all_points]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    for y in range(max_y, min_y - 1, -1):
        row_chars = []
        for x in range(min_x, max_x + 1):
            p = (x, y)
            if p in reds:
                ch = '#'
            elif p in greens:
                ch = 'X'
            else:
                ch = '.'

            if rect is not None and p in rect_points:
                ch = 'O'

            row_chars.append(ch)
        print("".join(row_chars))

def all_valid_two(a: Point, b: Point, boundary: set[Point], poly: List[Point]) -> bool:
    x1, y1 = a
    x2, y2 = b

    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            p = (x, y)


            if p in boundary:
                continue


            if not point_in_polygon(p, poly):
                return False

    return True

def point_in_polygon(p: Point, poly: List[Point]) -> bool:
    x, y = p
    inside = False
    n = len(poly)

    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]



        if ((y1 > y) != (y2 > y)) and (y2 - y1) != 0:

            x_intersect = x1 + (x2 - x1) * (y - y1) / (y2 - y1)
            if x_intersect > x:
                inside = not inside

    return inside

def main():
    reds = extract_data('data/realdata')
    print("fill_green")
    greens = fill_green(reds)
    boundary = set(reds) | set(greens)
    print("top_rectangle_area_constricted")
    print(top_rectangle_area_constricted(reds, boundary))
if __name__ == '__main__':
    main()
