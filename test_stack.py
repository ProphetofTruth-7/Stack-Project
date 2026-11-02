import unittest
from stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.singly_linked_list = SinglyLinkedList()
        self.test_list1 = [1, 2, 3, 4]
        self.test_list2 = [3, 1, 2, 3, 3, 4, 3]
        self.test_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15]
        self.test_list4 = [86, 45, 34, 78, 79, 34, 20, 39, 4, 32, 11]


    def test_simple_append(self):
        self.singly_linked_list.append(1)

        self.assertEqual(self.singly_linked_list._head.data, 1)
        self.assertEqual(len(self.singly_linked_list), 1)

        self.assertEqual(self.singly_linked_list._tail.next, None)
        self.assertEqual(self.singly_linked_list._tail.data, 1)

if __name__ == "__main__":
    unittest.main()