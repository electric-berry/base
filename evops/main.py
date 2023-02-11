from access_data import get_possible_spots
from input_data import get_data
from genetic_algorithm import genetic_algorithm
import csv
import os

#TODO:
# 1. Fix (?) genetic algorithm (doneish)
# 2. Change csv output format to include latitude and longitude column names 
# 3. Add more args to get_csv()

def get_csv(location):
    print("Getting Data...")
    try:
        get_data(location)
    except:
        print("Error when collecting data.")
        print("Processing existing CSV file...")
    print("Done!")
    print("Processing Data...")
    possible,latitudes,longitudes = get_possible_spots() # ! possible,latitudes,longitudes = get_possible_spots() ValueError: too many values to unpack (expected 3)
    print("Done!")
    ga = genetic_algorithm
    print("Running Genetic Algorithm...")
    agent = ga.execute(latitudes,longitudes,100,1000,100,possible,800)
    print("Done!")
    # Population size, generations,threshold,possible_coordinates,budget
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