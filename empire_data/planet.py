from navigate import login, goToPage

class Planet():
    fleet = []
    resources = []
    def __init__(self, id, name, coordinates):
        self.id = id
        self.shortId = id.split('-')[1]
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
    return populatePlanetData(driver, planets)

def populatePlanetData(driver, planets):
    populatedPlanets = []
    for planet in planets:
        goToPage.goToPlanet(driver, planet.id)
        goToPage.goToDefense(driver)

    return planets
