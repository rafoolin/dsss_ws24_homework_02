"""
TESTS: MATH QUIZ
"""

import unittest
from math_quiz.math_quiz import *


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        """Test if generated random numbers are within the specified range."""
        min_val = 1
        max_val = 30
        # Test a large number of random values
        for _ in range(1000):
            random_number = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= random_number <= max_val)

    def test_get_random_operator(self):
        """Test if the random operator is one of the valid operators."""
        for _ in range(1000):
            random_operator = get_random_operator()
            self.assertTrue(random_operator in ["+", "-", "*"])

    def test_execute_arithmetic_operation(self):
        """Test the arithmetic operation execution for various cases."""
        test_cases = [
            (3, 2, "+", "3 + 2", 5),
            (15, 5, "-", "15 - 5", 10),
            (17, 2, "*", "17 * 2", 34),
        ]
        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = execute_arithmetic_operation(num1, num2, operator)
            self.assertTrue(problem == expected_problem)
            self.assertTrue(answer == expected_answer)

    def test_execute_arithmetic_operation_exception(self):
        """Test the arithmetic operation execution for invalid cases."""

        with self.assertRaises(ValueError) as ctx:
            execute_arithmetic_operation(3, 2, "/")
        self.assertIs(type(ctx.exception), ValueError)


if __name__ == "__main__":
    unittest.main()
