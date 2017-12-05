from navigate import goToPage

def populateResources(driver, planet):
    goToPage.goToResources(driver)
    planet.resources['metal'] = driver.find_element_by_id('resources_metal').text
    planet.resources['crystal'] = driver.find_element_by_id('resources_crystal').text
    planet.resources['deuterium'] = driver.find_element_by_id('resources_deuterium').text
    planet.resources['energy'] = driver.find_element_by_id('resources_energy').text
    planet.production['metal_factory'] = getFactoryLevel(driver, 'button1')
    planet.production['crystal_factory'] = getFactoryLevel(driver, 'button2')
    planet.production['deuterium_factory'] = getFactoryLevel(driver, 'button3')
    planet.production['energy_factory'] = getFactoryLevel(driver, 'button4')
    planet.production['fusion_factory'] = getFactoryLevel(driver, 'button5')
    planet.production['satelite_factory'] = getFactoryLevel(driver, 'button6')
    planet.production['metal_stock'] = getFactoryLevel(driver, 'button7')
    planet.production['crystal_stock'] = getFactoryLevel(driver, 'button8')
    planet.production['deuterium_stock'] = getFactoryLevel(driver, 'button9')

def getFactoryLevel(driver, id):
    return driver.find_element_by_xpath("//li[@id='%s']/*//span[@class='level']" % id).text

def populateStation(driver, planet):
    goToPage.goToStation(driver)

def populateShipyard(driver, planet):
    goToPage.goToShipyard(driver)

def populateDefense(driver, planet):
    goToPage.goToDefense(driver)

def populateFleet(driver, planet):
    goToPage.goToFleet(driver)

def populateResearch(driver):
    goToPage.goToResearch(driver)
