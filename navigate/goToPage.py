def goTo(driver, page):
    driver.find_element_by_xpath("//ul[@id='menuTable']/li/a[contains(@href,'page=%s')]" % page).click()

def goToOverview(driver):
    goTo(driver, 'overview')

def goToResources(driver):
    goTo(driver, 'resources')

def goToStation(driver):
    goTo(driver, 'station')

def goToResearch(driver):
    goTo(driver, 'research')

def goToShipyard(driver):
    goTo(driver, 'shipyard')

def goToDefense(driver):
    goTo(driver, 'defense')

def goToFleet(driver):
    goTo(driver, 'fleet1')

def goToGalaxy(driver):
    goTo(driver, 'galaxy')

def goToPlanet(driver, planetId):
    driver.find_element_by_xpath("//div[@id='%s']" % planetId).click()
