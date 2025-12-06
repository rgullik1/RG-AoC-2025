import math
from itertools import zip_longest

class Problem:
    def __init__(self) -> None:
        self.problem: list[int] = []
        self.operator: str = ""


    def __str__(self) -> str:
        return f"{self.problem} {self.operator}"

    def __repr__(self) -> str:
        return f"Problem(problem={self.problem}, operator='{self.operator}')"


def build_number(strl: list[str]) -> int | None:
    new_str = "".join(strl).strip()
    if new_str == "":
        return None
    return int(new_str)

def extract_operator(chars: list[str]) -> str | None:
    for ch in chars:
        ch = ch.strip()  # remove whitespace
        if ch in {"+", "*"}:
            return ch
    return None

def is_all_empty(items: list[str]) -> bool:
    return all(x.strip() == "" for x in items)


def extract_data(file_path) -> list[str]:
    rows: list[list[str]] = []
    with open(file_path, "r") as f:
        for line in f:
            rows.append(line.split())
    transposed = list(map(list, zip(*rows)))




def extract_weird(file_path) -> list[Problem]:
    rows: list[list[str]] = []
    with open(file_path, "r") as f:
        for line in f:
            rows.append(list(line.rstrip("\n")))

    transposed = list(map(list, zip_longest(*rows, fillvalue=" ")))

    current_problem: Problem | None = None
    current_operator = ""
    problem_list: list[Problem] = []

    for l in transposed:
        if current_problem is None:
            current_problem = Problem()

        if is_all_empty(l):
            current_problem.operator = current_operator
            problem_list.append(current_problem)
            current_problem = None
            current_operator = ""
        else:
            current_operator = extract_operator(l) or current_operator
            numeral = build_number(l[:-1])
            if numeral is not None:
                current_problem.problem.append(numeral)

    if current_problem is not None and current_problem.problem:
        current_problem.operator = current_operator
        problem_list.append(current_problem)

    return problem_list

    return rows


    print(transposed)
def math_it(problem: list[str]) -> int:
    operator = problem.pop()
    problem = list(map(int, problem))
    if operator == "+":
        return sum(problem)
    if operator == "*":
        return math.prod(problem)
    print("ERROR")
    return 0

def math_problem(problem: Problem) -> int:
    if problem.operator == "+":
        return sum(problem.problem)
    if problem.operator == "*":
        return math.prod(problem.problem)
    print("ERROR")
    return 0

def main():
    # Day 1
    columns = extract_data("data/testdata")
    acc_sum = 0

    for column in columns:

        acc_sum = acc_sum + math_it(column)
    print(acc_sum)
    # Day 2
    weird_data = extract_weird("data/realdata")
    weird_acc_sum = 0
    for problem in weird_data:
        weird_acc_sum = weird_acc_sum + math_problem(problem)
    print(weird_acc_sum)

if __name__ == "__main__":
    main()
