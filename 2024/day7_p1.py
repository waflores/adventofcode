import itertools

# Parse incoming string in the form of:
# result<colon> <number> <number>...

DATA_FILE = "./day7-real-data.txt"
# In part 1, we need to devise with '+' and '*' - how to combine these numbers to equal result


def do_equation_probe(result_operands):
    result, operands = result_operands.split(":", 1)
    # Do conversion to int
    result = int(result)
    operands = [int(_operand) for _operand in operands.split()]

    operator_tracker = []
    # Let's go!
    intermediate_result = operands[0]

    for a, b in itertools.pairwise(operands):
        # Start with multiply first
        if intermediate_result * b > result:
            # We can't use multiplication (perhaps) - try addition.
            intermediate_result += b
            operator_tracker.append("+")
        else:
            intermediate_result *= b
            operator_tracker.append("*")

    if result == intermediate_result:
        return operator_tracker, intermediate_result, result
    else:
        operator_tracker = []
        intermediate_result = operands[0] + operands[1]
        operator_tracker.append("+")
        for a, b in itertools.pairwise(operands[1:]):
            if intermediate_result * b > result:
                # We can't use multiplication (perhaps) - try addition.
                intermediate_result += b
                operator_tracker.append("+")
            else:
                intermediate_result *= b
                operator_tracker.append("*")
        return operator_tracker, intermediate_result, result


def main():
    with open(DATA_FILE) as fh:
        number_data = fh.read().splitlines()
    calibration_sum = 0
    for line in number_data:
        print(f"Testing {line}:")
        operators_found, final_count, expected_count = do_equation_probe(line)
        if expected_count == final_count:
            calibration_sum += expected_count
            print(f"{operators_found} -> {expected_count}")
    print(f"Calibration Sum: {calibration_sum}")


if __name__ == "__main__":
    main()
