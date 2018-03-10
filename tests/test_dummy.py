import unittest


class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_dummy(self):
        self.assertEqual("1", "1")


if __name__ == '__main__':
    unittest.main()
