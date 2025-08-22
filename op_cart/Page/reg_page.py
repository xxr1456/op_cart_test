from Page.base_page import BasePage
from Page.reg_success import RegSuccessPage


class RegPage(BasePage):
    url='http://192.168.5.132/opencart'

    phone_num_reg = {'type': 'xpath', 'value': '//*[@id="tab-mobile"]/a'}
    email_reg = {'type': 'xpath', 'value': '//*[@id="tab-email"]/a'}
    name = {'type': 'xpath', 'value': '//*[@id="tab-mobile"]/a'}
    phon_num = {'type': 'xpath', 'value': '//*[@id="input-telephone"]'}
    email = {'type': 'xpath', 'value': '//*[@id="input-email"]'}
    password = {'type': 'xpath', 'value': '//*[@id="input-password"]'}
    confirm_password = {'type': 'xpath', 'value': '//*[@id="input-confirm"]'}
    subscribe_to_emails = {'type': 'xpath', 'value': '//*[@id="tab-general"]/form/fieldset[3]/div/label'}
    privacy_policy = {'type': 'xpath', 'value': '//*[@id="tab-general"]/form/div[1]/label'}

    #打开注册页面
    def vip_reg(self):
        self.open(self.url)



#使用手机号注册
    def reg_by_phone(self,name,phone,password,confirm_password):
        self.click_element(self.phone_num_reg['type'],self.phone_num_reg['value'])
        self.input_to_element(self.name['type'],self.name['value'],name)
        self.input_to_element(self.phon_num['type'],self.phon_num['value'],phone)
        self.input_to_element(self.password['type'],self.password['value'],password)
        self.input_to_element(self.confirm_password['type'],self.confirm_password['value'],confirm_password)
        self.click_element(self.subscribe_to_emails['type'],self.subscribe_to_emails['value'])
        self.click_element(self.privacy_policy['type'],self.privacy_policy['value'])
        return RegSuccessPage
#使用email注册
    def reg_by_email(self,name,email,password,confirm_password):
        self.click_element(self.email_reg['type'],self.email_reg['value'])
        self.input_to_element(self.name['type'],self.name['value'],name)
        self.input_to_element(self.email['type'], self.email['value'], email)
        self.input_to_element(self.password['type'],self.password['value'],password)
        self.input_to_element(self.confirm_password['type'],self.confirm_password['value'],confirm_password)
        self.click_element(self.subscribe_to_emails['type'],self.subscribe_to_emails['value'])
        self.click_element(self.privacy_policy['type'],self.privacy_policy['value'])
        return RegSuccessPage



