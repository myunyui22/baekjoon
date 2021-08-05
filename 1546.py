N = input()
current_grade = input().split()
current_grade_int = list(map(int,current_grade))
M = max(current_grade_int)
after_grade=[]
for i in range(int(N)):
    after_grade.append(current_grade_int[i]/M*100)
after_average = sum(after_grade)/float(N)
print(after_average)