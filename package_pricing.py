n = input()
p1 = raw_input().split()
p2 = raw_input().split()
p3 = raw_input().split()
p4 = raw_input().split()
p5 = raw_input().split()
A = []
B = []
C = []
D = []
P = []
T = []
def app(str,A,B,C,D,P,T):
        if 'a' in str:
                i = str.index('a')
                A = A.append(str[i+1])
        else:
                A = A.append(0)
        if 'b' in str:
                j = str.index('b')
                B = B.append(str[j+1])
        else:
                B = B.append(0)
        if 'c' in str:
                k = str.index('c')
                C = C.append(str[k+1])
        else:
                C = C.append(0)
        if 'd' in str:
                m = str.index('d')
                D =  D.append(str[m+1])
        else:
                D = D.append(0)
        P = P.append(str[1])
        T = T.append(str[0])
        return A,B,C,D,T,P
app(p1,A,B,C,D,P,T)
app(p2,A,B,C,D,P,T)
app(p3,A,B,C,D,P,T)
app(p4,A,B,C,D,P,T)
app(p5,A,B,C,D,P,T)
A = list(map(int, A))
B = list(map(int, B))
C = list(map(int, C))
D = list(map(int, D))
P = list(map(float, P))
T = list(map(int, T))
l = []
customers = input()
for i in range(0,customers):
	x = int(input("a:"))
	y = int(input("b:"))
	z = int(input("c:"))
	t = int(input("d:"))
	l= []
        e = []
	i,j,k = 0,0,0
	while i < 5:
		if A[i] >= x and B[i] >= y and C[i] >= z and D[i] >= t:
			l.append(P[i])
                        e.append([P[i], T[i]])
		j = 0    
		while j < 5:
			if A[i]+A[j] >= x and B[i]+B[j] >= y and C[i]+C[j] >= z and D[i]+D[j] >= t:
  		   		l.append(P[i]+P[j])
                                e.append([P[i]+P[j], T[j], T[j]])
			k = 0
			while k < 5:
                        	if A[i]+A[j]+A[k] >= x and B[i]+B[j]+B[k] >= y and C[i]+C[j]+C[k] >= z and D[i]+D[j]+D[k] >= t:
					l.append(P[i]+P[j]+P[k])
                                        e.append([P[i]+P[j]+P[k], T[i], T[j], T[k]])
                        	m = 0
                        	while m < 5:
                        		if A[i]+A[j]+A[k]+A[m] >= x and B[i]+B[j]+B[k]+B[m] >= y and C[i]+C[j]+C[k]+C[m] >= z and D[i]+D[j]+D[k]+D[m] >= t:
						l.append(P[i]+P[j]+P[k]+P[m])
                                                e.append([P[i]+P[j]+P[k]+P[m], T[i], T[j], T[k], T[m]])
                                	m = m + 1

                        	k = k + 1
                	j = j + 1
        	i = i + 1
        v = l.index(min(l))
        print (e[v])
	
