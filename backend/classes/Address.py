class Address:
    def __init__(self, street, city, state, zip):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.inhabitants = []

    def addInhabitant(self, person):
        self.inhabitants.append(person)
