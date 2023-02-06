from access_data import get_possible_spots
from input_data import get_data

get_data("Birmingham")
possible,latitudes,longitudes = get_possible_spots()
print(possible)