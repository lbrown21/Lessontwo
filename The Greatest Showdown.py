# Task 1

num1 = 3
num2 = 3
num3 = 4

def identify_largest(num1, num2, num3):
    largest = max(num1, num2, num3)
    return largest

# Task 2: Identify the Smallest
def identify_smallest(num1, num2, num3):
    smallest = min(num1, num2, num3)
    return smallest

# Task 3: Equality Check
def identify_numbers(num1, num2, num3):
    numbers = [num1, num2, num3]
    numbers_set = set(numbers)
    
    if len(numbers_set) == 1:
        print("All numbers are equal.")
    elif len(numbers_set) == 2:
        equal_numbers = [num for num in numbers_set if numbers.count(num) > 1]
        print(f"Two numbers are equal and the largest.")
        print(f"The equal numbers are: {equal_numbers[0]}")
    else:
        print("No numbers are equal.")

# Main program
if __name__ == "__main__":
    largest = identify_largest(num1, num2, num3)
    smallest = identify_smallest(num1, num2, num3)
    
    print(f"The smallest number is {smallest}.")
    print(f"The largest number is {largest}.")
    
    identify_numbers(num1, num2, num3)
