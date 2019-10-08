**Implementation of a Geo Distributed LRU (least recently used) cache with time expiration**

**Overall Design**

The Geo Distributed cache (Geocache) is composed of a list of servers and has a pre-defined maximum capacity (max number of items that can be inserted in the cache).

Servers each have their own cache, ip address and location. They represent servers in physical locations. 
Their own cache is implemented using LRU policy (we called these sub-caches lrucache).
Ex: Our Geocache is composed of 3 servers in Montreal, Toronto and New York. 


A while loop (in run.py) handles requests to the Geocache.
Ex: A request could ask the Geocache to retrieve a certain (key, value) from the Geocache.

When a request is received the following steps are followed:

	1. Request is parsed into a format that can be inserted in the cache.
	2. The server closest to the location of the request is found (we want to reduce latency).
	3. We handle the request using the cache of the closest server.
	4. Once the request has been handled: we update the individual cache of all the servers in order to ensure data consistency across 		regions
	5. We then save the data in all servers to protect against network failures or crashes. 
	6. We check the condition for cache expiration and if it is met, the contents of the Geocache are erased.


**Missing functionalities**

 Cache expiry: if no requests are made we cannot reach the code where the condition for cache expiry is tested.
	—> Must implemented something to check the cache expiry while waiting for requests.	
	
 Error Handling for different cases
	- Dealing with requests asking to retrieve keys that are not in the cache is not handled efficiently.
	- Need to write more tests.

Saving data to protect against network crashes is done with a python pickle (there should be better ways). 
