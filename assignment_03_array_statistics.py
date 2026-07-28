# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def get_numbers():
    """Prompt the user for a list of numbers and return them as a list."""
    n = int(input("How many numbers? "))
    if n <= 0:
        print("Error: Number of inputs must be a positive integer.")
        return []
    
    numbers = []
    for i in range(n):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    
    return numbers

def calculate_sum(numbers):
    """Calculate and return the sum of the numbers in the list."""
    total = 0
    for num in numbers:
        total += num
    return total

def calculate_average(numbers):
    """Calculate and return the average of the numbers in the list."""
    if len(numbers) == 0:
        return 0
    total = calculate_sum(numbers)
    return total / len(numbers)

def calculate_maximum(numbers):
    """Calculate and return the maximum of the numbers in the list."""
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def calculate_minimum(numbers):
    """Calculate and return the minimum of the numbers in the list."""
    if len(numbers) == 0:
        return None
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

def main():
    """Main function to read numbers and display statistical results."""
    numbers = get_numbers()
    if not numbers:
        return

    print("\nResults:")
    print(f"Sum:     {calculate_sum(numbers)}")
    print(f"Average: {calculate_average(numbers):.1f}")
    print(f"Maximum: {calculate_maximum(numbers)}")
    print(f"Minimum: {calculate_minimum(numbers)}")

if __name__ == "__main__":
    main()
