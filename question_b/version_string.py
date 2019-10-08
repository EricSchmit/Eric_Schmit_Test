"""
Compares two version strings
Return: -1 if version1 < version2, 1 if version1 > version2, 0 if they are equal
"""
import re


def compare_version_string(version1, version2):
	"""
	Compares two version strings and returns whether one is greater than, equal, or less than the other
	:param version1: Ex: 1.2.3
	:param version2: Ex: 1.2.34
	:return: -1 if version1 < version2, 1 if version1 > version2, 0 if they are equal
	"""

	# Tokenize the version strings by taking the parts in between each dot
	# Remove unnecessary 0's
	version1 = [int(token) for token in re.sub(r'(\.0+)*$', '', version1).split(".")]
	version2 = [int(token) for token in re.sub(r'(\.0+)*$', '', version2).split(".")]

	# Compare versions token by token
	# If tokens are not equal --> return appropriate output
	for a, b in zip(version1, version2):
		# b > a --> version1 < version2
		if a < b:
			return -1

		# a > b --> version1 > version2
		elif a > b:
			return 1

	# If we reach here both versions have same length
	# If both versions have the same length they are equal
	# If not, the greater version is the one with largest length
	if len(version1) == len(version2):
		return 0

	elif len(version1) < len(version2):
		return -1

	else:
		return 1













