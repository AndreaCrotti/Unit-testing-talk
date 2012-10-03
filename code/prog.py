from library import run_func

run_func()


def failing():
    print("In changed function")

import library
library.function = failing

run_func()
