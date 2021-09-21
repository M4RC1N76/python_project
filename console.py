import pdb
from models.city import City
from models.country import Country
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

# city_repository.delete_all()
# country_repository.delete_all()
country_1 = Country('Russia')
country_repository.save(country_1)
country_1.visited = True
country_repository.update(country_1)
results = country_repository.select_all()
for row in results:
    print(row.__dict__)

pdb.set_trace()

