from access_data import get_possible_spots
from input_data import get_data
from genetic_algorithm import genetic_algorithm

get_data("Birmingham")
possible,latitudes,longitudes = get_possible_spots()
ga = genetic_algorithm
agent = ga.execute(latitudes,longitudes,10000,1000,100,possible,10)
# Population size, generations,threshold,possible_coordinates,budget
print(agent.fitness,agent.config)