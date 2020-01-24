'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
	count = 0
	if not word:
		print("count a:", count)
		return count
	else:
		x = word.find("th")
		if x is not None:
			count += 1
			print("count b:", count)
			print("word:", word)
			return count_th(word[x + 3:])
			# must add the result of recursive call to count
		else:
			print("count c:", count)
	return count

	# count = 0
	# L = len(word)
	# if not word:
	# 	print("is None")
	# 	return count
	# elif word is "th":
	# 	print(word[0])
	# 	count += 1
	# 	return count
	# else:
	# 	print(word)
	# 	print(count)
	# 	return count_th(word[1:])

count_th("thanosthinks")