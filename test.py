import time

import pytest

from Page.main_page import MainPage
from data.data_manager import data_manager

class TestOpenCart():

    @pytest.mark.parametrize('name,phone,password,re_password',data_manager.get_from_excel('test_opcart_demo','test_01_reg'))
    def test_01_reg(self,name,phone,password,re_password):
        main_page=MainPage()
        main_page.open_main_page()
        reg_page=main_page.goto_reg()
        reg_page.reg_by_phone(name,phone,password,re_password)
        reg_page.del_cookies()
        time.sleep(2)

    @pytest.mark.parametrize('phone,password',data_manager.get_from_excel('test_opcart_demo','test_02_log'))
    def test_02_log(self,phone,password):
        main_page = MainPage()
        main_page.open_main_page()
        login_page=main_page.goto_log()
        login_page.login_by_phone(phone,password)
        login_page.del_cookies()

if __name__=='__main__':
    pytest.main()

