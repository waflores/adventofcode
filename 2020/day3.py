def get_map():
    with open('day3input.txt') as fh:
        raw_map = fh.read().splitlines()

    return [l.replace('--->', '').strip() for l in raw_map]


def tobogan_ride(moves_right=3, moves_down=1):
    # What do you get if you multiply together the number of trees encountered on each of the listed slopes?
    tree_count = 0
    current_column = 0
    length_of_row = 0
    next_valid_index = 0
    for index, row in enumerate(get_map()):
        # move 3 right, then move 1 down - evaluate
        if index == 0:
            length_of_row = len(row)
            current_column += moves_right
            next_valid_index += moves_down
            continue
        elif index == next_valid_index:
            next_valid_index += moves_down
            if row[current_column % length_of_row] == '#':
                tree_count += 1
            current_column += moves_right
    return tree_count


def part1():
    print('Number of Trees: {0}'.format(tobogan_ride(moves_right=3, moves_down=1)))


def part2():
    # Right 1, down 1.
    # Right 3, down 1.
    # Right 5, down 1.
    # Right 7, down 1.
    # Right 1, down 2.
    _magic_number = tobogan_ride(1) * tobogan_ride(3) * tobogan_ride(5) * tobogan_ride(7) * tobogan_ride(1, 2)
    print('magic number = {0}'.format(_magic_number))


if __name__ == '__main__':
    part2()
