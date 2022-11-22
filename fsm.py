
import unittest
from unittest import TestCase
code = input('enter password: ')
def match(code):
    state = 0
    for num in code:
        if state == 0:
            if num == "8":
                state = 1
        elif state == 1:
            if num == "4":
                state = 2
            elif num == "8":
                state = 1
            else:
                state = 0
        elif state == 2:
            if num == "5":
                state = 34
            elif num == "8":
                state = 1
            else:
                state = 0

        elif state == 34:
            if num == "4":
                state = 44
            elif num == "8":
                state = 1
            else:
                state = 0
        elif state == 44:
            if num == "4":
                state = 54
            elif num == "8":
                state = 1
            else:
                state = 0
        elif state == 54:
            if num == "4":
                state = 64
                return ("lock")
            elif num == "1":
                state = 6
                return ("unlock")
            elif num == "8":
                state = 1
            else:
                state = 0
match('845441')
class TestSum(unittest.TestCase):

    def test_sum1(self):
        self.assertEqual(match("9135203344124510334441238454412334451334410101"), "unlock")
    def test_sum2(self):
        self.assertEqual(match("9135203344124510334441238454442334451334410101"), "lock")
    def test_sum3(self):
        self.assertEqual(match("9135203845444344124510334441238454412334458454441334410101"), 'lock', "unlock")
    def test_sum4(self):
        self.assertEqual(match("4280396746897290462896589479240609826547845441185745643075608946785845444"), "unlock", "lock")
    def test_sum5(self):
        self.assertEqual(match("845441"), "unlock")
    def test_sum6(self):
        self.assertEqual(match("845444"), "lock")

if __name__ == '__main__':
    unittest.main()





