import unittest
from q3 import microscope, plush

class Testfunc(unittest.TestCase):
    def test_plush(self):
        self.assertEqual(plush(microscope(), [1, 2, 3, 4, 5]), 3)

if __name__ == '__main__':
    unittest.main()
