import unittest
import time
from selenium import webdriver
# import geetest
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image


class LoferLogin(unittest.TestCase):
    """A sample test class to show how page object works"""
    def setUp(self):
    	self.driver = webdriver.Chrome()
    	self.driver.get("http://www.lofter.com/")

    def test_login(self):
    	driver = self.driver
    	iframe_id = driver.find_element_by_xpath("//div[@id='login-URS-wrap']/iframe").get_attribute("id")
    	iframe = driver.find_element_by_id(iframe_id)
    	driver.switch_to.frame(iframe)
    	driver.find_element_by_name('email').clear()
    	driver.find_element_by_name('email').send_keys("452782353@163.com")
    	driver.find_element_by_name('password').clear()
    	driver.find_element_by_name('password').send_keys("equinox_1994")
    	element_span = driver.find_element_by_class_name('yidun_slider')
    	img_name = time.strftime("%y%m%d%H%M%S")
    	# element_span.location_once_scrolled_into_view  Returns the top lefthand corner location on the screen, or None if the element is not visible.
    	# 滑块验证
    	img_addr = 'D:\\code\\python\\img\\' + img_name +'.png'
    	driver.save_screenshot(img_addr)
    	element_img = driver.find_element_by_class_name('yidun_bg-img')
    	left = element_img.location_once_scrolled_into_view['x']
    	top = element_img.location_once_scrolled_into_view['y']
    	# 可以用size取宽高
    	right = left+220
    	bottom = top+110
    	action=ActionChains(driver)
    	action.click_and_hold(element_span).perform()
    	i=0
    	while i<22:
    		action.reset_actions()
    		action.move_by_offset(10,0).perform()
    		driver.get_screenshot_as_file('D:\\code\\python\\img\\' + img_name + '-screenshot'+ str(i) +'.png')
    		im = Image.open(img_addr)
    		im = im.crop((left, top, right, bottom))
    		im.save('D:\\code\\python\\img\\' + img_name + '-' + str(i) +'.png')
    		i+=1
    		time.sleep(2)
    	
    	# action.drag_and_drop_by_offset(element_span,0,0).perform()
    	driver.find_element_by_id('dologin').click()



    def tearDown(self):
    	time.sleep(2)
    	# self.driver.close()


if __name__ == '__main__':
	unittest.main()