"""
Project Euler Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def largest_palindrome_product(digits):
    if digits < 1:
        print("Can't have a less than 1 digit number doofus")
        return
    curr_max = 0
    min_num = 10**(digits - 1)
    max_num = 10**digits - 1
    # Test down from 10^n - 1 to 10^(n-1) as larger numbers multiplied together usually yield larger products
    # Where n is the number of digits
    # This could be faster and not brute forced, but oh well.
    for x in range(max_num, min_num, -1):
        for y in range(max_num, min_num, -1):
            product = x * y
            if is_palindrome(product):
                if product > curr_max:
                    curr_max = product
    print("Largest Palindrome for", digits, "digit numbers is", curr_max)
    return curr_max

largest_palindrome_product(4)


