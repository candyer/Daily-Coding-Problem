# Daily Coding Problem: Problem #2

# Given an array of integers, return a new array such that each element at index i of the new array 
# is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?


def solve1(array):
	'''
	time: O(n) * 2  with division
	space: O(n)
	'''
	total = 1
	for num in array:
		total *= num
	res = []
	for num in array:
		res.append(total / num)
	return res


def solve2(array):
	'''
	time: O(n^2), without division
	space: O(n)
	'''
	n = len(array)
	res = []
	for i in range(n):
		count = 1
		tmp = 1
		while count < n:
			j = (i + count) % n
			tmp *= array[j]
			count += 1 
		res.append(tmp)
	return res


def solve3(array):
	'''
	time: O(n) * 2, without division
	space: O(n)
	'''
	n = len(array)
	res = [1] * n

	tmp = 1
	for i in range(n):
		res[i] = tmp
		tmp *= array[i]

	tmp = 1
	for i in range(n - 1, -1, -1):
		res[i] *= tmp
		tmp *= array[i]
	return res


def solve4(array):
	'''
	time: O(n) * 1, without division
	space: O(n)
	'''
	n = len(array)
	left = right = 1
	res = [1] * n
	for i in range(n):
		res[i] *= left
		res[n - i - 1] *= right
		left *= array[i]
		right *= array[n - i - 1]
	return res

# assert solve([2, 3, 4, 5, 6]) == [360, 240, 180, 144, 120]
# assert solve([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
# assert solve([3, 2, 1]) == [2, 3, 6]
# assert solve([3]) == [1]
# assert solve([]) == []


