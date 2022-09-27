# 폰켓몬
# (문제생략)

def solution(nums):
    return len(list(set(nums))) if len(list(set(nums))) <= (len(nums)//2) else len(nums) // 2

    
# 테스트 확인용
print(solution([3,1,2,3])) # 2
print(solution([3,3,3,2,2,4])) # 3
print(solution([3,3,3,2,2,2])) # 2