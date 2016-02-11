import json
import math

# get distance
def getDistance(my_loc, station):
    lat_dist = my_loc["lat"] - station["latitude"]
    long_dist = my_loc["lng"] - station["longitude"]
    straight_dist = math.sqrt((lat_dist*lat_dist)+(long_dist*long_dist))
    return straight_dist

# Set my default location
MY_LOC = {"lat" : 53.3461, "lng" : -6.254863 }

# get the list of stations
def getBikeData():
    f = open('dummy_data.json')
    stations = json.load(f)
    return stations

# Write a method which will take a station list and
# return only those stations which have bikes available


# Write a method which will take our location object and 
# a list of stations and return the station that is closest to us 

# This is our main method, it links 
# all the different parts together
def main():
    print "This is our main method!"

if __name__ == '__main__':
    main()
