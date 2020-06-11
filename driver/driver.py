from selenium import webdriver


# 定义浏览器驱动
def browser():
    driver = webdriver.Chrome()
    return driver


if __name__ == '__main__':
    browser()
