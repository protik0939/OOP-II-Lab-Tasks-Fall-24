"""
given an array, a = [10, 5, 15, 20]
divisor => take input of int type
"""

a = [10, 5, 15, 20]

try:
    divisor = int(input("Enter divisor: "))

    # a) Perform division
    result = [x / divisor for x in a]
    print("Division results:", result)

    # b) Handle exceptions
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid value entered.")
except NameError:
    print("Error: Variable name not found.")
except TypeError:
    print("Error: Type mismatch.")
except IndexError:
    print("Error: Index out of range.")
except AttributeError:
    print("Error: Invalid attribute access.")
except FileNotFoundError:
    print("Error: File not found.")

# c) Use try, except, else, finally
finally:
    print("Execution completed.")