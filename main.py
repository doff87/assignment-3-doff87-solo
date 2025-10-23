"""
Team Collaboration Project - Main Module
"""

def calculate_total(items):
    """Calculate total of items"""
    try:
        items = [float(x) for x in items]
        return sum(items)
    except ValueError:
        print("Error: All provided values must be numeric.")
    return sum(items)

def calculate_average(items):
    """Calculate average of items"""
    try:
        items = [float(x) for x in items]
        return sum(items) / len(items)
    except ValueError:
        print("Error: All provided values must be numeric.")
    return sum(items) / len(items)

def find_max(items):
    """Find maximum value"""
    try:
        items = [float(x) for x in items]
        return max(items)
    except ValueError:
        print("Error: All provided values must be numeric.")
    return max(items)

def find_min(items):
    """Find minimum value"""
    try:
        items = [float(x) for x in items]
        return min(items)
    except ValueError:
        print("Error: All provided values must be numeric.")
    return min(items)

if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50]
    print(f"Total: {calculate_total(numbers)}")
    print(f"Average: {calculate_average(numbers)}")
    print(f"Max: {find_max(numbers)}")
    print(f"Min: {find_min(numbers)}")

