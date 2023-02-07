from access_data import get_possible_spots
from input_data import get_data
from genetic_algorithm import genetic_algorithm

print("Getting Data...")
get_data("Birmingham")
print("Done!")
print("Processing Data...")
possible,latitudes,longitudes = get_possible_spots()
print("Done!")
ga = genetic_algorithm
print("Running Genetic Algorithm...")
agent = ga.execute(latitudes,longitudes,100,1000,100,possible,10)
print("Done!")
# Population size, generations,threshold,possible_coordinates,budget
print(agent.fitness,agent.config)