def gnomesort(a): ' a is a list of unsorted integers, for example [6,9,4,1,34]
	i,j,size = 1,2,len(a)
	while i < size:
		if a[i-1] <= a[i]:
			i,j = j, j+1
		else:
			a[i-1],a[i] = a[i],a[i-1]
			i -= 1
			if i == 0:
				i,j = j, j+1
	return a
