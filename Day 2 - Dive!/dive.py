def part_one():
    with open('input.txt') as input_file:
        input_lines = input_file.readlines()

    horizontal_position = 0
    depth = 0
    for line in input_lines:
        command, value = line.split()
        value = int(value)

        if command == 'forward':
            horizontal_position += value
        elif command == 'down':
            depth += value
        elif command == 'up':
            depth -= value

    return horizontal_position * depth


def part_two():
    with open('input.txt') as input_file:
        input_lines = input_file.readlines()

    horizontal_position = 0
    depth = 0
    aim = 0

    for line in input_lines:
        command, value = line.split()
        value = int(value)

        if command == 'forward':
            horizontal_position += value
            depth += aim * value
        elif command == 'down':
            aim += value
        elif command == 'up':
            aim -= value

    return horizontal_position * depth


if __name__ == '__main__':
    print(f'Part 1: {part_one()}')

    print(f'Part 2: {part_two()}')
