import random
import numpy as np
from IPython.display import clear_output

def sigmoid(x):
    return 1/(1+np.exp(-x))


class genetic_algorithm:
        
    def execute(pop_size,generations,threshold,possible_coords,budget):
        class Agent:
            def __init__(self):
                self.config = []
                random.shuffle(possible_coords)
                for i in range(budget):
                    self.config.append(possible_coords[i])
                self.fitness = 0
            def __str__(self):
                    return 'Loss: ' + str(self.fitness[0])
        
                
        def generate_agents(population):
            return [Agent() for _ in range(population)]
        
        def fitness(agents):
            for agent in agents:
                fitness = 0
                agent.fitness = fitness
            return agents
        
        def selection(agents):
            agents = sorted(agents, key=lambda agent: agent.fitness, reverse=False)
            # print('\n'.join(map(str, agents)))
            agents = agents[:int(0.2 * len(agents))]
            return agents
        
        def unflatten(flattened,shapes):
            newarray = []
            index = 0
            for shape in shapes:
                size = np.product(shape)
                newarray.append(flattened[index : index + size].reshape(shape))
                index += size
            return newarray
        
        def crossover(agents,network,pop_size):
            offspring = []
            for _ in range((pop_size - len(agents)) // 2):
                parent1 = random.choice(agents)
                parent2 = random.choice(agents)
                child1 = Agent()
                child2 = Agent()
                
                split = random.randint(0,budget)

                child1.config = parent1.config[:split] + parent2.config[split:]
                child1.config = parent2.config[:split] + parent1.config[split:]
                
                offspring.append(child1)
                offspring.append(child2)
            agents.extend(offspring)
            return agents
        
        def mutation(agents):
            for agent in agents:
                if random.uniform(0.0, 1.0) <= 0.1:
                    weights = agent.neural_network.weights
                    shapes = [a.shape for a in weights]

                    flattened = np.concatenate([a.flatten() for a in weights])
                    randint = random.randint(0,len(flattened)-1)
                    flattened[randint] = np.random.randn()

                    newarray = []
                    indeweights = 0
                    for shape in shapes:
                        size = np.product(shape)
                        newarray.append(flattened[indeweights : indeweights + size].reshape(shape))
                        indeweights += size
                    agent.neural_network.weights = newarray
            return agents
        
        agents = generate_agents(pop_size)
        for i in range(generations):
            print('Generation',str(i),':')
            agents = fitness(agents)
            agents = selection(agents)
            # print(len(agents))
            agents = crossover(agents,pop_size)
            agents = mutation(agents)
            agents = fitness(agents)
            print(agents[0])
            # print(len(agents))
            
            
            if any(agent.fitness < threshold for agent in agents):
                print('Threshold met at generation '+str(i)+' !')
                break
                
            if i % 5 == 0:
                clear_output()
                
        return agents[0]
            
# ga = genetic_algorithm
# agent = ga.execute(10000,1000,0.0001,possible_coords)
# agent.fitness