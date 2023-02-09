from access_data import get_possible_spots
from input_data import get_data
from genetic_algorithm import genetic_algorithm
import csv
import os

print("Getting Data...")
try:
    get_data("Birmingham")
except:
    print("Error when collecting data.")
    print("Processing existing CSV file...")
print("Done!")
print("Processing Data...")
possible,latitudes,longitudes = get_possible_spots()
print("Done!")
ga = genetic_algorithm
print("Running Genetic Algorithm...")
agent = ga.execute(latitudes,longitudes,1000,1000,possible,100)
print("Done!")
# lats, longi, Population size, generations,threshold,possible_coordinates,budget
# print(agent.fitness,agent.config)
optimal = agent.config
os.system("cls")
print("Top Fitness:",str(agent.fitness))
print("Writing to CSV...")
with open('optimal.csv', 'w') as fh:
    spamwriter = csv.writer(fh)
    for t in agent.config:
        spamwriter.writerow(t)
print("Done!")