import itertools


def part1():
    # Part 1: Find the two entries that sum to 2020; what do you get if you multiply them together?
    with open('day1input.txt') as fh:
        expense_report = [int(i) for i in fh]

    for i in expense_report:
        m = 2020 - i
        if m in expense_report:
            print(i * m)


def part2():
    # Part 2: In your expense report, what is the product of the three entries that sum to 2020?
    with open('day1input.txt') as fh:
        expense_report = [int(i) for i in fh]

    for i in itertools.combinations(expense_report, 3):
        m = sum(i)
        if m == 2020:
            print('{0} = {1}'.format(i, i[0]*i[1]*i[2]))


if __name__ == '__main__':
    part2()
