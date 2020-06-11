import time
import unittest
from BSTestRunner import BSTestRunner

report_dir = "./TestReport/"
test_dir = "./TestCase/"

print("Start runnig TestCase...")
discover = unittest.defaultTestLoader.discover(test_dir,pattern="test_login.py")    # 设定目录，及其匹配的规则
now = time.strftime("%y-%m-%d %H_%M_%S")
report_name = report_dir+now+"_result.html"

print("Start writting report...")
# Python3运行前记得把BSTestRunner.py 120行 'unicode'-->'str' 以免报错
with open(report_name,'wb') as f:
    runner = BSTestRunner(stream=f,title="Test Report",description="FF_test's login test")
    runner.run(discover)
f.close()

print("Test is end !")
