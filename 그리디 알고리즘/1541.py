#1541
#input : 0~9,+,-로만 이루어진 식(숫자는 0으로 시작할 수 있음)
#return : 여러개의 괄호를 사용하여 최소화 할 수 있는 식의 값

cal = list(input())
max_parenthesis = sum([1 for i in cal if i=='+' or i=='-'])

