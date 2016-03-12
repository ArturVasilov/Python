import unittest

from numba import int16

from watermark import generate_matrix
from watermark import generate_s_vector
from watermark import generate_watermark


def array_to_list(items):
    list_items = []
    for value in items:
        list_items.append(int16(value))
    return list_items


class MatrixVectorsGeneratingTest(unittest.TestCase):

    def test_generate_very_small_s_vector(self):
        s = generate_s_vector([0])
        self.assertListEqual([1], array_to_list(s))

    def test_generate_small_s_vector(self):
        s = generate_s_vector([0, 1, 1])
        self.assertListEqual([0, 0, 1], array_to_list(s))

    def test_generate_medium_s_vector(self):
        s = generate_s_vector([0, 1, 1, 0, 0, 1, 0])
        self.assertListEqual([0, 0, 0, 0, 0, 0, 1], array_to_list(s))

    def test_generate_large_s_vector(self):
        s = generate_s_vector([0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0])
        self.assertListEqual([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], array_to_list(s))

    def test_generate_very_small_matrix(self):
        matrix = generate_matrix([0, 1])
        self.assertListEqual([0, 1], array_to_list(matrix[0]))
        self.assertListEqual([0, 1], array_to_list(matrix[1]))

    def test_generate_small_matrix(self):
        matrix = generate_matrix([0, 1, 1, 0])
        self.assertListEqual([0, 1, 0, 0], array_to_list(matrix[0]))
        self.assertListEqual([0, 0, 1, 0], array_to_list(matrix[1]))
        self.assertListEqual([0, 0, 0, 1], array_to_list(matrix[2]))
        self.assertListEqual([0, 1, 1, 0], array_to_list(matrix[3]))

    def test_generate_medium_matrix(self):
        matrix = generate_matrix([0, 0, 1, 0, 1, 1, 0])
        self.assertListEqual([0, 1, 0, 0, 0, 0, 0], array_to_list(matrix[0]))
        self.assertListEqual([0, 0, 1, 0, 0, 0, 0], array_to_list(matrix[1]))
        self.assertListEqual([0, 0, 0, 1, 0, 0, 0], array_to_list(matrix[2]))
        self.assertListEqual([0, 0, 0, 0, 1, 0, 0], array_to_list(matrix[3]))
        self.assertListEqual([0, 0, 0, 0, 0, 1, 0], array_to_list(matrix[4]))
        self.assertListEqual([0, 0, 0, 0, 0, 0, 1], array_to_list(matrix[5]))
        self.assertListEqual([0, 0, 1, 0, 1, 1, 0], array_to_list(matrix[6]))

    def test_generate_large_matrix(self):
        matrix = generate_matrix([1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1])
        self.assertListEqual([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], array_to_list(matrix[0]))
        self.assertListEqual([0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], array_to_list(matrix[1]))
        self.assertListEqual([0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], array_to_list(matrix[2]))
        self.assertListEqual([0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], array_to_list(matrix[3]))
        self.assertListEqual([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], array_to_list(matrix[4]))
        self.assertListEqual([0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], array_to_list(matrix[5]))
        self.assertListEqual([0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], array_to_list(matrix[6]))
        self.assertListEqual([0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], array_to_list(matrix[7]))
        self.assertListEqual([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], array_to_list(matrix[8]))
        self.assertListEqual([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], array_to_list(matrix[9]))
        self.assertListEqual([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], array_to_list(matrix[10]))
        self.assertListEqual([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], array_to_list(matrix[11]))
        self.assertListEqual([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], array_to_list(matrix[12]))
        self.assertListEqual([1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1], array_to_list(matrix[13]))

    def test_small_watermark(self):
        watermark = generate_watermark([0, 1, 1])
        self.assertListEqual([1, -1, 1, 1, -1, 1, 1], array_to_list(watermark))

if __name__ == '__main__':
    unittest.main()
