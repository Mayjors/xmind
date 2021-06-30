import time

import logging

import pyautogui
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

pyautogui.PAUSE = 0.5

# if __name__ == "__main__":
#     driver = webdriver.Chrome('chromedriver.exe')
#     driver.get('https://www.baidu.com/')
#     elem = driver.find_element_by_xpath('//*[@id="kw"]')
#     elem.send_keys("Jack Cui")
#     elem.send_keys(Keys.RETURN)


# if __name__ == "__main__":
#     driver = webdriver.Chrome("chromedriver.exe")
#     driver.get("https://www.python.org")
#     assert "Python" in driver.title
#     elem = driver.find_element_by_name("q")
#     elem.send_keys("pycon")
#     elem.send_keys(Keys.RETURN)
#     print(driver.page_source)

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class taobao():
    def __init__(self):

        self.browser = webdriver.Chrome('chromedriver.exe')
        # 最大化窗口
        self.browser.maximize_window()
        self.browser.implicitly_wait(5)
        self.domain = 'http://www.taobao.com'
        self.action_chains = ActionChains(self.browser)

    def login(self, username, password):
        while True:
            self.browser.get(self.domain)
            time.sleep(1)
            # 简化xpath
            # self.browser.find_element_by_class_name('h').click()
            # self.browser.find_element_by_id('fm-login-id').send_keys(username)
            # self.browser.find_element_by_id('fm-login-password').send_keys(password)
            self.browser.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()
            self.browser.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys(username)
            self.browser.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys(password)
            # driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys("tb054216_55")
            # driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys("qiufeng0852")
            time.sleep(1)

            try:
                # 出现验证码，华东验证
                slider = self.browser.find_element_by_xpath("//span[contains(@class, 'btn_slide')]")
                if slider.is_displayed():
                    # 拖拽滑块
                    self.action_chains.drag_and_drop_by_offset(slider, 258, 0).perform()
                    time.sleep(0.5)
                    # 释放滑块，相当于点击拖拽之后的释放鼠标
                    self.action_chains.release().perform()
            except (NoSuchElementException, WebDriverException):
                logger.info('未出现登录验证码')

            # xpath简化点击登陆按钮
            # 会xpath可以简化点击登陆按钮，但都无法登录，需要使用 pyautogui 完成点击事件
            # self.browser.find_element_by_class_name('password-login').click()
            # self.browser.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()

            # 图片地址
            coords = pyautogui.locateOnScreen('1.png')
            x, y = pyautogui.center(coords)
            pyautogui.leftClick(x, y)

            nickname = self.get_nickname()
            if nickname:
                logger.info('登陆成功，昵称为：' + nickname)
                break
            logger.debug('登陆出错，5s后继续登陆')
            time.sleep(5)


    def get_nickname(self):
        self.browser.get(self.domain)
        time.sleep(0.5)
        try:
            return self.browser.find_element_by_name('site_nav_user').text
        except NoSuchElementException:
            return ''


import cv2

if __name__ == '__main__':
    # 填入自己的用户名，密码
    username = '13129586469'
    password = 'qiufeng0852'
    # tb = taobao()
    # tb.login(username, password)

    coords = pyautogui.locateOnScreen('1.png',confidence=0.5)
    x, y = pyautogui.center(coords)

