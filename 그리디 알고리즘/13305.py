#13305
#input : 도시 개수 N
#input2 : 인접한 도로끼리의 길이(왼쪽부터, 한줄로, N-1개)
#input3 : 도시별 리터당 가격(왼쪽부터, 한줄로, N개)
#return : 최소 비용

N = int(input())
lengths = input().split(' ')
prices = input().split(' ')

lengths = list(map(int, lengths))
prices = list(map(int, prices))

remained_length=sum(lengths)
min_gas_amount = lengths[0]

total_values = []

for p in range(len(prices)):
    min_gas_amount = lengths[p]
    print(f'{p}번째 도시 주유계산')
    for i in range(remained_length-min_gas_amount+1):
        print("현재 i : ",i)
        print(f'{prices[p]}*({remained_length}-{i})+{prices[p+1]}*{i} = {prices[p]*(remained_length-i)+prices[p+1]*i}, \n {prices[p]}*({remained_length}-{i}+1)+{prices[p+1]}*({i}+1) = {prices[p]*(remained_length-(i+1))+prices[p+1]*(i+1)}')
        if prices[p]*(remained_length-i)+prices[p+1]*i > prices[p]*(remained_length-(i+1))+prices[p+1]*(i+1):
            pass
        
        else:
            total_values.append(prices[p]*(remained_length-i))
            remained_length = i
            break
        
        if remained_length-i == min_gas_amount:
            total_values.append(prices[p]*(remained_length-i))
            remained_length = i
            break
        
    if remained_length <= 0:
        break

print(sum(total_values))

