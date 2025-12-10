import re
from random import randint
from collections import deque
from heapq import heappush, heappop
from math import inf
from collections import defaultdict
import z3
class Problem:
    def __init__(self, lights: list[bool], buttons: list[tuple[int, ...]], joltage: list[int]):
        self.lights = lights
        self.buttons = buttons
        self.joltage = joltage

    def __str__(self):
        return f"Problem(lights={self.lights}, buttons={self.buttons}, joltage={self.joltage})"

    def __repr__(self):
        return self.__str__()

def to_int_tuples(s: str) -> list[tuple[int, ...]]:
    groups = re.findall(r'\(([^)]+)\)', s)  # extract contents inside each (...)
    return [tuple(int(x) for x in g.split(',')) for g in groups]


def extract_data(file_path):
    problem_list = []
    with open(file_path) as f:
        for line in f:
            lightsandrest = line.split("]")
            lights = lightsandrest[0].split("[")[1]
            buttons = lightsandrest[1].split("{")[0].strip()
            joltage = lightsandrest[1].split("{")[1].split("}")[0].strip()

            lightbools = [c == "#" for c in lights]
            buttons_listoftuples = to_int_tuples(buttons)
            joltage_list = [int(x) for x in joltage.split(",")]
            problem_list.append(Problem(lightbools, buttons_listoftuples, joltage_list))
    return problem_list

def flip(b: bool) -> bool:
    return not b

def press_button(current_state: list[bool], button: tuple[int, ...]) -> list[bool]:
    new_state = current_state[:]
    for index in button:
        if 0 <= index < len(new_state):
            new_state[index] = flip(new_state[index])
    return new_state

def push_button_two(current_state: list[int], button: tuple[int, ...]) -> list[int]:
    new_state = current_state[:]
    for index in button:
        if 0 <= index < len(new_state):
            new_state[index] += 1
    return new_state

def solver(solution: list[bool], buttons: list[tuple[int, ...]]) -> float:
    initial_lights = [False] * len(solution)
    current_best = float('inf')
    lowest_possible = 0
    if initial_lights == solution:
        return 0
    for _ in range(100000):
        test_lights = initial_lights[:]
        presses = 0
        while test_lights != solution:
            button_to_press = buttons[randint(0, len(buttons) - 1)]
            test_lights = press_button(test_lights, button_to_press)
            presses += 1
            if presses >= current_best:
                break
        if test_lights == solution and presses < current_best:
            current_best = presses
            if current_best == lowest_possible:
                break
    return current_best

from math import inf

from math import inf
from collections import defaultdict

def solver_p2(solution: list[int], buttons: list[tuple[int, ...]]) -> float:
    opt = z3.Optimize()

    button_presses = [z3.Int(f"x_{i}") for i in range(len(buttons))]
    for presses in button_presses:
        opt.add(presses >= 0)

    for i, required_joltage  in enumerate(solution):
        contributing_presses = [button_presses[j] for j, button in enumerate(buttons) if i in button]
        total_contribution = z3.Sum(contributing_presses) if contributing_presses else z3.IntVal(0)
        opt.add(total_contribution == required_joltage)

    total_presses = z3.Sum(button_presses)
    opt.minimize(total_presses)

    if opt.check() != z3.sat:
        return inf

    model = opt.model()
    return float(model.eval(total_presses).as_long())


def main():
    problem_list = extract_data("data/realdata")
    tot_presses = 0
  #  for problem in problem_list:
  #      result = solver(problem.lights, problem.buttons)
   #     print(f"Result for problem {problem}: {result}")
   #     tot_presses += result
    for i, problem in enumerate(problem_list):
        print("-----")
        print(f"Starting problem {i}: {problem}")
        result = solver_p2(problem.joltage, problem.buttons)
        print(f"Result for problem {problem}: {result}")

        tot_presses += result
    print(f"Total presses: {tot_presses}")
if __name__ == "__main__":
    main()
