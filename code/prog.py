# import library

# library.run_func()

import library

def failing():
    print("In changed function")

library.function = failing
# FIXME: not working as expected
library.run_func()
