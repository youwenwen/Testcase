from selenium import webdriver
import os


def insert_img(driver, filename):
    # 获取当前脚本所在目录的绝对路径
    func_path = os.path.dirname(__file__)
    print(func_path)
    # 获取上一层目录
    base_dir = os.path.dirname(func_path)
    print(base_dir)
    base_dir = str(base_dir)  # 已字符串方式处理
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split("/website")[0]  # 获取根目录
    filepath = base + "/website/TestReport/screenshot/" + filename
    driver.get_screenshot_as_file(filepath)  # 保存截图文件到指定的路径


# 内部调试
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://baidu.com")
    insert_img(driver, "111.png")
    driver.quit()