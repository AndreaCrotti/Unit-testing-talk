"""
Series of steps to pass from a messy function to many nice ones
"""

import subprocess
from os import chdir


def long_crappy_function():
    """Do a bit of everything
    """
    ls_cmd = 'ls'
    temp = '/tmp'
    chdir(temp)
    p = subprocess.Popen(ls_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)    

    out, err = p.communicate()
    res = []
    for line in out:
        if 'to-match' in line:
            res.append(line)

    for r in res:
        pass
