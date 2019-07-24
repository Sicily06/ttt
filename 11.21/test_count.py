'''测试集例子 TestSuit;引用了calculator文件中的方法'''
from calculator import Count
import unittest

class TestCount(unittest.TestCase):

    def setUp(self):
        print("test start!")

    def test_add(self):
        j= Count(2,3)
        self.assertEqual(j.add(),5)

    def test_add2(self):
        j = Count(41,76)
        self.assertEqual(j.add(),117)

    def tearDown(self):
        print("test end!")

if __name__== '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestCount("test_add"))
    suite.addTest(TestCount("test_add2"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)

