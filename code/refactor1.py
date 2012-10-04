"""
Series of steps to pass from a messy function to many nice ones
"""

import subprocess
from os import chdir

import MySQLdb


def long_crappy_function():
    """Do a bit of everything
    """
    ## launching a shell command
    ls_cmd = 'ls'
    temp = '/tmp'
    p = subprocess.Popen(ls_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, chdir=temp)

    ## filtering the output of a shell command
    out, err = p.communicate()
    res = []
    for line in out:
        if 'to-match' in line:
            res.append(line)

    ## updating the results to database
    dbc = MySQLdb.connect(host='host', user='user', passwd='passwd', port='port')
    cursor = dbc.cursor(MySQLdb.cursors.DictCursor)

    for r in res:
       cursor.execute('INSERT INTO table VALUES (%s)' % r)
