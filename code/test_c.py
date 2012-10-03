from ctypes import *

libsum = cdll.LoadLibrary('./libsum.so.1.0.1')

for i in range(100):
    for j in range(100):
        # print("Checking that %d + %d is correct" % (i, j))
        assert libsum.sum(i, j) == i + j, "%d + %d failed!!" % (i, j)
