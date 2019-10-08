from question_c.lrucache import *
from question_c.geocache import *
from question_c.server import *
from geographiclib.geodesic import Geodesic
import re


def create_servers():
	"""
	Used for testing, creates servers
	Returns a list of servers
	:return: list
	"""

	# List of servers
	servers = []

	# Coordinates of the servers
	mtl_coordinates = Coordinates(45.5017, 73.5673)
	tor_coordinates = Coordinates(43.6532, 79.3832)
	nyc_coordinates = Coordinates(40.7128, 74.0060)

	# Initialize Caches
	mtl_cache = LRUCache(5)
	tor_cache = LRUCache(5)
	nyc_cache = LRUCache(5)

	# Fill the caches up with arbitrary actions
	cache_actions(mtl_cache)
	cache_actions(tor_cache)
	cache_actions(nyc_cache)

	# Initialize 3 servers
	mtl = Server("mtl", "15.2.3", mtl_coordinates, mtl_cache)
	tor = Server("tor", "20.3.1", tor_coordinates, tor_cache)
	nyc = Server("nyc", "3.4.1", nyc_coordinates, nyc_cache)

	# Append servers to the list
	servers.append(mtl)
	servers.append(tor)
	servers.append(nyc)

	return servers


def parse_request(raw_req):
	"""
	Returns a request object given a raw request
	Will depend on the format of the request
	Need to parse the request in order for it to be in a format that can be inserted into the cache
	Here the format is: "type, coordinate1, coordinate2, key, value"
	Ex: "1,45.5017,73.5673,3,5"
	:param raw_req: string
	:return: request
	"""

	# Parse request into a list
	temp = [float(x) for x in re.sub('[^0-9,.-]', '', raw_req).split(",")]
	type = temp[0]
	lat = temp[1]
	lon = temp[2]
	key = temp[3]
	value = temp[4]

	# Create request object
	coordinates = Coordinates(lat, lon)
	request = Request(type, coordinates, key, value)

	return request


def get_closest_serv(servers, coordinates):
	"""
	Iterates through a list of servers and returns the server closest to the given coordinates
	:param servers: list
	:param coordinates: coordinates
	:return: closest_serv: Server
	"""

	cur_distance = float("inf")  # Initialize minimum distance to infinity
	closest_serv = servers[0]  # Initialize closest serv to the first server of the list

	# Iterate through all servers
	for serv in servers:
		d = get_coordinates_distance(serv.coordinates, coordinates)  # Get distance between current server and coordinates

		# d < current best distance
		if d < cur_distance:
			cur_distance = d
			closest_serv = serv  # Update current closest server

	return closest_serv


def handle_request(req, closest_serv):
	"""
	# Executes either a PUT or a GET on the cache of closest_serv
	:param req: Request
	:param closest_serv: Server
	:return:
	"""

	# Request is a PUT --> (key, value) inserted in the cache of the closest server
	if req.type == 0:
		closest_serv.cache.put(req.key, req.value)
		# Should add confirmation from cache that operation was successful

	# Request is a GET --> Value retrived from the cache of the closest server
	elif req.type == 1:
		value = closest_serv.cache.get(req.key)
		return value
		# Should add confirmation from cache that operation was successful


def get_coordinates_distance(c1, c2):
	"""
	Returns the distance in meters between two coordinates objects
	:param c1: coordinates
	:param c2: coordinates
	:return: d: float
	"""

	# Extract latitudes and longitudes
	p1_lat, p1_lon = c1.lat, c1.lon
	p2_lat, p2_lon = c2.lat, c2.lon

	# Use geographiclib to compute distance between points
	geod = Geodesic.WGS84
	g = geod.Inverse(p1_lat, p1_lon, p2_lat, p2_lon)
	d = float(format(g['s12']))

	return d


def create_requests():
	"""
	Used for testing: creates arbitrary requests to be handled by the Geocache
	Returns a list of requests
	:return:
	"""

	# List of requests
	req_list = []

	# Two different locations
	req_coordinates = Coordinates(46.8139, 71.2080)  # Quebec city
	req_coordinates = Coordinates(43.8561, 79.3370)  # Markam

	# Construct requests
	req = Request(0, req_coordinates, 13, 13)  # put
	req2 = Request(0, req_coordinates, 14, 14)  # put
	req3 = Request(1, req_coordinates, 5, 14)  # get
	req4 = Request(1, req_coordinates, 6, 6)  # get

	# Append to request list
	req_list.append(req)
	req_list.append(req2)
	req_list.append(req3)
	req_list.append(req4)

	return req_list


def cache_actions(cache):
	"""
	Used for testing
	:param cache: Cache
	:return: None
	"""

	cache.put(1, "one")
	cache.put(3, "three")
	cache.put(4, "four")
