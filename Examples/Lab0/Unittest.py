import unittest
from Interface import interface


class Test(unittest.TestCase):
    def setUp(self):
        self.c=interface("Co2.html", "Temperature.html")
        self.result=self.c.inputdata()

    def tearDown(self):
        pass

    def testint(self):
        self.assertEqual(self.result[0][0],1959)


if __name__=='__main__':
    unittest.main()

"""
.
----------------------------------------------------------------------
Ran 1 test in 0.042s

OK

"""
