"""
Takes two lines as input
Returns True if they overlap, False if they don't
Ex Input: (1,5) (6,8)
Return: False
"""
import sys
import re


def main():
	# Take in two lines
	first_input = sys.argv[1]
	second_input = sys.argv[2]

	# Compare
	answer = compare_lines(first_input, second_input)
	print(answer)
	return answer


def compare_lines(line1, line2):
	"""
	:param line1: String
	:param line2: String
	:return: Bool
	"""
	# Process the 4 points into floats and make sure that x1 < x2 and x3 < x4
	x1, x2 = get_points(line1)
	x3, x4 = get_points(line2)

	# Lines overlap
	if x3 < x2 and x1 < x4:
		return True

	# Lines overlap
	elif x1 < x4 and x3 < x2:
		return True

	# No overlap
	else:
		return False


def get_points(line):
	"""
	:param line: Ex: (-1.3, 23)
	:return: x1 and x2 with x1 < x2. Ex x1 = -1.3, x2 = 23
	"""
	# Extract the points into a list
	# Use regex to be able to process negative and decimal numbers
	temp = [float(x) for x in re.sub('[^0-9,.-]', '', line).split(",")]

	# Make sure x1 < x2
	x1 = min(temp)
	x2 = max(temp)

	return x1, x2


main()
