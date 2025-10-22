"""
Team Collaboration Project - Main Module
"""

def calculate_total(items):
    """Calculate total of items"""
    if items is None or len(items) == 0:
        print("No values provided to evaluate.")
    else:
        if all(isinstance(x, (int, float)) for x in items):
            return sum(items)
        else:
            pass
        

    

def calculate_average(items):
    """Calculate average of items"""
    if items is None or len(items) == 0:
        print("No values provided to evaluate.")
    else:
        if all(isinstance(x, (int, float)) for x in items):
            return sum(items) / len(items)
        else:
            pass
        

def find_max(items):
    """Find maximum value"""
    if items is None or len(items) == 0:
        print("No values provided to evaluate.")
    else:
        if all(isinstance(x, (int, float)) for x in items):
            return max(items)
        else:
            pass
        

def find_min(items):
    """Find minimum value"""
    if items is None or len(items) == 0:
        print("No values provided to evaluate.")
    else:
        if all(isinstance(x, (int, float)) for x in items):
            return min(items)
        else:
            pass
        

if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50]
    print(f"Total: {calculate_total(numbers)}")
    print(f"Average: {calculate_average(numbers)}")
    print(f"Max: {find_max(numbers)}")
    print(f"Min: {find_min(numbers)}")