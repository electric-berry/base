from access_data import get_possible_spots
from input_data import get_data
from genetic_algorithm import genetic_algorithm
import csv
import os

#TODO:
# 1. Fix (?) genetic algorithm (doneish)
# 2. Change csv output format to include latitude and longitude column names 
# 3. Add more args to get_csv()

def get_csv(location,pop_size,generations,budget):
    print("Getting Data...")
    try:
        get_data(location)
    except:
        print("Error when collecting data.")
        print("Processing existing CSV file...")
    print("Done!")
    print("Processing Data...")
    possible,latitudes,longitudes,traffics = get_possible_spots()
    print(traffics)
    print("Done!")
    ga = genetic_algorithm
    print("Running Genetic Algorithm...")
    agent = ga.execute(latitudes,longitudes,traffics,pop_size,generations,possible,budget)
    print("Done!")
    # ! lats, longs, pop_size, generations, possible_coordinates, budget
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

if __name__ == "__main__":
    get_csv("Birmingham",1000,200,100)
    