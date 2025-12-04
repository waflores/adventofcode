# Each input is 'a-b\s\w:\s+(\S*)'
import re

RULE_INPUT_RE = re.compile(r'(?P<min>\d+)-(?P<max>\d+)\s(?P<rule>\w):\s(?P<password>\S*)')


def get_rules():
    with open('day2input.txt') as fh:
        raw_data = fh.read().splitlines()
    return [RULE_INPUT_RE.match(r).groupdict() for r in raw_data]


def part1():
    # How many passwords are valid according to their policies?
    valid_count = 0
    for rule in get_rules():
        _min = int(rule['min'])
        _max = int(rule['max'])
        _password = rule['password']
        matches = re.findall(rule['rule'], _password)
        print('{0} -> {1}'.format(_password, matches))
        if _min <= len(matches) <= _max:
            valid_count += 1
    print('Valid Passwords: {0}'.format(valid_count))


def part2():
    # How many passwords are valid according to the new interpretation of the policies?
    # Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter.
    #   Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
    valid_count = 0
    for rule in get_rules():
        _pos1 = int(rule['min']) - 1
        _pos2 = int(rule['max']) - 1
        _password = rule['password']
        matches = re.finditer(rule['rule'], _password)
        _all_pos = [m for m in matches if m.start() in (_pos1, _pos2)]
        if _all_pos:
            print((_password, _pos1, _pos2, _all_pos))
        if len(_all_pos) == 1:
            valid_count += 1
    print('Valid Passwords: {0}'.format(valid_count))


if __name__ == '__main__':
    part2()
