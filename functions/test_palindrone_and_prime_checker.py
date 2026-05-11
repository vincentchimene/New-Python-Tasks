from unittest import TestCase
import palindrone_and_prime_checker

class TestPalindroneAndPrimeChecker(TestCase):

    def test_that_the_checker_function_exists(self):
        palindrone_and_prime_checker.checker(23432)

    def test_that_a_palindrome_and_prime_number_asserts_true(self):
        result = palindrone_and_prime_checker.checker(383) 
        self.assertTrue(result)

    def test_that_a_palindrome_but_not_prime_number_asserts_false(self):
        result = palindrone_and_prime_checker.checker(242) 
        self.assertFalse(result)
    
    def test_that_a_not_palindrome_but_prime_number_asserts_False(self):
        result = palindrone_and_prime_checker.checker(29) 
        self.assertFalse(result)

    def test_that_a_not_palindrome_and_not_prime_number_asserts_False(self):
        result = palindrone_and_prime_checker.checker(245) 
        self.assertFalse(result)
        

        



