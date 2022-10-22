msg_0 = "Enter an equation\n"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):\n"
msg_5 = "Do you want to continue calculations? (y / n):\n"


def parse_memory_or_float(x, memory):
    if x == "M":
        return memory
    return float(x)


def read_operation(memory):
    valid = False
    x, operator, y = 0, "", 0
    while not valid:
        x, operator, y = input(msg_0).split()
        try:
            x = parse_memory_or_float(x, memory)
            y = parse_memory_or_float(y, memory)
        except ValueError:
            print(msg_1)
            continue

        if operator not in ["+", "-", "*", "/"]:
            print(msg_2)
            continue

        if operator == "/" and y == 0:
            print(msg_3)
            continue
        valid = True
    return x, operator, y


def calculate(x, operator, y):
    result = x
    if operator == "+":
        result += y
    if operator == "-":
        result -= y
    if operator == "*":
        result *= y
    if operator == "/":
        result /= y
    return result


def positive_answered(question):
    choice = input(question)
    while choice not in ["y", "n"]:
        choice = input(question)
    return True if choice == "y" else False


def main():
    continue_calc = True
    memory = 0
    while continue_calc:
        x, operator, y = read_operation(memory)
        result = calculate(x, operator, y)
        print(result)
        if positive_answered(msg_4):
            memory = result
        continue_calc = positive_answered(msg_5)


main()
