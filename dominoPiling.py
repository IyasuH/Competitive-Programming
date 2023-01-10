import math
def domino(m, n):
	rec = m*n
	dominoSize=2
	print(math.trunc(rec/dominoSize))
	return(math.trunc(rec/dominoSize))

x = input().split()
domino(int(x[0]),int(x[1]))