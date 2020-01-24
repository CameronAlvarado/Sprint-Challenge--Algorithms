'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
	L1 = len(word)
	L2 = len("th")

	if (L1 == 0 or L1 < L2):
		return 0

	if (word[0 : L2] == "th"):
		return count_th(word[L2 - 1:]) + 1

	return count_th(word[L2 - 1:])


print(count_th("thanosthinks"))
# should return 2