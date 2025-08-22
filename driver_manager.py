from selenium import webdriver

class DriverManager:
    def __init__(self, name='chrome'):
        if name == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument('--no-sandbox')
            self.d = webdriver.Chrome(options=options)
        elif name == 'firefox':
            options = webdriver.FirefoxOptions()
            self.d = webdriver.Firefox(options=options)

driver = DriverManager().d