import unittest
import os
from subprocess import getoutput, getstatusoutput


class TestSuit(unittest.TestCase):
	def setUp(self) -> None:
		self.prg = './hello.py'

	def test_ans(self):
		self.assertEqual(int('5'), 5)

	def test_exists(self):
		self.assertTrue(os.path.isfile(self.prg))

	def test_runnable(self):
		_, out = getstatusoutput(f'python {self.prg}')
		self.assertTrue(out)
		self.assertEqual(out.strip(), 'help please people')


if __name__ == '__main__':
	unittest.main()
