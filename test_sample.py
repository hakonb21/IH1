from sample import fizzbuzz
import pytest 




def test_mod_by_3_and_5():
    """Tests if an integer divisible by 3 and 5 put into fizzbuzz will return the string 
    "fizzbuzz" """
    assert fizzbuzz(15) == "FizzBuzz"

def test_mod_5():
    """Tests if the fizzbuzz function returns "Buzz" when given an integer divisable by 5 """
    assert fizzbuzz(10) == "Buzz"


def test_mod_3():
    """Tests if the fizzbuzz function returns "Fizz" when given an integer divisible by 3"""
    assert fizzbuzz(9) == "Fizz"






