class Country:
    def __init__(self, name, visited = False, id = None):
        self.name = name
        self.visited = visited
        self.cities = [] # it was self.countries by mistake
        self.id = id
