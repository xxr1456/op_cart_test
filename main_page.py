from Page.base_page import BasePage
from Page.reg_page import RegPage
from Page.login_page import LoginPage

class MainPage(BasePage):
     url = 'http://192.168.5.132/opencart/'

     def open_main_page(self):
         self.open(self.url)
    #VIP相关
     vip_center = {'type': 'xpath','value':'//*[@id="top-links"]/ul/li[2]/a/span[1]'}
     vip_reg = {'type': 'xpath','value':'//*[@id="top-links"]/ul/li[2]/ul/li[1]/a'}
     vip_log = {'type': 'xpath','value':'//*[@id="top-links"]/ul/li[2]/ul/li[2]/a'}
#搜索相关
     search_input={'type': 'name','value':'search'}
     search_button={'type': 'xpath','value':'//*[@id="search"]/button'}


#点击会员注册
     def goto_reg(self):
         self.move_mouse_to_element(self.vip_center['type'],self.vip_center['value'])

         self.click_element(self.vip_reg['type'],self.vip_reg['value'])
         return RegPage()
#点击会员登录
     def goto_log(self):
         self.move_mouse_to_element(self.vip_center['type'],self.vip_center['value'])
         self.click_element(self.vip_log['type'],self.vip_log['value'])
         return LoginPage()
#搜索
     def sear(self):
         self.input_to_element(self.search_input['type'],self.search_input['value'])
         self.click_element(self.search_button['type'],self.search_button['value'])
