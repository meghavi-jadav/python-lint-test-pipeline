"""
Calculator Module

This module provides a basic calculator class with methods for addition, subtraction, multiplication, and division.
"""

class Calculator:
    """Calculator Class"""
    def add(self, a, b):
        """Return the sum of two numbers."""
        return a + b

    def subtract(self, a, b):
        """Return the difference of the two numbers."""
        return a - b

    def multiply(self, a, b):
        """Return the product of the two numbers."""
        return a * b

    def divide(self, a, b):
        """Return the division of the two numbers. Raise error if b is zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
