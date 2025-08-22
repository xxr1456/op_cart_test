from Page.base_page import BasePage


class LoginPage(BasePage):
    url='http://192.168.5.132/opencart/index.php?route=account/login'
    phone={'type':'xpath','value':'//*[@id="input-telephone"]'}
    email={'type':'xpath','value':'//*[@id="input-email"]'}
    password={'type':'xpath','value':'//*[@id="input-password"]'}
    forget_passwd={'type':'xpath','value':'//*[@id="content"]/div/form/div[3]/a[1]'}
    user_reg={'type':'xpath','value':'//*[@id="content"]/div/form/div[3]/a[2]'}
    login_button={'type':'xpath','value':'//*[@id="content"]/div/form/input'}
    #代开登录页面
    def login(self,url):
        self.open(url)
#使用手机号登录
    def login_by_phone(self,phone,password):
        self.input_to_element(self.phone['type'],self.phone['value'],phone)
        self.input_to_element(self.password['type'],self.password['value'],password)
        self.click_element(self.login_button['type'],self.login_button['value'])

#使用email登录
    def login_by_email(self,email,password):
        self.input_to_element(self.email['type'],self.email['value'],email)
        self.input_to_element(self.password['type'],self.password['value'],password)
        self.click_element(self.login_button['type'],self.login_button['value'])