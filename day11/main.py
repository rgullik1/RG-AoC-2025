import re
import random
def extract_data(file_path: str) -> dict[str, list[str]]:
    devices: dict[str, list[str]] = {}
    with open(file_path, 'r') as f:
        for raw in f:
            line = raw.strip()
            if not line or ':' not in line:
                continue
            left, right = line.split(':', 1)
            name = re.sub(r'[^A-Za-z]+', '', left)
            outputs_raw = right.strip().split()
            outputs = [re.sub(r'[^A-Za-z]+', '', s) for s in outputs_raw]
            outputs = [s for s in outputs if s]
            devices[name] = outputs
    return devices

def find_all_paths(devices: dict[str, list[str]], start: str, target: str) -> list[list[str]]:
    paths: list[list[str]] = []
    stack: list[tuple[str, list[str]]] = [(start, [])]
    while stack:
        node, path = stack.pop()
        if node == target:
            paths.append(path[:])
            continue
        for nxt in devices.get(node):
            if nxt in path:
                continue
            stack.append((nxt, path + [nxt]))
    return paths

def main():
    devices = extract_data('data/realdata')
    paths = find_all_paths(devices, 'you', 'out')
    print('paths:', paths)
    print('number of paths:', len(paths))

if __name__ == '__main__':
    main()