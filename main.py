"""
Team Collaboration Project - Main Module
"""

def calculate_total(items):
    """This function takes a list of numerical values and returns the sum of those values""""
    try:
        testItems = [float(x) for x in items]
        return sum(items)
    except ValueError:
        raise ValueError("Error: All provided values must be numeric.")

def calculate_average(items):
    """This function takes a list of numerical values, sums them, divides them by the number of values in the list, and then returns the average of the list"""
    try:
        testItems = [float(x) for x in items]
        return sum(items) / len(items)
    except ValueError:
        raise ValueError("Error: All provided values must be numeric.")

def find_max(items):
    """This function returns the highest value in a list of numerical values"""
    try:
        testItems = [float(x) for x in items]
        return max(items)
    except ValueError:
        raise ValueError("Error: All provided values must be numeric.")

def find_min(items):
    """This function returns the lowest value in a list of numerical values"""
    try:
        testItems = [float(x) for x in items]
        return min(items)
    except ValueError:
        raise ValueError("Error: All provided values must be numeric.")

if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50]
    print(f"Total: {calculate_total(numbers)}")
    print(f"Average: {calculate_average(numbers)}")
    print(f"Max: {find_max(numbers)}")
    print(f"Min: {find_min(numbers)}")

