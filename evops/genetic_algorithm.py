import random
import numpy as np
from math import radians, cos, sin, asin, sqrt
import pandas as pd
import os
def haversine(pt1,pt2):
    # output in miles
    lon1, lat1 = pt1
    lon2, lat2 = pt2
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 3956
    return c * r


class genetic_algorithm:

    def execute(latitudes, longitudes, traffic, pop_size, generations, possible_coords, budget, distance_limit=1000):
        neighbors = {i: () for i in range(len(latitudes))}
        distances = {}
        points = sorted([[latitudes[i], longitudes[i]]
                        for i in range(len(latitudes))])

        for point_1 in range(len(points)):
            for point_2 in range(point_1, len(points)):
                point1 = np.array(points[point_1])
                point2 = np.array(points[point_2])
                distance = abs(haversine(point1,point2))
                if distance <= distance_limit:
                    neighbors[point_1] = tuple(
                        list(neighbors[point_1]) + [point_2])
                    neighbors[point_2] = tuple(
                        list(neighbors[point_2]) + [point_1])
                    distances[tuple([point_1, point_2])] = distance
            

        class Agent:
            def __init__(self):
                self.config = []
                random.shuffle(possible_coords)
                for i in range(budget):
                    self.config.append(possible_coords[i])
                self.fitness = 0

            def __str__(self):
                return 'Fitness: ' + str(self.fitness)
            
        def profit(agent,distance_limit = 1000,simuls = 1000):
            # print("Call")
            '''
            setup adjacency matrix
            choose point
            average traffic between points is total traffic/num_neighbors
            move from point to point, recording profits
            assume 50kwh capacity
            '''
            profit = 0
            chargers = [points.index(charger) for charger in agent.config]
            # print("CHARGERS",chargers)

            visited = set()
            for _ in range(simuls):
                random_idx = random.randint(1,len(points)-1)
                queue = []
                # each node is [node,capacity in kwh,distance_travelled in coordinates]
                head = 0 
                queue.append([random_idx,50,0])
                # BFS until nodes_visited == depth
                # print(queue)
                while head < len(queue):
                    point1,capacity,distance = queue[head]
                
                    head += 1
                    new_states = neighbors[point1]
                    traffic_value = traffic[point1]/len(new_states)
                    # print(point1,new_states)
                    if distance < distance_limit:
                        for point2 in new_states[:3]:
                            if not(tuple(sorted([point1,point2])) in visited):
                                capacity -= distance*3
                                if point2 in chargers:
                                    # print("CHARGED")
                                    profit += (50-capacity)*0.34*traffic_value
                                    capacity = 50
                                # print(point1,point2)
                                # print(distance*3)
                                # convert distance to miles and
                                # ! https://www.fleetalliance.co.uk/driver-ev/mpg-to-kwh-electric-car-efficiency-explained/#:~:text=Most%20EVs%20will%20cover%20between,it%20will%20cost%20to%20run.
                                # change capacity by distance
                                # print(distance,distances[tuple(sorted([point1,point2]))])
                                new_state = [point2,capacity,distance + distances[tuple(sorted([point1,point2]))]]
                                queue.append(new_state)
                                # print(queue)
                                visited.add(tuple(sorted([point1,point2])))
                    else:
                        # print("DISTANCE PASS")
                        break
                # print(queue)
                # check if charger at new_state, if yes charge and count cost
                # if point2 in chargers:
                #     profit += (50-capacity)*0.34
                    # ! https://www.which.co.uk/reviews/new-and-used-cars/article/electric-car-charging-guide/how-much-does-it-cost-to-charge-an-electric-car-a8f4g1o7JzXj
                # ? possibly add regression or research to estimate traffic
            return profit/simuls/len(chargers)

        def generate_agents(population):
            return [Agent() for _ in range(population)]

        def fitness(agents):
            for agent in agents:
                agent.fitness = profit(agent)
                # print(agent)
            return agents

        def selection(agents):
            agents = sorted(
                agents, key=lambda agent: agent.fitness, reverse=True)
            # print('\n'.join(map(str, agents)))
            agents = agents[:int(0.2 * len(agents))]
            return agents

        def crossover(agents, pop_size):
            offspring = []
            for _ in range((pop_size - len(agents)) // 2):
                parent1 = random.choice(agents)
                parent2 = random.choice(agents)
                child1 = Agent()
                child2 = Agent()

                split = random.randint(0, budget)

                child1.config = parent1.config[:split] + parent2.config[split:]
                child1.config = parent2.config[:split] + parent1.config[split:]

                offspring.append(child1)
                offspring.append(child2)
            agents.extend(offspring)
            return agents

        def mutation(agents):
            for agent in agents:
                if random.uniform(0.0, 1.0) <= 0.1:
                    change_idx = random.randint(0, budget-1)
                    agent.config[change_idx] = random.choice(possible_coords)
            return agents

        agents = generate_agents(pop_size)
        agents = fitness(agents)
        for i in range(generations):
            print('Generation', str(i), ':')
            agents = selection(agents)
            # print(len(agents))
            agents = crossover(agents, pop_size)
            agents = mutation(agents)
            agents = fitness(agents)
            agents = sorted(
                agents, key=lambda agent: agent.fitness, reverse=True)
            # for agent in agents:
            #     print(agent)
            print(agents[0])
            # print(len(agents))
            # print(len(agents))

            # if any(agent.fitness > threshold for agent in agents):
            #     print('Threshold met at generation '+str(i)+' !')
            #     break

            if i % 5 == 0:
                os.system("cls")

        return agents[0]

# ga = genetic_algorithm
# agent = ga.execute(10000,1000,0.0001,possible_coords)
# agent.fitness
