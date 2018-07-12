# Problem 24
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2,
# 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The
# lexicographic permutations of 0, 1 and 2 are: 012, 021, 102, 120, 201, 210. What is the millionth lexicographic
# permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# Description:
# We could naively create a list of all possible permutations of the digits above, sort the list, and return the value at
# index 1,000,000 of our list. However, this would be somewhat time consuming as there are 10! = 3,628,800 possible permutations
# and then we would still need to sort the list (which has O(n*log(n)) complexity using Python's sorted(data) function).
# Instead, we can use the algorithm below:

import math
string = '0123456789'
str_rem = string
out_string = ''
fact_table = [math.factorial(n) for n in range(1,len(string))] # Return list with number of unique permutations for an n-digit string
contribution = 0
remaining = 999999 # The number of smaller permutations we still need to pass over
for index in range(0,len(string)):
    remaining -= contribution # Subtract contribution for current number of permutations
    contribution = 0
    counter = 0
    found_max = False # Have we reached permutation 1,000,000 yet?
    while contribution < remaining and found_max == False:
        if (contribution + fact_table[-1]) <= remaining: # If we can add all permutations for a given sub-string without exceeding permutation 1 million
            contribution += fact_table[-1] # Add all combinations beginning with the value at the current index, since we still won't be at 1 million
            counter += 1 # Move to the next digit in the string
        else:
            found_max = True
    out_string += str_rem[counter] # Add digit to output string
    str_rem = str_rem.replace(str_rem[counter],"") # Remove digit from remaining characters
    fact_table = fact_table[:-1] # Remove largest factorial in table
print(out_string)

# Approximate solution runtime: 0.0 seconds