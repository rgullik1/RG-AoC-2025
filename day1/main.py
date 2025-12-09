

def turn_wheel(twist: int, current_position: int):
    new_position = twist + current_position
    lands_on = new_position % 100
    return(lands_on)

def slowly_turn_wheel(twist: int, current_position: int)  -> tuple[int, int]:
    zero_crossings = 0
    while twist:
        if twist > 0:
            twist -= 1
            current_position += 1
            current_position = current_position % 100
            if current_position == 0:
                zero_crossings += 1
        if twist < 0:
            twist += 1
            current_position -= 1
            current_position = current_position % 100
            if current_position == 0:
                zero_crossings += 1
    return current_position, zero_crossings

def main():
    data_as_list = []
    current_pos = 50
    print(f"The dial starts by pointing at: {current_pos}")
    zeroed_out = 0
    crossed_zero = 0
    print("Hello from adv-of-code!")
    with open('day1data/data', 'r') as file:
        for line in file:
            data_as_list.append(line.strip())
            print(line.strip())
    data_as_list = [s.replace("L","-") for s in data_as_list]
    data_as_list = [s.replace("R","+") for s in data_as_list]
    data_as_list = [int(s) for s in data_as_list]
    print(data_as_list)
    for twist in data_as_list:
        current_pos, zero_crossings = slowly_turn_wheel(twist, current_pos)
        print(f"The dial is rotated {twist} to point at {current_pos}.")
        if current_pos == 0:
            zeroed_out += 1
        crossed_zero += zero_crossings

    print(f"zeroed_out: {zeroed_out}")
    print(f"crossed_zero: {crossed_zero}")
if __name__ == "__main__":
    main()

