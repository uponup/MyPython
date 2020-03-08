# selenium是一个自动化测试工具，支持各种主流的浏览器，遇到Python之后就变成了爬虫利器

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

input = driver.find_element_by_class_name('s_ipt')
input.send_keys("虎扑nba")

button = driver.find_element_by_css_selector('#su')
button.click()


# selenium提供了很多方法帮我们去获取界面中的元素：

# find_element_by_id
# find_element_by_name
# find_element_by_xpath
# find_element_by_link_text
# find_element_by_partial_link_text
# find_element_by_tag_name
# find_element_by_class_name
# find_element_by_css_selector

# 想要获取多个值的时候，可以这样：

# find_elements_by_name
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector


# 当然，我们拿到Chrome浏览器的对象了，很多东西自然也就可以直接获取到了：

# 获取当前url
driver.current_url

# 获取cookies
driver.get_cookie

# 获取源代码
driver.page_source

# 获取文本的值
input.text

