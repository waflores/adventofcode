import itertools

DATA_FILE = "./day7-real-data.txt"
#  89195306971 - without brute force
# 303943215325 - with brute force


def do_equation_probe(result_operands):
    result, operands = result_operands.split(":", 1)
    # Do conversion to int
    result = int(result)
    operands = [int(_operand) for _operand in operands.split()]

    # Come up with the routine based on the number of operators needed
    operator_count = len(operands) - 1
    for op_seq in itertools.product("*+", repeat=operator_count):
        # Each tuple gives us instructions on how to proceed
        intermediate_result = operands[0]
        operator_tracker = []
        for index, operand in enumerate(operands[1:]):
            current_operator = op_seq[index]
            if current_operator == "+":
                if intermediate_result + operand > result:
                    # Bail out, we messed up!
                    break
                else:
                    intermediate_result += operand
                    operator_tracker.append("+")
            else:
                # it's a multiply
                if intermediate_result * operand > result:
                    # Bail out, we messed up!
                    break
                else:
                    intermediate_result *= operand
                    operator_tracker.append("*")
        if intermediate_result == result:
            return operator_tracker, intermediate_result, result
    else:
        return operator_tracker, intermediate_result, result


"""
2 = 1: +, *
3 = 2: + +, * *, + *, * +
4 = 3: + + +, + + *, + * *, * * *, * * +, * + +, * + *, + * +
itertools.product("*+", repeat=3)
"""


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
