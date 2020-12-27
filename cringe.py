def cringe(word="cringe"):
	for i in word:
		print(i)
		if i == word[0]:
			cringe(word[1:])
cringe()
