import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    '''初始化的一部分，在每一个测试方法被执行前都执行一遍'''
    def setUp(self):
        self.driver = webdriver.Chrome()

    '''测试方法始终以test开头'''
    def test_search_in_python_org(self):
        driver = self.driver #本地引用
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        # assert 判断是否包含指定字符串
        assert "No results found." not in driver.page_source

    '''每一个测试方法执行之后被执行，勇于做清扫工作，比如关闭浏览器。'''
    def tearDown(self):
        self.driver.close()#quit 关闭整个浏览器，close关闭一个标签页，如果只打开了一个标签页，则等同

if __name__ == "__main__":
    unittest.main()