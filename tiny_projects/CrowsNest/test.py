import unittest
from subprocess import getoutput, getstatusoutput
import os


class TestSuit(unittest.TestCase):
    def setUp(self) -> None:
        self.prg = './solution.py'

    def test_is_exist(self):
        self.assertTrue(os.path.isfile(self.prg))

    def test_runnable(self):
        out = getoutput(f'python {self.prg} ali')
        self.assertTrue(out)

    def test_lower_input(self):
        out = getoutput(f'python {self.prg} zebra')
        self.assertEqual(out, 'aloha, captain  a zebra  larboard bow')

    def test_capital_input(self):
        out = getoutput(f'python {self.prg} Zebra')
        self.assertEqual(out, 'aloha, captain  a Zebra  larboard bow')

    def test_lower_input_vowel(self):
        out = getoutput(f'python {self.prg} animal')
        self.assertEqual(out, 'aloha, captain  an animal  larboard bow')

    def test_capital_input_vowel(self):
        out = getoutput(f'python {self.prg} Animal')
        self.assertEqual(out, 'aloha, captain  an Animal  larboard bow')


if __name__ == '__main__':
    unittest.main()
