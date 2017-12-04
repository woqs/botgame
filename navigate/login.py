from selenium.webdriver.support.ui import Select

def login(driver, conf):
    loginButton = driver.find_element_by_id('loginBtn')
    loginButton.click()
    login = driver.find_element_by_id('usernameLogin')
    login.send_keys(conf['login'])
    pwd = driver.find_element_by_id('passwordLogin')
    pwd.send_keys(conf['password'])
    universes = Select(driver.find_element_by_id('serverLogin'))
    universes.select_by_visible_text(conf['univers'])
    loginButton = driver.find_element_by_id('loginSubmit')
    loginButton.click()
