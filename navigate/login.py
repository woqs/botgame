from selenium.webdriver.support.ui import Select

def login(driver, conf):
    driver.find_element_by_id('loginBtn').click()
    driver.find_element_by_id('usernameLogin').send_keys(conf['login'])
    driver.find_element_by_id('passwordLogin').send_keys(conf['password'])
    Select(driver.find_element_by_id('serverLogin')).select_by_visible_text(conf['univers'])
    driver.find_element_by_id('loginSubmit').click()
