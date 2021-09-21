class Country:
    def __init__(self, name, visited = False, id = None):
        self.name = name
        self.visited = visited
        self.cities = []
        self.id = id
