from typing import List


def part_one():
    increasing_values_count = 0

    with open('input.txt') as input_file:
        input_lines = input_file.readlines()

    previous_value = None
    for line in input_lines:
        current_value = int(line)
        if previous_value and current_value > previous_value:
            increasing_values_count += 1

        previous_value = current_value

    print(increasing_values_count)


def part_two():
    increasing_values_count = 0

    with open('input.txt') as input_file:
        input_lines = input_file.readlines()

    sliding_window_length = 3

    sliding_window_lists: List[List[int]] = [[]] * sliding_window_length

    previous_sliding_window_total = None
    current_sliding_window_total = None
    for index, line in enumerate(input_lines):
        current_value = int(line)

        sliding_window_lists[index % sliding_window_length] = [0] * sliding_window_length

        for window_list_index in range(min(sliding_window_length, index + 1)):
            sliding_window_lists[index % sliding_window_length - window_list_index][window_list_index] = current_value

        if index >= sliding_window_length - 1:
            current_sliding_window_total = sum(sliding_window_lists[(index + 1) % sliding_window_length])

            if previous_sliding_window_total and current_sliding_window_total > previous_sliding_window_total:
                increasing_values_count += 1

        if current_sliding_window_total:
            previous_sliding_window_total = current_sliding_window_total

    print(increasing_values_count)


if __name__ == '__main__':
    part_two()
