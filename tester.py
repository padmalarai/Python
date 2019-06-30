import unittest

def sum(a,b):
    return a+b


def multi(a,b):
    return a*b

def  triare(base,height):
    return base*height/2


class TestClass(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(3,5),8)
        self.assertEqual(sum(0,0),0)
    def test_multi(self):
        self.assertEqual(multi(3,5),15)
        self.assertEqual(multi(0,5),0)
    def test_triare(self):
        self.assertEqual(triare(3,5),7.5)
        self.assertEqual((0,5),0)


unittest.main()

        
