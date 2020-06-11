from .BasePage import *
from selenium.webdriver.common.by import By


# 创建登录页面的类
class LoginPage(Page):
    u_para = "/web/login.php"
    # 设置定位器
    username_loc = (By.NAME, "user_name")
    password_loc = (By.NAME, "password")
    submit_loc = (By.XPATH, "//button[@class='btn btn-primary btn-block']")

    # 定义username输入框元素的定位 、输入方法
    def type_username(self, username):
        self.find_element(*self.username_loc).clear() # 调用find_element()方法
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def type_submit(self):
        self.find_element(*self.submit_loc).click()

    # 封装登录功能模块
    def login_action(self, username,password):
        self.open()
        self.type_username(username)
        self.type_password(password)
        self.type_submit()

    # 设置登陆成功和失败的定位器
    loginPass_loc = (By.LINK_TEXT, "修改密码")
    loginFail_loc = (By.NAME, "user_name")

    # 返回实际定位的元素
    def type_loginPass_hint(self):
        return self.find_element(*self.loginPass_loc).text

    def type_loginFail_hint(self):
        return self.find_element(*self.loginFail_loc).text