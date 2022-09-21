# 자연수 뒤집어 배열로 만들기

# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

def solution(n):
    lst1 = list(str(n))
    lst2 = []
    for i in lst1[::-1]:
        lst2.append(int(i))
    return lst2
    
num = 12345
print(solution(num))