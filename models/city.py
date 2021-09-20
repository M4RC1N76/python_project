class City:
    def __init__(self, name, country, visited = False, id = None):
        self.name = name
        self.visited = visited
        self.id = id
        self.country = country

    # def get_details(self):
    #     return f"{self.name} is in {self.country.name}"
        # check the correctness of f string
