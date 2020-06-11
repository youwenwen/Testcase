from time import sleep


# 创建页面基础类
class Page():
    # 初始化
    def __init__(self, driver):
        self.base_url = "https://fpadmin-t.vova.com.hk"
        self.driver = driver
        self.timeout = 10

    def _open(self, u_para):
        url = self.base_url + u_para
        print("Test Page is: %s" % url)
        self.driver.maximize_window()
        self.driver.get(url)
        sleep(2)
        assert self.driver.current_url == url, "Did not land on %s" % url

    def open(self):
        self._open(self.u_para)

    # 封装元素定位的方法
    def find_element(self, *loc):
        return self.driver.find_element(*loc)
