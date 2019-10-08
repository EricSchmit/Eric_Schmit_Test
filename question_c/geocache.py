import time
import pickle


class Geocache:
	"""
	Geo Distributed LRU (least recently used) cache with time expiration
	Geocache has a list of servers (each containing their own LRUCache) and a pre-defined capacity
	All servers added to the geocache must have a LRUCache with equal capacity
	"""

	def __init__(self, servers, capacity):
		"""
		:param servers: list
		:param capacity: int
		"""
		self.servers = servers
		self.capacity = capacity
		self.time_created = time.time()

		# Set the capacity of each server to the capacity of the Geocache
		for serv in servers:
			serv.cache.capacity = capacity

	def update_servers(self, req, closest_serv):
		"""
		Ensure data replication
		Performs a request on all servers in servers except closest_serv
		closest_serv should not be updated as it already handled the request
		:param req: Request
		:param closest_serv: Server
		"""

		# Request is a put --> Key, value insert in the cache of the closest server
		if req.type == 0:
			# Iterate through all servers
			for serv in self.servers:
				if serv.ip != closest_serv.ip:  # If Server has not been updated
					serv.cache.put(req.key, req.value)  # Update server cache

		# Request is a get --> Value retrived from the cache of the closest server
		elif req.type == 1:
			# Iterate through all servers
			for serv in self.servers:
				if serv.ip != closest_serv.ip:  # If server has not been updated
					serv.cache.get(req.key)

	def add_server(self, server):
		"""
		Adds a server to the list of servers of a Geocache
		:param server: Server
		"""

		server.capacity = self.capacity  # Set capacity of the server to the capacity of the Geocache
		self.servers.append(server)

	def save_servers(self):
		"""
		Saves the content of the cache in a pickle
		NOT OPTIMAL SOLUTION, needs to be rewritten
		"""

		for serv in self.servers:
			a = serv.cache.hash_map
			with open('cache.pickle', 'wb') as handle:
				pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)

	def check_expiration(self, cur_time):
		"""
		If cache has not been modified for a certain period of time --> Call cache_expiration
		OR other condition. Could write something like: if no actions has been performed on the cache for a certain
		amount of time --> cache_expiration()
		REWRITE
		"""

		time_limit = 1000
		time_elapsed = cur_time - self.time_created

		# Erase cache after an arbitrary amount of time
		if time_elapsed > time_limit:
			self.cache_expiration()

	def cache_expiration(self):
		"""
		Erases the cache of each server of the Geocache
		"""

		# Iterate through servers
		for serv in self.servers:
			serv.cache.hash_table.clear()  # Erase the cache
			serv.cache.cur_size = 0  # Resets the number of items in the cache to 0















