def fizzbuzz(integer):
    if integer % 3 == 0 and integer % 5 == 0:
        return "FizzBuzz"

    elif integer % 5 == 0:
        return "Buzz"
    
    elif integer % 3 == 0:
        return "Fizz"

    else:
        return integer