class Planet():
    def __init__(self, id, name, coordinates):
        self.id = id
        self.name = name
        self.coordinates = coordinates

def getPlanetList(driver):
    planets = []
    planetsId = []
    for planetDiv in driver.find_elements_by_xpath("//div[@id='planetList']//div"):
        planetsId.append(planetDiv.get_attribute("id"))
    for planId in planetsId:
        planets.append(Planet(
            planId,
            driver.find_element_by_xpath("//div[@id='%s']/*/span[@class='planet-name ']" %planId).text,
            driver.find_element_by_xpath("//div[@id='%s']/*/span[@class='planet-koords ']" %planId).text
        ))
    return planets
