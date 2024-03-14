
import unittest

from fibo.model.fibo import Fibonacci

class TestFibonacci(unittest.TestCase):
    def setUp(self) -> None:
        self.fibo = Fibonacci()

    def test_series(self):
        series = self.fibo.series(0)
        self.assertEqual(series, [0])

        series = self.fibo.series(1)
        self.assertEqual(series, [0,1])

        series = self.fibo.series(2)
        self.assertEqual(series, [0,1,1])

        series = self.fibo.series(5)
        self.assertEqual(series, [0,1,1,2,3,5])

    def test_sum(self):
        sum = self.fibo.sum(0)
        self.assertEqual(sum, 0)

        sum = self.fibo.sum(1)
        self.assertEqual(sum, 1)

        sum = self.fibo.sum(2)
        self.assertEqual(sum, 2)

        sum = self.fibo.sum(5)
        self.assertEqual(sum, 12)

if __name__ == '__main__':
    unittest.main()
