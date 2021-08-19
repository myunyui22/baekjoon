def backTranking(depth):
    global N,M,arr
    if depth == M:
        print(' '.join(map(str, arr)))
        return
    
    for j in range(1,N+1):
        arr.append(j)
        backTranking(depth+1)
        arr.pop()
        
N=M=0

N,M = map(int, input().split())
arr = []
result = []
backTranking(0)

