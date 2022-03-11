import unittest
from travellingSalesMan import WeightedGraph

class TestTSM(unittest.TestCase):

    def testCase_1(self):
        graph = WeightedGraph([1,2,3,4])
        graph.addCost(1, 2, 10)
        graph.addCost(1, 4, 20)
        graph.addCost(1, 3, 15)
        graph.addCost(2, 4, 25)
        graph.addCost(2, 3, 35)
        graph.addCost(3, 4, 30)
        
        result = graph.getMinPath(1)
        self.assertEqual(result, 80)

    def testCase_2(self):
        graph = WeightedGraph([1,2,3,4,5])
        graph.addCost(1, 5, 75)
        graph.addCost(1, 4, 100)
        graph.addCost(1, 3, 300)
        graph.addCost(1, 2, 100)
        graph.addCost(2, 5, 125)
        graph.addCost(2, 4, 75)
        graph.addCost(2, 3, 50)
        graph.addCost(3, 5, 125)
        graph.addCost(3, 4, 100)
        graph.addCost(4, 5, 50)
        result = graph.getMinPath(1)
        self.assertEqual(result, 375)

    def testCase_3(self):
        graph = WeightedGraph([1,2,3,4])
        graph.addCost(1, 2, 2)
        graph.addCost(1, 3, 5)
        graph.addCost(1, 4, 7)
        graph.addCost(2, 3, 8)
        graph.addCost(2, 4, 3)
        graph.addCost(3, 4, 1)
        result = graph.getMinPath(1)
        self.assertEqual(result, 11)

if __name__ == '__main__':
    unittest.main()