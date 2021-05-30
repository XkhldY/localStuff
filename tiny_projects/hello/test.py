import unittest


class TestSuit(unittest.TestCase):

	def test_ans(self):
		self.assertEqual(int('5'), 5)


if __name__ == '__main__':
	unittest.main()
