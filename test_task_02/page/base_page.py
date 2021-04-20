import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    """
    把页面重复的步骤抽离出来，封装，比如driver 的实例化
    """
    # 没有参数传入， 会取默认None ,如果有参数传入,会取传入的参数
    def __init__(self, _base_driver:WebDriver=None):


        if _base_driver == None:
            # 实例化 driver
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            # 访问扫码登录页面
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
            with open("cookie.yaml", encoding="UTF-8") as f:
                yaml_data = yaml.safe_load(f)
                print(yaml_data)
                for cookie in yaml_data:
                    self.driver.add_cookie(cookie)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            # 隐式等待，每一次调用find 方法，就会轮询查找元素是否存在
            self.driver.implicitly_wait(3)

        else:
            self.driver = _base_driver


