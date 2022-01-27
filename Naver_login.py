from selenium import webdriver
driver = webdriver.Chrome('./chromedriver.exe')

target_url = "http://nid.naver.com/nidlogin.login"

driver.get(target_url)

driver.find_element_by_name('id').send_keys('kyy804')

driver.find_element_by_name('pw').send_keys('wlsqkd232!')

driver.find_element_by_class_name('btn_global').click()