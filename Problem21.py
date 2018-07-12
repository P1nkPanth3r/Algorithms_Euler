# Problem 21
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

def factors(n): # Return all factors of a number (not including itself)
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    result = sorted(result)
    return result[:-1]

amicable = []
for a in range(1,10000):
    a_fact = list(factors(a)) # All factors of number a
    a_fact_sum = 0
    for item in a_fact:
        a_fact_sum += item # Sum items in the list of factors of a
    sum_fact = list(factors(a_fact_sum)) # Input the sum of a's factors and find its factors
    sum_total_fact = 0
    for item in sum_fact:
        sum_total_fact += item # Sum the factors of a's factors
    if a == sum_total_fact and a != a_fact_sum and a_fact_sum < 10000: # If a and a's factors are amicable, and both less than 10,000
        amicable.append(a)
        amicable.append(a_fact_sum)
    elif a == sum_total_fact and a != a_fact_sum: # If a and a's factors are amicable, but a's factors sum to over 10,000
        amicable.append(a)
output = []
for item in amicable:
    if item not in output: # Ignore duplicates
        output.append(item)
print(sum(output))

# Approximate solution runtime: 0.18401575088500977 seconds
