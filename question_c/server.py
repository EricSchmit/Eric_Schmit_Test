class Server:
	def __init__(self, name, ip, coordinates, cache):
		"""
		Represents a server with its name, ip address, geographic coordinates and LRUcache
		:param name: string
		:param ip: string
		:param coordinates: Coordinates
		:param cache: LRUCache
		"""

		# Set up name, ip address, coordinates and cache
		self.name = name
		self.ip = ip
		self.coordinates = coordinates
		self.cache = cache

	def __str__(self):
		return "(%s, %s)" % (self.name, self.ip)

	def print_server(self):
		print(self)
		self.cache.print_nodes()


class Request:
	"""
	Object representing a request to the Geographic distributed cache
	Type: type of request to handle (ex: PUT or GET)
	Coord: Geographic coordinates of the request
	Key: Key associated with the request
	Value: Value associated with the request
	"""

	def __init__(self, type, coordinates, key, value):
		# Key, value pair
		self.key = key
		self.value = value

		# Type of request: 0 for put(), 1 for get()
		self.type = type

		# Location of the request
		self.coord = coordinates


class Coordinates:
	"""
	Geographic coordinates of a location
	"""
	def __init__(self, latitude, longitude):
		# Latitude, Longitude
		self.lat = latitude
		self.lon = longitude
