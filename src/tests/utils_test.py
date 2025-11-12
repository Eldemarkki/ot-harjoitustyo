import unittest
from utils import create_empty_2d_array, parse_pattern
from textwrap import dedent

class TestUtils(unittest.TestCase):
    def test_can_create_0_by_0_array(self):
        array = create_empty_2d_array(0, 0)
        self.assertEqual(len(array), 0)

    def test_can_create_5_by_3_array(self):
        array = create_empty_2d_array(3, 5)
        self.assertEqual(len(array), 3)
        self.assertEqual(len(array[0]), 5)

    def test_can_access_in_logical_order(self):
        array = create_empty_2d_array(3, 5)

        # First row (y), then column (x) 
        self.assertEqual(array[2][4], False)

    def test_can_parse_glider(self):
        glider = parse_pattern(dedent("""\
            .#.
            ..#
            ###"""))

        self.assertEqual(glider, [
            # First row
            [1, 0],
            # Second row
            [2, 1],
            # Third row
            [0, 2],
            [1, 2],
            [2, 2]
        ])
