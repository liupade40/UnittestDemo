from selenium import webdriver
import unittest
import config
from config.config import read_ini


class TestBase(unittest.TestCase):
    browerName = ''
    url = ''
    @classmethod
    def setUpClass(cls) -> None:
        cf = read_ini()
        cls.browerName = cf.get('browserType','browerName')
        cls.url = cf.get('testServer', 'URL')
        print(cls.browerName)
    def setUp(self):
        """chromedriver.exe 需要放在python.exe的根目录下面"""
        if  self.browerName == 'Chrome':
            self.driver = webdriver.Chrome()  # 驱动浏览器
        else:
            self.driver = webdriver.Firefox()  # 驱动浏览器
        self.driver.implicitly_wait(10)  # 设置隐式等待
        self.driver.maximize_window()  # 最大化浏览器
    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

if __name__ == '__main__':
    unittest.main()