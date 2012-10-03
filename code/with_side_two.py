import unittest

import with_side_one
from os import remove
from mock import patch

TMP = 'tempfile.txt'
TEXT = 'firstline\nsecond line'
DESIRED = TEXT.splitlines()


# first manual approach

def test_read_from_disk():
    old_fname = with_side_one.FNAME
    with_side_one.FNAME = TMP

    open(TMP, 'w').write(TEXT)
    assert with_side_one.read_from_disk() == DESIRED

    remove(TMP)
    with_side_one.FNAME = old_fname

# using unittest

class TestReadFromDisk(unittest.TestCase):
    def setUp(self):
        self.old_fname = with_side_one.FNAME
        with_side_one.FNAME = TMP
        open(TMP, 'w').write(TEXT)

    def tearDown(self):
        with_side_one.FNAME = self.old_fname
        remove(TMP)

    def test_read_from_disk(self):
        res = with_side_one.read_from_disk()
        self.assertEqual(res, DESIRED)


# using unittest and mock
@patch('with_side_one.FNAME', new=TMP)
class TestReadFromDiskMocked(unittest.TestCase):
    def setUp(self):
        open(TMP, 'w').write(TEXT)

    def tearDown(self):
        remove(TMP)

    def test_read_from_disk(self):
        res = with_side_one.read_from_disk()
        self.assertEqual(res, DESIRED)


if __name__ == '__main__':
    test_read_from_disk()
    unittest.main()

# Use "nosetests-2.7 with_side_two.py -sv --with-cov --cov-report=term-missing"
# to run the tests and show the report of the missing lines