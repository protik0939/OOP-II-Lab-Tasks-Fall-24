"""
Create a custom Exception and handle it in the following way:
"""

class InvalidVoterException(Exception):
    pass

# a) Take an input named age
try:
    age = int(input("Enter age: "))

    # b) if age < 18, it will raise InvalidVoterException
    if age < 18:
        raise InvalidVoterException("Age is less than 18. Not eligible to vote.")
    else:
        print("Eligible to vote.")
except InvalidVoterException as e:
    print(e)
except ValueError:
    print("Invalid input. Please enter a valid integer.")