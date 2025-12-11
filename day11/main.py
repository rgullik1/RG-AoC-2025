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

def main():
    devices = extract_data('data/testdata')
    print(devices)
    current_outputs = devices.get('you', [])
    while 'out' not in current_outputs:
        current_outputs = devices.get(
if __name__ == '__main__':
    main()