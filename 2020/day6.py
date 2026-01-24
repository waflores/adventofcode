import collections


def get_custom_responses():
    with open('day6input.txt') as fh:
        raw_data = fh.read().split('\n\n')
    return raw_data


def part1():
    print(sum([len(set(s.replace('\n', ''))) for s in get_custom_responses()]))


def part2():
    running_count = 0
    for group_responses in get_custom_responses():
        custom_responses = group_responses.split()
        num_in_group = len(custom_responses)
        if num_in_group == 1:
            running_count += len(custom_responses[0])
        else:
            response_counter = collections.Counter()
            for person in custom_responses:
                response_counter.update(person)
            subgroup_tally = list(response_counter.values()).count(num_in_group)
            running_count += subgroup_tally
    print(running_count)


if __name__ == '__main__':
    part2()
