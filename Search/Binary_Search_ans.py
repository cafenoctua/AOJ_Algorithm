def binarySearch(A, n, key):
	
	left = 0
	right = n
	while (left < right):
		mid = (left + right) // 2
		if (key == A[mid]):
			return 1
		if (key > A[mid]):
			left = mid + 1
		elif (key < A[mid]):
			right = mid
	
	return 0

if __name__ == '__main__':
	
	n = int(input())
	L = list(map(int, input().split()))

	q = int(input())
	Key = list(map(int, input().split()))

	cnt = 0
	for i in range(q):
		if (binarySearch(L, n, Key[i])):
			cnt += 1

	print(cnt)