from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
url='http://10.115.161.203/oaweb/oaconsole'
driver = webdriver.Ie()
driver.maximize_window()
driver.get(url)
#部门
# js="document.getElementById('unit').click()"
# driver.execute_script(js)
# time.sleep(5)
# #部门二级标题框
# table=driver.find_element_by_id('loginTreeDialog')
# #本部按钮
# js1="document.getElementsByClassName('x-tree-node-icon')[0].click()"
# driver.execute_script(js1)
# time.sleep(3)
# table.find_element_by_link_text('办公室').click()
driver.find_element_by_name('password').send_keys(1)
js="document.getElementsByClassName('btnLogin')[0].click()" #登录按钮
driver.execute_script(js)
time.sleep(30)
a=driver.find_element_by_xpath('/html/body/iframe')
driver.switch_to_frame(a)
driver.find_element_by_id('dbTotalNum').click()#工作台
time.sleep(3)
driver.switch_to_default_content()
driver.switch_to_frame(a)
time.sleep(3)
b=driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div[2]/iframe')
driver.switch_to_frame(b)
driver.find_element_by_id('groupBtn').click()
driver.find_elements_by_class_name('ico-group')[3].click()
# s=driver.find_element_by_id('groupTip')
# s.find_element_by_link_text('按时间分组').click()
# Select(s).select_by_index(0)
# time.sleep(2)
# Select(s).select_by_index(1)
#/html/body/div[5]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div[2]/iframe
#测试
