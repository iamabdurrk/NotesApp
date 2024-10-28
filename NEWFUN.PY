# multiplication of n numbers
def multiply(*args):
    result = 1
    for i in args:
        result *= i
    return result

# sbtraction of n numbers
def subtract(*args):
    result = args[0]
    for i in args[1:]:
        result -= i
    return result