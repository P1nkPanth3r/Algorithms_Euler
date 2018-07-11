# Problem 15
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6
# routes to the bottom right corner. How many such routes are there through a 20×20 grid?

# Description:
# The key in this problem is to realize we can easily represent the rightward (r) and downward (d) movements using a
# binomial distribution and simply solve the resulting combinations. Thus, we can start by creating a vector with 40 indices,
# starting with 20 r's and then 20 d's (obviously there is only one way to do this). Then, we can imagine taking a single r
# and placing it on the "right-hand" side (somewhere in the last 20 indices). There are 20-choose-1 = 20 ways to do this
# (one way for each index). However, this also means we are de-facto placing one d on the "left-hand" side (somewhere in
# the first 20 indices) which can also happen 20-choose-1 = 20 ways, so in total we have (20-choose-1)**2 = 400
# possibilities. In general, since this sequence of 20-choose-i for 0 <= i <= 20 is binomial it follows pascal's triangle,
# so the number of routes is simply the sum of the squared values at the 20th row of the triangle.

# It is easy to generalize this result for any NxN square grid - simply replace pascal(20) with pascal(N).

def pascal(n):
    line = [1]
    for k in range(n):
        line.append(line[k] * (n-k) / (k+1))
    return line
pascal_output = pascal(20)
pascal_squared = [x**2 for x in pascal_output]
print(sum(pascal_squared))