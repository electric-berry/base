import pandas
import numpy as np
# from matplotlib import pyplot as plt

csv = pandas.read_csv("data.csv")
latitude = list(csv.columns).index("latitude")
longitude = list(csv.columns).index("longitude")
latitudes = []
longitudes = []
pairs = []
for row in csv.values:
    lat = float(row[latitude])
    longi = float(row[longitude])
    if not([lat,longi] in pairs):
        latitudes.append(lat)
        longitudes.append(longi)
        pairs.append([lat,longi])

possible = set()
def points_from_line(start_point,end_point,distance = 0.1,y_distance = 0.01):
    points = []
    
    start_point,end_point = sorted([start_point,end_point])
    start_point = np.array(start_point)
    end_point = np.array(end_point)
    start_x,start_y = np.array(start_point)
    end_x,end_y = np.array(end_point)
    gradient = (end_y - start_y)/(end_x-start_x)
    distance_between = np.linalg.norm(start_point-end_point)
    
    num_points = round(distance_between/distance)
    # print(start_x,start_y)
    counter = 0
    while True:
        x = start_x + counter*distance
        y = start_y + gradient*(counter*distance)
        if x > end_x or y > end_y:
            break
        top_point = [round(x,2),round(y+y_distance,3)]
        bottom_point = [round(x,2),round(y-y_distance,3)]
        # print([x,y])
        if not(tuple(top_point) in possible):
            possible.add(tuple(top_point))
            points.append(top_point)
        # else:
        #     print("IN")
        if not(tuple(bottom_point) in possible):
            possible.add(tuple(bottom_point))
            points.append(bottom_point)
        # else:
        #     print("IN")
        # points.append([x,y])
        counter += 1
    return points

counter = 0
# fig, ax = plt.subplots()
for i in range(0,200,2):
    x,y = latitudes[i],longitudes[i]
    points = points_from_line([latitudes[i],longitudes[i]],[latitudes[i+1],longitudes[i+1]])
    # for point in points:
    #     ax.scatter(point[0],point[1],s=1,c="red")
    # ax.plot(latitudes[i:i+2], longitudes[i:i+2], 'bo-', linewidth=0.1, markersize=1)
    
    counter += 1

# Points is the possible variables
# Latitudes and Longitudes are the road data.