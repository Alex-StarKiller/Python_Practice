def symmetric(lista):
	count = 0
	f = 0
	while f < len(lista):
		c = 0
		while c < len(lista):
			if lista[f][c] == lista[c][f]:
				count+=1
				c+=1
			else:
				c+=1
		f+=1
	if count == (len(lista) ** 2):
		return True
	else:
		return False







print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])
#>>> True

print symmetric([[1, 2],
                [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]])
#>>> False

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])