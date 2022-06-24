def sort(lst):
	lst.sort(key = str)
	return lst

lst = ['l', 5, 'd', 3, 'g', 7, 0, 'u']
print(sort(lst))