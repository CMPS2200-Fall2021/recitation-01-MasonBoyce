"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
			return -1

def test_linear_search():
	""" done. """
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1

def binary_search(mylist, key):
	ret = _binary_search(mylist, key, 0, len(mylist)-1)
	print("binary search answer",ret)
	return ret

def _binary_search(mylist, key, left, right):
	if left>right:
		return -1
	middleNum = (left+ right) //2
	if (mylist[middleNum] == key):
		#print(mylist[middleNum] == key)
		#print("in returning")
		#print("middleNum", middleNum)
		return middleNum
	elif (mylist[middleNum] > key and right>0):
		#print("in greater")
		return _binary_search(mylist,key,left,middleNum-1)
	elif (mylist[middleNum] < key and left<len(mylist)):
		#print("in less")
		return _binary_search(mylist,key,middleNum+1,right)
	else:
		return -1


		"""
		Recursive implementation of binary search.

		Params:
		mylist....list to search
		key.......search key
		left......left index into list to search
		right.....right index into list to search

		Returns:
		index of key in mylist, or -1 if not present.
		"""
		### TODO

		pass

def test_binary_search():
	assert binary_search([5,6,7,8,9,10],7) == 2
	assert binary_search([1,2,3,4,5], 5) == 4
	assert binary_search([1,2,3,4,5], 1) == 0
	assert binary_search([1,2,3,4,5], 6) == -1
	assert binary_search([5,6,7,8,9,10],7) == 2
	pass

print(binary_search([1,2,3,4,5], 5))
print(binary_search([5,6,7,8,9,10],7))

def time_search(search_fn, mylist, key):
	startTime = time.time()*1000
	search_fn(mylist,key)
	endTime = time.time()*1000
	totalTime = (endTime-startTime)
	return totalTime

	"""
	Return the number of milliseconds to run this
	search function on this list.

	Note 1: `sort_fn` parameter is a function.
	Note 2: time.time() returns the current time in seconds.
	You'll have to multiple by 1000 to get milliseconds.

	Params:
	sort_fn.....the search function
	mylist......the list to search
	key.........the search key

	Returns:
	the number of milliseconds it takes to run this
	search function on this input.
	"""
	### TODO
	pass

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	broad_list = []
	for i in sizes:
		i_list = []
		for j in range(i):
			i_list.append(j)
		binarySearchTime = time_search(binary_search,i_list,-1)
		linearSearchTime = time_search(linear_search,i_list,-1)
		broad_list.append([i,linearSearchTime,binarySearchTime])

	return broad_list

	"""
	Compare the running time of linear_search and binary_search
	for input sizes as given. The key for each search should be
	-1. The list to search for each size contains the numbers from 0 to n-1,
	sorted in ascending order.

	You'll use the time_search function to time each call.

	Returns:
	A list of tuples of the form
	(n, linear_search_time, binary_search_time)
	indicating the number of milliseconds it takes
	for each method to run on each value of n
	"""
	### TODO
	pass

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
	headers=['n', 'linear', 'binary'],
	floatfmt=".3f",
	tablefmt="github"))

def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print("res", res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1

test_compare_search()
test_binary_search()
