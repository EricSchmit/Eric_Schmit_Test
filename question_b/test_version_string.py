import unittest
from question_b.version_string import *


class TestCompareVersionString(unittest.TestCase):
	def test_compare_version_string(self):
		assert compare_version_string("1", "1") == 0
		assert compare_version_string("1.1", "1.2") < 0
		assert compare_version_string("1.0", "1.0.1") < 0
		assert compare_version_string("1.0.1", "1.0") > 0
		assert compare_version_string("1.0.4.10", "1.0.4.2") > 0
		assert compare_version_string("2.02", "4.02.01") < 0
		assert compare_version_string("4.3.1.9.84", "4.3") > 0
		assert compare_version_string("2.2", "2.2.6.7.8") < 0
		assert compare_version_string("2.2", "3.1") < 0
		assert compare_version_string("2.1", "1.2") > 0
		assert compare_version_string("7.3.1", "7.3.1") == 0
		assert compare_version_string("2.01.1", "2.1.1") == 0
		assert compare_version_string("2.1.1", "2.01.1") == 0
		assert compare_version_string("1", "1.0000") == 0
		assert compare_version_string("1.0000", "1") == 0
		assert compare_version_string("1.0.2.0", "1.0.2") == 0
		assert compare_version_string("1.0003.1", "1.0004.1") < 0
