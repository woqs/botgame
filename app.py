from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import yaml

from navigate import login
from empire_data import getPlanetList

if __name__ == "__main__":
    with open("conf.yml", 'r') as ymlfile:
        conf = yaml.load(ymlfile)

    driver = webdriver.Firefox()
    # double get to get rid of the ads
    driver.get(conf['url'])
    driver.get(conf['url'])

    login(driver, conf)
    planets = getPlanetList(driver)

    #driver.close()
