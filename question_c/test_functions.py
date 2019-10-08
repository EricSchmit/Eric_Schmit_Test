from question_c.functions import *
from question_c.server import *
import unittest


class TestGetClosestServ(unittest.TestCase):
	def test_get_closest_serv(self):
		# Create servers for testing
		# create_servers() creates 3 servers with locations: Montreal, Toronto, New york
		servers = create_servers()

		# Create coordinates to be tested
		c1 = Coordinates(46.8139, 71.2080)  # Quebec city
		c2 = Coordinates(43.8561, 79.3370)  # Markam
		c3 = Coordinates(42.3601, 71.0589)  # Boston

		# Retrieve closest server to each of the coordinates
		serv1 = get_closest_serv(servers, c1)  # Quebec should be closest to Montreal
		serv2 = get_closest_serv(servers, c2)  # Markam should be closest to Toronto
		serv3 = get_closest_serv(servers, c3)  # Boston should be closes to New york

		# Test
		self.assertIs(serv1.name, "mtl")
		self.assertIs(serv2.name, "tor")
		self.assertIs(serv3.name, "nyc")


class TestGetCoordinatesDistance(unittest.TestCase):
	def test_get_coordinates_distance(self):
		# Coordinates of toronto and montreal as an example
		c1 = Coordinates(45.5017, 73.5673)
		c2 = Coordinates(43.6532, 79.3832)
		real_distance = 505  # Distance between c1 and c2 according to http://boulter.com/gps/distance

		# Get distance in km
		distance = get_coordinates_distance(c1, c2)
		distance_km = round(distance/1000, 0)  # Assuming distance does not have to be accurate to the meter

		# Test
		self.assertAlmostEqual(distance_km, real_distance)
















