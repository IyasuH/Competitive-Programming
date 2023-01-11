def printf(arr):
	for x in range(len(arr)):
		print(arr[x], end=" ")
	print("\n", end="")
def insertSort(n, arr):
	ini = n-1
	for x in range(n):
		civ  = arr[ini]
		# n-=1
		# print(arr[-(x+1)])
		if civ < arr[-(x+1)]:
			temp = arr[ini]
			arr[ini] = arr[-(x+1)]
			printf(arr)
			arr[-(x+1)] = temp
			ini-=1
	printf(arr)

insertSort(5, [2, 4, 6, 8, 3])