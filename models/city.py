class City:
    def __init__(self, name, visited = False, id = None):
        self.name = name
        self.visited = visited
        self.id = id

    def get_details(self):
        return f"{self.name} by {self.visited} is in {self.country.name}"
        # check the correctness of f string
