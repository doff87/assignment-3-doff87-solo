"""
Team Collaboration Project - Main Module
"""

def calculate_total(items):
    """This function takes a list of numerical values and returns the sum of those values"""
    return sum(items)

def calculate_average(items):
    """This function takes a list of numerical values, sums them, divides them by the number of values in the list, and then returns the average of the list"""
    return sum(items) / len(items)

def find_max(items):
    """This function returns the highest value in a list of numerical values"""
    return max(items)

def find_min(items):
    """Find minimum value"""
    return min(items)

if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50]
    print(f"Total: {calculate_total(numbers)}")
    print(f"Average: {calculate_average(numbers)}")
    print(f"Max: {find_max(numbers)}")
    print(f"Min: {find_min(numbers)}")

