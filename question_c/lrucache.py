class LRUCache:
	"""
	Cache follows least recently used (LRU) policy
	Uses a hash map and a doubly linked list
	"""

	def __init__(self, capacity):
		# Set up capacity and size of the cache
		self.capacity = capacity
		self.cur_size = 0

		# Hash table to access cache items in O(1)
		self.hash_map = {}

		# Set up head and tail
		self.head = Node(0, 0)  # May have to check that key != 0 when handling requests
		self.tail = Node(0, 0)
		self.head.next = self.tail
		self.tail.prev = self.head

	def put(self, key, value):
		"""
		Adds a node to the cache if the key does not exist in the hash table
		Else updates the value associated with the key
		"""

		# Key exists --> update value
		if key in self.hash_map:
			node = self.hash_map[key]
			node.value = value
			return key, value  # Return key value for consistency
		# Create and insert node at the front (MRU position)
		else:
			new_node = Node(key, value)

			# Deal with over capacity issues
			if self.cur_size >= self.capacity:
				last_node = self.tail.prev  # LRU node
				self.remove(last_node)  # Remove LRU node
				del self.hash_map[last_node.key]  # Update hash table

			self.add_to_front(new_node)
			self.hash_map[key] = new_node
			return key, value  # Return key, value for consistency

	def get(self, key):
		"""
		Returns the value associated with the key
		Moves the affected node to the front (MRU)
		"""

		# Key is in cache --> Return key and value associated
		if key in self.hash_map:
			node = self.hash_map[key]
			self.remove(node)
			self.add_to_front(node)
			value = node.value
			return key, value

		# Key was not in cache
		else:
			raise ValueError("Key not in cache")

	def add_to_front(self, node):
		"""
		Adds a node to the front
		"""

		# Link up new node
		node.prev = self.head
		node.next = self.head.next

		# Update previous links
		self.head.next.prev = node
		self.head.next = node

		# Update capacity
		self.cur_size += 1

	def remove(self, node):
		"""
		Removes a node and links up the nodes on either side
		"""

		# If key exists in cache
		if node.key in self.hash_map:
			prev = node.prev
			next = node.next
			next.prev = prev
			prev.next = next
			self.cur_size -= 1  # Decrement size
		else:
			raise ValueError("Key not in cache")

	def print_nodes(self):
		n = self.head
		while n:
			n = n.next
			if n == self.tail:
				break
			print("%s " % n, end = " ")
		print("")


class Node:
	def __init__(self, key, value):
		"""
		Node to be inserted in LRUcache
		:param key: undefined
		:param value: undefined
		"""

		self.key = key
		self.value = value
		self.next = None
		self.prev = None

	def __str__(self):
		return "(%s, %s)" % (self.key, self.value)





