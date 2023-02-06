def test_func(agent):
    # ! coords are tuples
    possible_coords = agent.config
    return sorted(possible_coords)[0][0]
    
    
def fitness_func(possible_coords):
    '''
    start car on random part of road (weighted on traffic)
    count when fuel is at certain level, refill
    calculate the cost for fuel
    rinse and repeat n times
    calculate average profitability
    '''
    pass