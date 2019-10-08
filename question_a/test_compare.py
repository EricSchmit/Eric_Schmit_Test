import unittest
from question_a.compare import compare_lines


class TestCompareLine(unittest.TestCase):
	def test_compare_line(self):
		# (1,5) and (2,6) overlap
		line1 = "(1,5)"
		line2 = "(2,6)"
		answer = compare_lines(line1, line2)
		self.assertEqual(answer, True)

		# (1,5) and (6,8) do not overlap
		line1 = "(1,5)"
		line2 = "(6,8)"
		answer = compare_lines(line1, line2)
		self.assertEqual(answer, False)

		# (-1,5) and (0,3) overlap
		line1 = "(-1,5)"
		line2 = "(0,3)"
		answer = compare_lines(line1, line2)
		self.assertEqual(answer, True)

		# (-3.3454, -1) and (-1,-1) overlap
		line1 = "(-3.3454, -1)"
		line2 = "(-2,-1)"
		answer = compare_lines(line1, line2)
		self.assertEqual(answer, True)

		# (-2, -1) and (-0.5,1) do not overlap
		line1 = "(-2,-1)"
		line2 = "(-0.5,1)"
		answer = compare_lines(line1, line2)
		self.assertEqual(answer, False)

		# Testing for uncommon inputs
		line1 = "( 34 , 1)"
		line2 = "( 30, 2 )"
		answer = compare_lines(line1, line2)
		self.assertEqual(answer, True)





