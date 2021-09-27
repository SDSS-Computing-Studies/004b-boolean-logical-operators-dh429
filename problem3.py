#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 

You can use max() to help you find the largest number
You can use min() to help you find the smallest number
How can we find the middle number though?
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""

number1 = input("Enter an integer=>")
number1 = float(number1)

number2 = input("Enter an integer=>")
number2 = float(number2)

number3 = input("Enter an integer=>")
number3 = float(number3)

bignum = max(number1, number2, number3)

smallnum = min(number1 , number2, number3)

if number1 < bignum and number1 > smallnum:
    midnum = number1

elif number2 < bignum and number2 > smallnum:
    midnum = number2

elif number3 < bignum and number3 > smallnum:
    midnum = number3

if smallnum**2 + midnum**2 == bignum**2:
    print(f"{smallnum},{midnum},{bignum} form a Pythagorean triple")

else:
    print(f"{smallnum},{midnum},{bignum} do not form a Pythagorean triple")