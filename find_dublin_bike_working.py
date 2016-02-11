#import requests
import json
import math

# Set my default location
MY_LOC = {"lat" : 53.3461, "lng" : -6.254863 }

# get the list of stations
def getBikesResponse():
    url = 'http://api.citybik.es/v2/networks/dublinbikes'
    response = requests.get(url)
    response_dict = json.loads(response.text)
    return response_dict["network"]["stations"]

def getBikeData():
    f = open('dummy_data.json')
    stations = json.load(f)
    return stations

# get the stations which have bikes available
def findAvailableBikes(stations):
    candidates = []
    for st in stations:
        if st["free_bikes"]>0:
            candidates.append(st)
    return candidates

# get distance
def getDistance(my_loc, station):
    lat_dist = my_loc["lat"] - station["latitude"]
    long_dist = my_loc["lng"] - station["longitude"]
    straight_dist = math.sqrt((lat_dist*lat_dist)+(long_dist*long_dist))
    return straight_dist

# find which of those is closest to us 
def findClosestStation(my_loc, stations):
    closest = stations[0]
    for st in stations:
        straight_dist = getDistance(my_loc,st)
        if straight_dist < getDistance(my_loc,closest):
            closest = st
    return closest

def main():
    stations = getBikesResponse()
    candidates = findAvailableBikes(stations)
    closest = findClosestStation(MY_LOC, candidates)
    print "The nearest available bike is at: "+closest["name"]

if __name__ == '__main__':
    main()
