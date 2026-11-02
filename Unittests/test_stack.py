import unittest
from stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.test_stack = Stack()


    def test_initial_emptiness(self):
        self.assertEqual(len(self.test_stack.items), 0)
        self.assertTrue(self.test_stack.is_empty())


    def test_size(self):
        self.test_stack.push(5)
        self.assertEqual(len(self.test_stack.items), 1)
        self.test_stack.push(10)
        self.assertEqual(len(self.test_stack.items), 2)
        self.test_stack.push(15)
        self.assertEqual(len(self.test_stack.items), 3)
        self.test_stack.push(20)
        self.assertEqual(len(self.test_stack.items), 4)


    def test_simple_push(self):
        self.test_stack.push(5)

        self.assertEqual(self.test_stack.items[0], 5)
        self.assertEqual(len(self.test_stack.items), 1)
    def test_multi_push_reverse(self):
        self.test_stack.push(5)
        self.test_stack.push(10)
        self.test_stack.push(15)
        self.test_stack.push(20)

        self.assertEqual(self.test_stack.items[-1], 20)
        self.assertEqual(self.test_stack.items[-2], 15)
        self.assertEqual(self.test_stack.items[-3], 10)
        self.assertEqual(self.test_stack.items[-4], 5)
        self.assertEqual(len(self.test_stack.items), 4)
    def test_multi_push(self):
        self.test_stack.push(5)
        self.test_stack.push(10)
        self.test_stack.push(15)
        self.test_stack.push(20)

        self.assertEqual(self.test_stack.items[0], 5)
        self.assertEqual(self.test_stack.items[1], 10)
        self.assertEqual(self.test_stack.items[2], 15)
        self.assertEqual(self.test_stack.items[3], 20)
        self.assertEqual(len(self.test_stack.items), 4)

    
    def test_simple_pop(self):
        self.test_stack.push(5)
        self.test_stack.push(10)
        self.test_stack.push(15)
        self.test_stack.push(20)

        self.assertEqual(self.test_stack.pop(), 20)
        self.assertEqual(self.test_stack.items[-1], 15)
        self.assertEqual(len(self.test_stack.items), 3)
    def test_multi_pop(self):
        self.test_stack.push(5)
        self.test_stack.push(10)
        self.test_stack.push(15)
        self.test_stack.push(20)

        self.assertEqual(self.test_stack.pop(), 20)
        self.assertEqual(self.test_stack.pop(), 15)
        self.assertEqual(self.test_stack.pop(), 10)
        self.assertEqual(self.test_stack.items[-1], 5)
        self.assertEqual(len(self.test_stack.items), 1)
    def test_empty_pop(self):
        with self.assertRaises(IndexError):
            self.test_stack.pop()
    def test_full_pop(self):
        self.test_stack.push(5)
        self.test_stack.push(10)

        self.assertEqual(self.test_stack.pop(), 10)
        self.assertEqual(self.test_stack.pop(), 5)
        self.assertEqual(len(self.test_stack.items), 0)
        self.assertTrue(self.test_stack.is_empty())


    def test_empty_peek(self):
        with self.assertRaises(IndexError):
            self.test_stack.peek()
    def test_simple_peek(self):
        self.test_stack.push(5)

        self.assertEqual(self.test_stack.peek(), 5)
        self.assertEqual(len(self.test_stack.items), 1)
        self.assertEqual(self.test_stack.items[0], 5)
    def test_multi_peek(self):
        self.test_stack.push(5)
        self.assertEqual(self.test_stack.peek(), 5)
        self.test_stack.push(10)
        self.assertEqual(self.test_stack.peek(), 10)
        self.test_stack.push(15)
        self.test_stack.push(20)
        self.assertEqual(self.test_stack.peek(), 20)

if __name__ == "__main__":
    unittest.main()