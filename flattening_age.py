rom
func
tools
import reduce


def multiply(args_add):
    return (lambda *args_add: reduce(lambda a, b: a * b, args_add))(*args_add)


def add(args_add):
    return (lambda *args_add: reduce(lambda a, b: a + b, args_add))(*args_add)


def substract(args_add):
    return (lambda *args_add: reduce(lambda a, b: a - b, args_add))(*args_add)


def divice(args_add):f
    try:
        return (lambda *args_add: reduce(lambda a, b: a / b, args_add))(*args_add)
    except:
        return ""


def operate(*args):
    action_d = {"+": add, "-": substract, "*": multiply, "/": divice}
    action = args[0]
    data = tuple([int(args[i]) for i in range(1, len(args))])
    if action in action_d:
        return action_d[action](data)
