msg_0 = "Enter an equation\n"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."

term_validated = False
x, oper, y = 0, "", 0
while not term_validated:
    x, oper, y = input(msg_0).split()

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue

    if oper not in ["+", "-", "*", "/"]:
        print(msg_2)
        continue

    if oper == "/" and y == 0:
        print(msg_3)
        continue
    term_validated = True
if oper == "+":
    result = x + y
if oper == "-":
    result = x - y
if oper == "*":
    result = x * y
else:
    result = x / y
print(result)
