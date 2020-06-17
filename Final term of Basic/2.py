N=int(input())
for i in range(1,N+1):
    j=N-i
    for _ in range(0,j):
        print(' ',end='')
    for _ in range(0,i):
        print('*',end='')
    print()
