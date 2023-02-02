
import unittest
class unittest1(unittest.TestCase):
    def setUp(self) -> None:
        print("这是setup下面的打印内容")
    def test_1(self):
        print("进行登录")
    def tearDown(self) -> None:
        print("这是tearDown下面打印的内容")


suite = unittest.TestSuite()
suite.addTest(unittest1("test_1"))
runner = unittest.TextTestRunner()
runner.run(suite)