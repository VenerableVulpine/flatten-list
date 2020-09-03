import unittest
import flatten_list

class TestFlattenIterable(unittest.TestCase):
    def setUp(self):
        self.ex1  = ['spam', 'eggs', ['bone', ['apple', 'teeth']], ('marrow'), ['stalk', 'filling']]
        self.ex2  = [1, (2, 3, 4, 5), 6]
        self.ex3  = []
        self.ex4  = 'juice'
        self.ex5  = 0
        self.res1 = ['spam', 'eggs', 'bone', 'apple', 'teeth', 'marrow', 'stalk', 'filling']
        self.res2 = [1, 2, 3, 4, 5, 6]
        self.res3 = []
        self.res4 = ['juice']
        self.res5 = [0]
    def test_flatten_iterable(self):    
        self.assertEqual(flatten_list.flatten_iterable(self.ex1), self.res1)
        self.assertEqual(flatten_list.flatten_iterable(self.ex2), self.res2)
        self.assertEqual(flatten_list.flatten_iterable(self.ex3), self.res3)
        self.assertEqual(flatten_list.flatten_iterable(self.ex4), self.res4)
        self.assertEqual(flatten_list.flatten_iterable(self.ex5), self.res5)
        
if __name__ == "__main__":
    unittest.main()
