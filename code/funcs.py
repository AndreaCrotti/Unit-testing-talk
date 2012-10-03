GLOBAL_VALUE = 0

from mock import patch

def rare_failure_condition():
    return False

def normal_behaviour(arg):
    return arg

def report_error(arg):
    print(arg)


def smart_function(arg0):
    if rare_failure_condition():
        report_error(argO)
    else:
        normal_behaviour(arg0)

@patch('__main__.rare_failure_condition', new=lambda: True)
def test_smart():
    smart_function(100)


def test_adder():
    assert adder(0, 0) == 0
    assert adder(-1, 1) == 0


def adder(a, b):
    return a + b

test_adder()


def silly_function(value):
    global GLOBAL_VALUE
    GLOBAL_VALUE += 1
    return (value * 2) + GLOBAL_VALUE


if __name__ == '__main__':
    test_smart()
