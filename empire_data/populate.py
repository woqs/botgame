from navigate import goToPage

def populateResources(driver, planet):
    goToPage.goToResources(driver)
    planet.resources['metal'] = driver.find_element_by_id('resources_metal').text
    planet.resources['crystal'] = driver.find_element_by_id('resources_crystal').text
    planet.resources['deuterium'] = driver.find_element_by_id('resources_deuterium').text
    planet.resources['energy'] = driver.find_element_by_id('resources_energy').text
    planet.production['metal_factory'] = __getLevel(driver, 'button1')
    planet.production['crystal_factory'] = __getLevel(driver, 'button2')
    planet.production['deuterium_factory'] = __getLevel(driver, 'button3')
    planet.production['energy_factory'] = __getLevel(driver, 'button4')
    planet.production['fusion_factory'] = __getLevel(driver, 'button5')
    planet.production['satelite_factory'] = __getLevel(driver, 'button6')
    planet.production['metal_stock'] = __getLevel(driver, 'button7')
    planet.production['crystal_stock'] = __getLevel(driver, 'button8')
    planet.production['deuterium_stock'] = __getLevel(driver, 'button9')
    driver.find_element_by_id('slot01').click()
    hours = driver.find_elements_by_xpath("//tr[@class='summary alt']/td[@class='undermark']/span[@class='tooltipCustom']")
    planet.resources['metal_hour'] = hours[0].text
    planet.resources['crystal_hour'] = hours[1].text
    planet.resources['deuterium_hour'] = hours[2].text

def populateStation(driver, planet):
    goToPage.goToStation(driver)
    planet.station['robots'] = __getLevel(driver, 'button0')
    planet.station['shipyard'] = __getLevel(driver, 'button1')
    planet.station['research'] = __getLevel(driver, 'button2')
    planet.station['resupply'] = __getLevel(driver, 'button3')
    planet.station['missiles'] = __getLevel(driver, 'button4')
    planet.station['nanites'] = __getLevel(driver, 'button5')
    planet.station['terraform'] = __getLevel(driver, 'button6')
    planet.station['dock'] = __getLevel(driver, 'button7')

def populateShipyard(driver, planet):
    goToPage.goToShipyard(driver)
    planet.fleet['light_f'] = __getShipNumber(driver, 'military', 'button1')
    planet.fleet['heavy_f'] = __getShipNumber(driver, 'military', 'button2')
    planet.fleet['cruiser'] = __getShipNumber(driver, 'military', 'button3')
    planet.fleet['battle_ship'] = __getShipNumber(driver, 'military', 'button4')
    planet.fleet['tracker'] = __getShipNumber(driver, 'military', 'button5')
    planet.fleet['bombarder'] = __getShipNumber(driver, 'military', 'button6')
    planet.fleet['destructor'] = __getShipNumber(driver, 'military', 'button7')
    planet.fleet['deathstar'] = __getShipNumber(driver, 'military', 'button8')
    planet.fleet['light_transport'] = __getShipNumber(driver, 'civil', 'button1')
    planet.fleet['heavy_transport'] = __getShipNumber(driver, 'civil', 'button2')
    planet.fleet['colonisation'] = __getShipNumber(driver, 'civil', 'button3')
    planet.fleet['recycler'] = __getShipNumber(driver, 'civil', 'button4')
    planet.fleet['spy'] = __getShipNumber(driver, 'civil', 'button5')
    planet.fleet['sun_satelite'] = __getShipNumber(driver, 'civil', 'button6')

def populateDefense(driver, planet):
    goToPage.goToDefense(driver)
    planet.defense['missile_launcher'] = __getLevel(driver, 'defense1')
    planet.defense['light_laser'] = __getLevel(driver, 'defense2')
    planet.defense['heavy_laser'] = __getLevel(driver, 'defense3')
    planet.defense['gauss'] = __getLevel(driver, 'defense4')
    planet.defense['ion'] = __getLevel(driver, 'defense5')
    planet.defense['plasma'] = __getLevel(driver, 'defense6')
    planet.defense['small_shield'] = __getLevel(driver, 'defense7')
    planet.defense['big_shield'] = __getLevel(driver, 'defense8')
    planet.defense['interception_missile'] = __getLevel(driver, 'defense9')
    planet.defense['interplanetary_missile'] = __getLevel(driver, 'defense10')

def populateFleet(driver, planet):
    goToPage.goToFleet(driver)

def populateResearch(driver):
    goToPage.goToResearch(driver)

def __getLevel(driver, id):
    return driver.find_element_by_xpath("//li[@id='%s']/*//span[@class='level']" % id).text

def __getShipNumber(driver, type, id):
    return driver.find_element_by_xpath("//ul[@id='{!s}']/li[@id='{!s}']/*//span[@class='level']".format(type, id)).text
