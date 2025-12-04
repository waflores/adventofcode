def get_boarding_passes():
    with open('day5input.txt') as fh:
        return fh.read().splitlines()


def determine_row(row_sequence, lo=0, hi=127):
    for r in row_sequence:
        mid = (lo + hi) // 2
        if r in ('F', 'L'):
            hi = mid
        elif r in ('B', 'R'):
            lo = mid + 1
    return lo


def generate_seat_id(encoded_seat):
    row = determine_row(encoded_seat[:7])
    column = determine_row(encoded_seat[7:], hi=7)
    return row * 8 + column


def part1():
    max_seat_id = max([generate_seat_id(i) for i in get_boarding_passes()])
    print(max_seat_id)


def part2():
    all_seats = set(range(0, 833))
    decoded_seats = {generate_seat_id(bp) for bp in get_boarding_passes()}
    print(all_seats - decoded_seats)  # It's the last element here...
    print(decoded_seats)


if __name__ == '__main__':
    part2()
