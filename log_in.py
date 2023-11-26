import schedule
import time
import subprocess

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
 
def login():
    # 打开浏览器，option的作用是隐藏浏览器窗口（静默执行），去掉option以后会弹出浏览器窗口
    option = webdriver.EdgeOptions()                                                    #需要上网下载对应版本的edgedriver并添加环境变量
    option.add_argument('headless')
    browser = webdriver.Edge(options=option)
 
    # 打开登录网址,给它5s时间加载
    browser.get('http://10.9.1.3/')
    sleep(2)
 
    # 如果是注销页，说明已登陆过，直接退了
    if browser.title == "注销页":
        browser.quit()  # 退出浏览器
        print("已经登录过了")
 
    # 如果是上网登录页，说明未登录，速速登录
    elif browser.title == "上网登录页":
        elem = browser.find_element(By.XPATH,
                                    '//*[@id="edit_body"]/div[2]/div[12]/select')  
    # 这里的XPATH就是前面用元素审查复制得到的Xpath，用于定位元素
        sleep(0.5)
        browser.execute_script("arguments[0].selectedIndex = 3;",elem)         #选择运营商：移动index = 2，电信3，联通4
        sleep(0.5)
        elem =browser.find_element(By.XPATH, '//*[@id="edit_body"]/div[2]/div[12]/form/input[3]')             
        elem.send_keys('123456')                                              # 这里输入用户名（即学号）
        sleep(0.5)
        elem = browser.find_element(By.XPATH, '//*[@id="edit_body"]/div[2]/div[12]/form/input[4]')
        elem.clear()
        sleep(0.5)
        elem.send_keys('123456')                                               # 这里输入密码
        sleep(0.5)
        elem = browser.find_element(By.XPATH, '//*[@id="edit_body"]/div[2]/div[12]/form/input[2]')
        sleep(0.5)
        browser.execute_script("arguments[0].click();", elem)  # 这里不直接用.click()是因为这里报错，报错内容是有阻挡，所以换了种方法进行click
        browser.quit()  # 退出浏览器




subprocess.Popen(["pythonw","gui_program.py"])                           #后台运行时隐藏程序
schedule.every(60).minutes.do(login)                                     #每一小时自动登录一次

while True:
    schedule.run_pending()
    time.sleep(2)