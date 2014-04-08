# -*- coding: utf-8 -*-

# weather.py
#
# display temperature

import urllib2
import json

city = raw_input("City: ")
state = raw_input("State: ")

with open("key.txt") as key:
  APIkey = key.readline().strip()

http = "http://api.wunderground.com/api/" + APIkey + "/geolookup/conditions/q/" + state + "/" + city + ".json"

f = urllib2.urlopen(http)

json_string = f.read()
parsed = json.loads(json_string)
try:
  location = parsed['location']['city']
  temperature = parsed['current_observation']['temp_f']
  print "Current Temperature in %s is %s" % (location, temperature)
except KeyError:
  print "City not found"

f.close()
