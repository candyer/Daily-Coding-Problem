# Daily Coding Problem: Problem #9


# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?



def solve1(array):
	'''
	time: O(n)
	space: O(n)
	'''
	if array == []: return 0
	n = len(array)
	dp = [float('-inf')] * n
	for i in range(n):
		dp[i] = max(array[i] + dp[i - 2], dp[i - 1], array[i])
		# print i, array[i], dp
	return dp[-1]



def solve2(array):
	''' 
	time: O(n)
	space: O(1)
	'''
	if array == []: return 0
	n = len(array)
	if n <= 2: return max(array)
	dp = [float('-inf'), float('-inf'), float('-inf')]
	for i in range(n):
		a, b, c = dp
		dp[i % 3] = max(array[i] + dp[(i - 2) % 3], dp[(i - 1) % 3], array[i])
	return max(dp)



def solve3(array):
	''' 
	time: O(n)
	space: O(1)
	'''
	if array == []: return 0
	if len(array) <= 2: return max(array)
	return max(solve(array[:-2]) + array[-1], solve(array[:-1]), array[-1])

# assert solve([5, 1, 1, 5, -1]) == 10
# assert solve([2, 4, 6, 2, 5]) == 13
# assert solve([5, 1, 1, 5]) == 10
# assert solve([-1, 1, 0, -5]) == 1
# assert solve([-100, 1, 103, 10]) == 103
# assert solve([-100, -1, -103, -10]) == -1

# from random import randint as r
# for _ in range(1000):
# 	array = []
# 	for _ in range(5):
# 		array.append(r(-10, 10))
# 	# print array
# 	if not solve(array) == solve1(array) == solve2(array):
# 		print array




