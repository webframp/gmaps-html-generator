#!/bin/python

import csv
import time
import pygmaps
from ggeocoder import Geocoder

# change to cli opts with defaults
#(45.0004904, -120.2110871, '0000FF', 'Fossil, OR', 'DROP')
center_lattitude = 45.000
center_longitude = -120.211
zoom = "8"

#(46.175566, -123.835858)
address = "1760 7th St - Astoria, OR  97103-5205"

def latitude(t):
    return t[0]

def longitude(t):
    return t[1]

processor = Geocoder()

map = pygmaps.maps(center_lattitude, center_longitude, zoom)

# loop through list from csv
with open('kh-addresses.csv', 'rU') as csv_file:
    address_list = csv.reader(csv_file)
    for kingdom_hall, address in address_list:
        time.sleep(0.15) # throttle our API requests
        lat_long_tuple = processor.geocode(address)
        for result in lat_long_tuple:
            map.addpoint(latitude(result.coordinates), 
                         longitude(result.coordinates), 
                         "#0000FF", 
                         title=kingdom_hall)


# change to cli opt with default
map.draw('out.html')
