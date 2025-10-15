"""
Team Collaboration Project - Main Module
"""

def calculate_total(items):
    """Calculate total of items"""
    return sum(items)

def calculate_average(items):
    """Calculate average of items"""
    return sum(items) / len(items)

def find_max(items):
    """Find maximum value"""
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

