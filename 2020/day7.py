# https://stackoverflow.com/questions/22937618/reference-what-does-this-regex-mean/22944075#22944075
# https://www.regular-expressions.info/reference.html
# https://github.com/banach-space/llvm-tutor
# https://indefinitestudies.org/2011/04/23/generic-iterative-dataflow-analysis-in-python/

import pprint
import re

RULES_RE = re.compile('(?P<qty>\d+)?[ ]?(?P<color>\w+ \w+) bag[s]?[^,.]?')


def get_luggage_rules():
    with open('day7input.txt') as fh:
        raw_data = fh.read().splitlines()
    return raw_data


def part1():
    # In other words: how many colors can, eventually, contain at least one shiny gold bag?
    luggage_rule_book = {}
    for _raw_rule in get_luggage_rules():
        _parsed_rule = RULES_RE.findall(_raw_rule)
        _key = _parsed_rule[0][1]
        _values = {}
        for _v in _parsed_rule[1:]:
            _str_qty, _color = _v
            try:
                _qty = int(_str_qty)
            except ValueError:
                _qty = 0
            _values[_color] = _qty
        luggage_rule_book[_key] = _values
    # pprint.pprint(luggage_rule_book)

    # Coalesce for 'shiny gold' bag
    coalesced_rule_book = {}
    for _color, _bag_combos in luggage_rule_book.items():
        print(_color, _bag_combos)
        for _inner_bag, _inner_qty in _bag_combos.items():
            if _inner_bag in ('shiny gold', 'no other'):
                continue
            print('{0!r} can hold: {1}'.format(_inner_bag, luggage_rule_book[_inner_bag]))


if __name__ == '__main__':
    part1()
