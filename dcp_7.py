# Daily Coding Problem: Problem #7

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.


# def create_dict():
# 	d = {}
# 	for i in range(97, 97 + 26):
# 		d[chr(i)] = i - 96
# 	return d


# def create_dict():
# 	d = {}
# 	for i in range(97, 97 + 26):
# 		d[str(i - 96)] = chr(i)
# 	return d
# d = create_dict()


# according to problem description, I assume "00" will not be in the message. 
# and "0" will not be the first element in the message, or last if the second last is >= "3".
# "102030" is impossible but "10203" would be possible 

#################################################################################
def rec(message):
	n = len(message)
	if n <= 1:
		return 1
	if message[0] == '0':
		rec(message[1:])
	elif message[1] == '0':
		rec(message[2:])
	elif n > 2 and message[2] == '0':
		return rec(message[2:])
	elif 0 < int(message[0:2]) < 27:
		return rec(message[1:]) + rec(message[2:])
	return rec(message[1:])

assert rec('') == 1
assert rec('120') == 1
assert rec('1203') == 1
assert rec('10') == 1 
assert rec('1212') == 5
assert rec('12121') == 8
assert rec('10203') == 1
assert rec('110203') == 1
assert rec('2516') == 4
assert rec('1111') == 5
assert rec('2561') == 2
assert rec('111') == 3



#################################################################################
def rec(message):
	if len(message) <= 1:
		return 1
	if 0 < int(message[0:2]) < 27:
		return rec(message[1:]) + rec(message[2:])
	return rec(message[1:])

def solve(message):
	res, start, flag = 1, 0, True
	for i, c in enumerate(message + '10'):
		if c == '0':
			flag = False
			res *= rec(message[start:i - 1])
			start = i + 1
	if flag:  # no '0' in the message
		return rec(message)	
	return res

assert solve('1102033333') == 1
assert solve('12021023456') == 2
assert solve('1020222') == 3
assert solve('1212') == 5
assert solve('12121') == 8
assert solve('10203') == 1
assert solve('110203') == 1
assert solve('2516') == 4
assert solve('1111') == 5
assert solve('2561') == 2
assert solve('111') == 3

