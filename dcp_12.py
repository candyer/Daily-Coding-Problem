# Daily Coding Problem: Problem #12

# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, 
# write a function that returns the number of unique ways you can climb the staircase. 
# The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:
# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2


def solve(n):
	'''
	time: O(n)
	space: O(1)
	for given input from 1 to n, the output will be a fibnacci sequence.
	'''
	a, b = 1, 1
	for _ in range(2, n + 1):
		b, a = a + b, b
	return b

assert solve(4) == 5
assert solve(5) == 8
assert solve(7) == 21
assert solve(10) == 89


# What if, instead of being able to climb 1 or 2 steps at a time, 
# you could climb any number from a set of positive integers X? For example, 
# if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.


def memoize(func):
	memo = {}

	def helper(n, steps):
		if n in memo:
			return memo[n]
		else:
			memo[n] = func(n, steps)
			return memo[n]
	return helper

@memoize
def solve1(n, steps):
	'''
	n: a staircase with n steps
	steps: all possible steps, no duplicate
	'''
	if n <= 1:
		return 1
	res = 0
	for step in steps:
		if n >= step:
			res += solve1(n - step, steps)
	return res

# assert solve1(5,  [1, 3, 5]) == 5
# assert solve1(5,  [1, 2]) == 8
# assert solve1(10, [1, 3, 5]) == 47
# assert solve1(10, [1, 2]) == 89

