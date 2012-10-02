GLOBAL_VALUE = 0

def smart_function(arg):
    if failure_condition:
        report_error(arg1)
    else:
        normal_behaviour(arg)


def test_adder():
    assert adder(0, 0) == 0
    assert adder(-1, 1) == 0


def adder(a, b):
    return a + b

test_adder()


def silly_function(value):
    global GLOBAL_VALUE
    GLOBAL_VALUE += 1
    return value
