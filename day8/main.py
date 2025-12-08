import math
from itertools import combinations
from typing import Iterable
all_boxes = []

class Box:
    x: int = 0
    y: int = 0
    z: int = 0
    circuit: int = 0

    def __init__(self, *args):
        if len(args) == 4 and all(isinstance(a, int) for a in args):
            self.x, self.y, self.z, self.circuit = args
        elif len(args) == 2:
            ints, circuit = args
            ints = list(ints)
            if len(ints) != 3 or not all(isinstance(a, int) for a in ints):
                raise ValueError("Expected 3 integers for coordinates")
            self.x, self.y, self.z = ints
            self.circuit = int(circuit)
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z}, circuit: {self.circuit})"

    def __repr__(self):
        return self.__str__()

class Circuit:
    boxes: list[Box]
def distance(box1: Box, box2: Box) -> float:
    return math.sqrt(pow(box1.x-box2.x,2) +
                     pow(box1.y-box2.y,2) +
                     pow(box1.z-box2.z,2))




def extract_data(file_path):
    with open(file_path) as f:
        return [list(map(int, line.split(","))) for line in f]


def smallest_distance(boxes: Iterable) -> tuple[float, tuple[int, int]]:
    min_d = math.inf
    min_pair = (-1, -1)
    for (i, b1), (j, b2) in combinations(enumerate(boxes), 2):
        if b1.circuit == b2.circuit:
            continue
        d = distance(b1, b2)
        if d < min_d:
            min_d = d
            min_pair = (i, j)
    return min_d, min_pair

def count_same_circuit(box: Box, boxes: list[Box]) -> int:
    cur_sum = 0
    for cbox in boxes:
        if box.circuit == cbox.circuit:
            cur_sum = cur_sum + 1
    return cur_sum

def merge_circuit(box1: Box, box2: Box) -> None:
    b1c = box1.circuit
    b2c = box2.circuit
    for box in all_boxes:
        if box.circuit == b2c:
            box.circuit = b1c

def most_popular_circuit(excluding_circuits: set[int]) -> tuple[int, int]:
    circuits: dict[int, int] = {}
    for box in all_boxes:
        if box.circuit in excluding_circuits:
            continue
        circuits[box.circuit] = circuits.get(box.circuit, 0) + 1

    if not circuits:
        return -1, 0

    max_circuit = max(circuits, key=circuits.get)
    return max_circuit, circuits[max_circuit]

def main():
    global all_boxes
    rows = extract_data("data/testdata")
    all_boxes = [Box(row, i) for i, row in enumerate(rows)]
    print(all_boxes)
    print(distance(all_boxes[0], all_boxes[1]))
    print(smallest_distance(all_boxes))
    x = 1
    while x < 10:
        dist, (b1, b2) = smallest_distance(all_boxes)
        b1_count = count_same_circuit(all_boxes[b1], all_boxes)
        b2_count = count_same_circuit(all_boxes[b2], all_boxes)
        if b1_count >= b2_count:
            merge_circuit(all_boxes[b1], all_boxes[b2])
        else:
            merge_circuit(all_boxes[b2], all_boxes[b1])
        print(all_boxes)
        x += 1
    for box in all_boxes:
        print(box)
    most_popular, ncircuits = most_popular_circuit(set())
    print(most_popular, ncircuits)

    most_popular2, ncircuits2 = most_popular_circuit({most_popular})
    print(most_popular2, ncircuits2)

    most_popular3, ncircuits3 = most_popular_circuit({most_popular, most_popular2})
    print(most_popular3, ncircuits3)
    print(math.prod([ncircuits, ncircuits2, ncircuits3]))

    # Reset
    all_boxes = []
    rows = extract_data("data/realdata")
    all_boxes = [Box(row, i) for i, row in enumerate(rows)]
    x = 1
    pairs = []
    for i, b1 in enumerate(all_boxes):
        for j in range(i + 1, len(all_boxes)):
            d = distance(b1, all_boxes[j])
            pairs.append((d, i, j))

    pairs.sort(key=lambda t: t[0])
    for k in range(10000):
        _, b1, b2 = pairs[k]
        b1_count = count_same_circuit(all_boxes[b1], all_boxes)
        b2_count = count_same_circuit(all_boxes[b2], all_boxes)
        if b1_count >= b2_count:
            merge_circuit(all_boxes[b1], all_boxes[b2])
        else:
            merge_circuit(all_boxes[b2], all_boxes[b1])
        if count_same_circuit(all_boxes[38], all_boxes) == 1000:
            print("DONE")
            print(all_boxes[b1], all_boxes[b2])
            print("all_boxes[b1] * all_boxes[b2] =", math.prod([all_boxes[b1].x, all_boxes[b2].x]))
            break
    most_popular, ncircuits = most_popular_circuit(set())
    print(most_popular, ncircuits)

    most_popular2, ncircuits2 = most_popular_circuit({most_popular})
    print(most_popular2, ncircuits2)

    most_popular3, ncircuits3 = most_popular_circuit({most_popular, most_popular2})
    print(most_popular3, ncircuits3)
    print(math.prod([ncircuits, ncircuits2, ncircuits3]))
if __name__ == "__main__":
    main()
