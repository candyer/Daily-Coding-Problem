
# Daily Coding Problem: Problem #1

# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?


def solve1(array, k):
	'''
	O(n^2)  burte force  
	'''
	n = len(array)
	for i in range(n):
		for j in range(i + 1, n):
			if array[i] + array[j] == k:
				return True
	return False


def solve2(array, k):
	'''
	O(nlogn)  two pointers  
	'''
	array.sort()
	left, right = 0, len(array) - 1
	while left < right:
		tmp = array[left] + array[right]
		if tmp == k:
			return True
		elif tmp > k:
			right -= 1
		else:
			left += 1
	return False


from collections import Counter as c
def solve3(array, k):
	'''
	O(n) * 2
	'''	
	nums = c(array)
	for key, val in nums.items():
		shortage = k - key
		if shortage == key:
			if val > 1:
				return True
			else:
				return False
		elif shortage in nums:
			return True
	return False


def solve4(array, k):
	'''
	O(n) * 1
	'''	
	nums = set()
	for num in array:
		if k - num in nums:
			return True
		nums.add(num)
	return False


# assert solve([10, 15, 3, 7], 20) == False
# assert solve([11, -20, 25, 7, 18, 20, 40, 11, 3, 0, 10, 9, 30, 9], 20) == True
# assert solve([10, 15, 3, 7], 17) == True
# assert solve([10, 15, 3, 100], 19) == False
# assert solve([3, 7, 9, 10, 11, 18, 19], 20) == True
# assert solve([3, 7, 9, 10, 11, 18, 19], 2) == False



