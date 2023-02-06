def test_func(agent):
    # ! coords are tuples
    possible_coords = agent.config
    return sorted(possible_coords)[0][0]
    
    
def fitness_func(possible_coords):
    pass