# Write a recursive Python program to print a symmetric diamond pattern made of stars (*)
# for a given number n. The diamond should have 2 * n - 1 rows.
# You must use recursion only to generate both the top and bottom halves of the diamond.

# Requirements:
# Input: An integer n (number of rows in the top half).
# Output: A full diamond made of *, centered and symmetrical.
# No loops allowed — only recursion.

def print_line(spaces, stars):
    print(' ' * spaces + '*' * stars)

def print_top(n, current=1):
    if current > n:
        return
    print_line(n - current, 2 * current - 1)
    print_top(n, current + 1)

def print_bottom(n, current=1):
    if current > n - 1:
        return
    print_line(current, 2 * (n - current) - 1)
    print_bottom(n, current + 1)

def print_diamond(n):
    print_top(n)
    print_bottom(n)

# Example usage
if __name__ == "__main__":
    rows = 4
    print_diamond(rows)
