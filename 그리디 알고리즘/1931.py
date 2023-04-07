#1931번
#input : 회의개수 N
#input2 : N개의 줄에 회의 시작시간, 끝나는시간(둘이 같을 수 있음)
#return : 사용가능한 회의 최대개수

N = int(input())

meeting = []
for i in range(N):
    start, end = input().split(' ')
    start, end = int(start), int(end)
    meeting.append([end-start, start,end])

min_start = min(meeting)[1]
max_end = max(meeting)[2]
meeting.sort(key=lambda x: x[0])
remained = [[min_start, max_end]]

count = 0
t_end = 0

new_meeting = {}
for t,s,e in meeting:
    if t not in new_meeting.keys():
        new_meeting[t] = [[s,e]]
    else:
        new_meeting[t] += [[s,e]]

count = 0
t_end = 0
for t in new_meeting.keys():
    values = new_meeting[t]
    values.sort(key=lambda x: x[0])
    
    for s,e in values:
        for [min_start, max_end] in remained:
            if s>=min_start and e<=max_end:
                count +=1
                taking_s = s-min_start
                if taking_s > t:
                    min_start = s
                taking_e = max_end-e
                
            
                
    

        
        
# =============================================================================
# count = 0
# t_end = 0
# for taking, start, end in meeting:
#     if start >= t_end:
#         count+=1
#         t_end = end
# print(count) 
# =============================================================================
