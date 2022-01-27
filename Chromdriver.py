from selenium import webdriver
driver = webdriver.Chrome('./chromedriver.exe')

target_url = "http://naver.com/"

driver.get(target_url)

search_box = driver.find_element_by_name('query')

search_box.send_keys('Python')

search_box.submit()