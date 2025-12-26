import re
import time
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
        for next_node in devices.get(node):
            if next_node in path:
                continue
            stack.append((next_node, path + [next_node]))
    return paths

def find_all_paths_svr_fft_dac_out(devices: dict[str, list[str]], start: str, target: str) -> list[list[str]]:
    paths: list[list[str]] = []
    stack: list[tuple[str, list[str]]] = [(start, [])]
    while stack:
        node, path = stack.pop()
        if node == target and 'dac' in path and 'fft' in path:
            paths.append(path[:])
            continue
        if len(path) > 100:
            continue
        for next_node in devices.get(node, []):
            if next_node in path:
                continue
            stack.append((next_node, path + [next_node]))
    return paths

def main():
    devices = extract_data('data/realdata')
    print(devices)
    #Day 1
    start = time.time()
    paths = find_all_paths(devices, 'you', 'out')
    print('paths:', paths)
    print('number of paths:', len(paths))
    elapsed = time.time() - start
    print(f"Time taken: {elapsed:.2f} seconds")
    #Day 2
    start = time.time()
    paths2 = find_all_paths_svr_fft_dac_out(devices, 'svr', 'out')
    print("number of paths:", len(paths2))
    elapsed = time.time() - start
    print(f"Time taken: {elapsed:.2f} seconds")
if __name__ == '__main__':
    main()