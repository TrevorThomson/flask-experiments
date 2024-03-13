
import unittest

from fibo.__main__ import create_service

class TestFibonacci(unittest.TestCase):
    def setUp(self) -> None:
        app = create_service()
        app.testing = True
        self.app = app.test_client()

    def test_home(self):
        result = self.app.get('/')
        self.assertTrue('Home Page' in result.get_data(as_text=True))

    def test_hello(self):
        result = self.app.get('/hello/Chuck')
        self.assertTrue('Hello, Chuck!' in result.get_data(as_text=True))

    def test_fibo(self):
        result = self.app.get('/fibo/3')
        self.assertTrue('Fibonacci(3)' in result.get_data(as_text=True))
        self.assertTrue('[0, 1, 1, 2]' in result.get_data(as_text=True))
        self.assertTrue('sums to 4' in result.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
