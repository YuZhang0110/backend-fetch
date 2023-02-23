import unittest
import mycode

class TestSpendPoints(unittest.TestCase):
    def testSpendPoints1(self):
        # Test case 1
        transactions = "transactions.csv"
        points2Spend = 5000
        expected_output = {
            "DANNON": 1000,
            "UNILEVER": 0,
            "MILLER COORS": 5300
        }
        result = mycode.spendPoints(points2Spend, transactions)
        self.assertDictEqual(result, expected_output)
    def testSpendPoints2(self):
        # Test case 2
        transactions = "transactions.csv"
        points2Spend = 5000
        expected_output = {
            "DANNON": 500,
            "UNILEVER": 0,
            "MILLER COORS": 5300
        }
        result = mycode.spendPoints(points2Spend, transactions)
        self.assertDictEqual(result, expected_output)

    def testSpendPoints3(self):
        # Test case 3
        transactions = "transactions.csv"
        points2Spend = 6000
        expected_output = {
            "DANNON": 1000,
            "UNILEVER": 0,
            "MILLER COORS": 4300
        }
        result = mycode.spendPoints(points2Spend, transactions)
        self.assertDictEqual(result, expected_output)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestSpendPoints("testSpendPoints1"))
    suite.addTest(TestSpendPoints("testSpendPoints2"))
    suite.addTest(TestSpendPoints("testSpendPoints3"))
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)
