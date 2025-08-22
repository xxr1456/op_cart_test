from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Base.driver_manager import  driver


class BasePage():
    driver.implicitly_wait(10)  # 隐式等待10秒
    #打开获取的指定网页
    def open(self,url):
        driver.get(url)

    #定位元素
    def find_element(self,type,value):
        if type=='id':
            el = driver.find_element(By.ID,value)
        elif type=='name':
            el = driver.find_element(By.NAME,value)
        elif type=='tag':
            el = driver.find_element(By.TAG_NAME,value)
        elif type=='class':
            el = driver.find_element(By.CLASS_NAME,value)
        elif type=='xpath':
            el = driver.find_element(By.XPATH,value)
        elif type=='css':
            el = driver.find_element(By.CSS_SELECTOR,value)
        elif type=='link':
            el = driver.find_element(By.LINK_TEXT,value)
        elif type=='p_link':
            el = driver.find_element(By.PARTIAL_LINK_TEXT ,value)
        else:
            print('输入的定位方式错误')
        return el

    #点击目标元素
    def click_element(self, type, value):
        self.find_element(type,value).click()

    #向目标元素输入文本
    def input_to_element(self,type,value,text):
        self.find_element(type,value).send_keys(text)
    #鼠标悬停于指定位置(pause(2)停2s)
    def move_mouse_to_element(self,type,value):
        ActionChains(driver).move_to_element(self.find_element(type,value)).pause(2).perform()
    #切换框架
    def switch_to_frame(self,id_name_or_element):
        driver.switch_to.frame(id_name_or_element)
    #切换窗口
    def switch_to_windows(self,title,):
        handles = driver.window_handles
        for handle in handles:
            driver.switch_to.window(handle)
            if driver.title == title:
                break
    #删除cookies
    def del_cookies(self):
        driver.delete_all_cookies()
