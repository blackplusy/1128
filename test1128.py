#coding=utf-8

#1.导入selenium库
from selenium import webdriver
#2.定义需要打开的浏览器
br=webdriver.Chrome()
#3.打开的页面
br.get("https://www.baidu.com")
#1.id定位
# br.find_element_by_id("kw").send_keys("爵迹2")
#2.name定位
# br.find_element_by_name("wd").send_keys("特朗普")
#3.class定位
# br.find_element_by_class_name("s_ipt").send_keys("LOL")
#4.tag定位
# br.find_element_by_tag_name("input").send_keys("123")
#5.通过link定位
# br.find_element_by_link_text("hao123").click()
#6.partial_link定位
# br.find_element_by_partial_link_text("闻").click()
#7.通过xpath定位
# br.find_element_by_xpath("//*[@id='kw']").send_keys("拜登")
#8.通过css定位
br.find_element_by_css_selector("#kw").send_keys("扣你齐瓦")