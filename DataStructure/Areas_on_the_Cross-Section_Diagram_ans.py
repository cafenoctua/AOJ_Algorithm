if __name__ == '__main__':

	l = input()
	S1, S2 = [], []
	
	sum = 0
	n = len(l)
	for i in range(n):
		if l[i] == "\\":
			S1.append(i)
		elif l[i] == "/" and S1:
			j = S1.pop()
			a = i - j
			sum += a
	
			while S2 and S2[-1][0] > j:
				a += S2.pop()[1]
			S2.append([j, a])
	
	print(sum)
	print(len(S2), *(a for j, a in S2))