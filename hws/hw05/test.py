import traceback
import unittest
from hw05 import repeated, merge

class Testhw(unittest.TestCase):
    def test_repeated(self):
        try:
            lst = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
            self.assertEqual(repeated(lst, 2), 9)
        except Exception as e:
            print("An error occured: ", e)
            traceback.print_exc()
    def test_merge(self):
        m = merge([0, 2, 4, 6, 8, 10, 12, 14], [0, 3, 6, 9, 12, 15])
        breakpoint()
        self.assertEqual(list(m), [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15])
    



if __name__ == '__main__':
    unittest.main()



