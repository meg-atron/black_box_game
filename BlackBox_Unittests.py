import unittest
from BlackBoxGame import BlackBoxGame, Board, Player

class TestBlackBox(unittest.TestCase):
    """"Creates a class to test LinkedList file"""


    def test_(self):
        """tests whether two items in the cart are added correctly at checkout"""


    def test_reverse(self):
        link_one = LinkedList()
        link_one.add(65)
        link_one.add("beach")
        link_one.add(5.4)
        link_one.add("ball")
        link_one.reverse()
        item = link_one.to_regular_list()
        self.assertEqual(item[0], "ball")

    def test_insert(self):
        link_one = LinkedList()
        link_one.add(65)
        link_one.add("beach")
        link_one.add(5.4)
        link_one.add("ball")
        link_one.insert("dog", 4)
        inserted = link_one.to_regular_list()
        self.assertEqual(inserted[4], "dog")

    def test_gradescope(self):
        link_one = LinkedList()
        link_one.add(65)
        link_one.add("beach")
        link_one.add(5.4)
        link_one.remove(65)
        link_one.remove("beach")
        link_one.remove(5.4)
        tester = link_one.is_empty()
        self.assertTrue(tester)




if __name__ == '__main__':
    unittest.main()