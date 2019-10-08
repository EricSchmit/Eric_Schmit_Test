from question_c.functions import *


def main():
	# Initialize parameters of the cache
	capacity = 5

	# Create servers
	servers = create_servers()

	# Create Geo Distributed Cache with capacity 5 and the created servers
	geo_cache = Geocache(servers, capacity)

	# While loop to handle cache requests in real time
	while True:
		# Get request and parse it (example request: "1,45.5017,73.5673,3,5")
		raw_request = input()  # This should be modified depending on how we receive input requests
		request = parse_request(raw_request)  # Parsed request

		# Get server closest to the request
		closest_serv = get_closest_serv(servers, request.coord)

		# Handle request with server closest to the request
		request_output = handle_request(request, closest_serv)

		# Update all servers to ensure data consistency accross locations
		geo_cache.update_servers(request, closest_serv)

		# Save data to protect against network failures/crashes
		geo_cache.save_servers()

		# Cache expires after a certain amount of time (can/should change the condition for expiry)
		cur_time = time.time()
		geo_cache.check_expiration(cur_time)


main()

