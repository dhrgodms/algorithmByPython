n = int(input())
list1 = list(int(input()) for _ in range(n))
list1.sort()
for i in list1:
    if list1.count(i)>1:
        list1.remove(i)
for i in list1:
    print(i)
'''
28에 프로젝트 끝
활동 보고는 간단하게 이메일로 
굳이 학교에 안나와도 됨
마지막주는 오프라인
010-9450-2031(이광용)

3일까지 프로젝트 제안서 작성하여 제출
주간활동 보고서 계속 써야 됨
10
17
24

'''