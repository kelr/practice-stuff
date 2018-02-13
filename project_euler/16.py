"""
Project Euler Problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

"""

# Python is great
def sum_digits_power_two(exp):
    big_num = str(2**exp)
    curr_sum = 0
    for n in big_num:
        curr_sum += int(n)
    return curr_sum

print(sum_digits_power_two(15))
print(sum_digits_power_two(1000))