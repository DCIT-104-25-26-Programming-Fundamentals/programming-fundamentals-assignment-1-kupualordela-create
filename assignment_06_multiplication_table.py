# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def multiplication_table(number):
    """
    Generate and print the multiplication table for a given number from 1 to 12.

    Args:
        number (int): The number for which to generate the multiplication table.
    """
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        result = number * i
        print(f"{number} x {i} = {result}")

def full_multiplication_tables(n):
    """
    Generate and print the full multiplication tables for numbers from 1 to n.

    Args:
        n (int): The upper limit for generating multiplication tables.
    """
    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    for number in range(1, n + 1):
        multiplication_table(number)
        print("---")  
def main():
    """
    Main function to execute the multiplication table generator program.
    """
    # Part A: Single Table
    try:
        number = int(input("Enter a number for the multiplication table: "))
        multiplication_table(number)
    except ValueError:
        print("Error: Please enter a valid integer.")

    # Part B: Full Tables from 1 to N
    try:
        n = int(input("Enter a positive integer N for full multiplication tables: "))
        full_multiplication_tables(n)
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    main()