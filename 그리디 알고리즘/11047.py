#11047번
#input : 동전종류 N, 가치 합 K
#input2 : N개의 줄에 오름차순으로 동전 가치(원) 주어짐(N이 2이상이면 i번째 가치는 i-1번째의 배수)
#return : K원을 만드는데 필요한 동전 최소 개수

N,K = input().split(' ')
N,K = int(N),int(K)

values = []
for i in range(N):
    v = int(input())
    values.append(v)

count = 0
while K>0 or len(values)>=1:
    v = values[-1]
    share = K//v
    K %= v
    count+=share
    values.pop()
    print(f'몫 : {share} 남은 K : {K} values : {values}')

print(count)
