import unittest

from signals.homework1 import sum_cubes


class TestTask1(unittest.TestCase):

    def test_sum2(self):
        self.assertEquals(9, sum_cubes(2))

    def test_sum3(self):
        self.assertEquals(36, sum_cubes(3))

    def test_sum4(self):
        self.assertEquals(100, sum_cubes(4))

    def test_sum5(self):
        self.assertEquals(225, sum_cubes(5))

    def test_sum10(self):
        self.assertEquals(3025, sum_cubes(10))

    def test_sum20(self):
        self.assertEquals(44100, sum_cubes(20))

if __name__ == '__main__':
    unittest.main()