import unittest

from signals.homework1 import task2


class TestTask1(unittest.TestCase):

    def test_input1(self):
        numbers = [5]
        middle, median = task2(numbers)
        self.assertEquals(5, middle)
        self.assertEquals(5, median)

    def test_input2(self):
        numbers = [5, 8]
        middle, median = task2(numbers)
        self.assertEquals(6.5, middle)
        self.assertEquals(6.5, median)

    def test_input3(self):
        numbers = [1, 2, 3, 4]
        middle, median = task2(numbers)
        self.assertEquals(2.5, middle)
        self.assertEquals(2.5, median)

    def test_input4(self):
        numbers = [1, 2, 3, 4, 10]
        middle, median = task2(numbers)
        self.assertEquals(4, middle)
        self.assertEquals(3, median)

    def test_input5(self):
        numbers = [20, 45, 70, 10, 3, 19, 71, 89, 133, 65]
        middle, median = task2(numbers)
        self.assertEquals(52.5, middle)
        self.assertEquals(55, median)

        self.assertEquals(20, numbers[0])
        self.assertEquals(3, numbers[4])
        self.assertEquals(71, numbers[6])
        self.assertEquals(65, numbers[9])

if __name__ == '__main__':
    unittest.main()