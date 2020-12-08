import pprint
import re

PASSPORT_FIELDS_RE = re.compile('(\w+):(\S*)')

VALID_FIELDS = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')


def get_passports():
    with open('day4input.txt') as fh:
        raw_data = fh.read().split('\n\n')
    return [PASSPORT_FIELDS_RE.findall(l) for l in raw_data]


VALID_EYE_COLORS = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
VALID_HAIR_COLOR_RE = re.compile('^#[0-9a-f]{6}$')
VALID_PASSPORT_ID_RE = re.compile('^\d{9}$')
HEIGHT_RE = re.compile('^(?P<value>\d+)(?P<units>cm|in)$')
INVALID_YEAR = 'A'


def validate_passport(raw_passport):
    # cid (Country ID) - ignored, missing or not.
    passport = dict(raw_passport)
    if all(f in passport for f in VALID_FIELDS):
        try:
            _byr = int(passport.get('byr', INVALID_YEAR))
        except ValueError:
            return False
        try:
            _iyr = int(passport.get('iyr', INVALID_YEAR))
        except ValueError:
            return False
        try:
            _eyr = int(passport.get('eyr', INVALID_YEAR))
        except ValueError:
            return False
        try:
            _hgt = HEIGHT_RE.search(passport['hgt']).groupdict()
        except AttributeError:
            return False
        else:
            # hgt (Height) - a number followed by either cm or in:
            #     If cm, the number must be at least 150 and at most 193.
            #     If in, the number must be at least 59 and at most 76.
            tallness = int(_hgt['value'])
            if _hgt['units'] == 'cm':
                if not (150 <= tallness <= 193):
                    return False
            elif _hgt['units'] == 'in':
                if not (59 <= tallness <= 76):
                    return False

        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        return (1920 <= _byr <= 2002) and (2010 <= _iyr <= 2020) and (2020 <= _eyr <= 2030) and \
               VALID_HAIR_COLOR_RE.search(passport['hcl']) and VALID_PASSPORT_ID_RE.search(passport['pid']) and \
               passport['ecl'] in VALID_EYE_COLORS
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        # pid (Passport ID) - a nine-digit number, including leading zeroes.
    else:
        return False


def part1():
    valid_passports = 0
    for p in get_passports():
        if validate_passport(p):
            valid_passports += 1
    print('Valid passport count: {0}'.format(valid_passports))  # not 198 or 259


if __name__ == '__main__':
    part1()
