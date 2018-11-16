# Daily Coding Problem: Problem #4


# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.


def solve1(array):
	'''
	time: O(n^2)
	space: O(1)
	'''
	n = len(array)
	res = 1
	while res < n + 1:
		if res not in array:
			return res
		res += 1


def solve2(array):
	'''
	time: O(nlog(n))
	space: O(1)
	'''
	array.sort()
	n = len(array)
	res = 1
	for i in range(n):
		if array[i] > 0:
			if array[i] == res:
				res += 1
			elif array[i] > res:
				return res


def solve(array):
	'''
	time: O(n)
	space: O(1)
	the result is always in [1, len(array) + 1], both sides inclusive
	'''
	array = [num for num in array if num > 0]
	if array == []: return 1
	n = len(array)
	for num in array:
		if abs(num) - 1 < n and array[abs(num) - 1] > 0:
			array[abs(num) - 1] = -array[abs(num) - 1]
	for i, num in enumerate(array):
		if num > 0:
			return i + 1
	return n + 1



# assert solve([-1, -2, -3]) == 1
# assert solve([6, 10, 3, -2, 1, -4, -8, -7, 1]) == 2
# assert solve([5, 4, 3, -1, 2, 1]) == 6
# assert solve([3, 4, -1, 1]) == 2
# assert solve([1, 2, 0]) == 3
# assert solve([7, 4, 1, 6, 2, 3]) == 5
# assert solve([14, -15, -25, 8, 3, 8, -4, 5, 18, -17, 16, 17, -2, -22, -26, -15, 2, 1, -12, -19, 17, -4, 26, 15, -3, -21]) == 4






