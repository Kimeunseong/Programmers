# 두 개 뽑아서 더하기

# 정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 
# 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

def solution(numbers):
    lst = []
    
    for i in range(len(numbers)):
        for j in numbers[i+1:]:
            if (numbers[i]+j) in lst:
                pass
            else:
                lst.append(numbers[i]+j)
    
    return sorted(lst)
    
print(solution([2,1,3,4,1])) # [2,3,4,5,6,7]
print(solution([5,0,2,7])) # [2,5,7,9,12]