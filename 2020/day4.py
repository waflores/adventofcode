import pprint
import re

PASSPORT_FIELDS_RE = re.compile('(\w+):(\S*)')

VALID_FIELDS = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')


def get_passports():
    with open('day4input.txt') as fh:
        raw_data = fh.read().split('\n\n')
    return [PASSPORT_FIELDS_RE.findall(l) for l in raw_data]


def validate_passport(raw_passport):
    #     byr (Birth Year)
    #     iyr (Issue Year)
    #     eyr (Expiration Year)
    #     hgt (Height)
    #     hcl (Hair Color)
    #     ecl (Eye Color)
    #     pid (Passport ID)
    #     cid (Country ID)
    # We can skip cid and still consider it valid
    passport = dict(raw_passport)
    # passport_keys = []
    # passport_values = []
    # for key, value in raw_passport:
    #     passport_keys.append(key)
    #     passport_values.append(value)
    # print(passport_keys)
    return all(f in passport for f in VALID_FIELDS)


def part1():
    valid_passports = 0
    for p in get_passports():
        if validate_passport(p):
            valid_passports += 1
    print('Valid passport count: {0}'.format(valid_passports))  # not 198 or 259


if __name__ == '__main__':
    part1()
