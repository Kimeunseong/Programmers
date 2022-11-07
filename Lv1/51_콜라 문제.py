# 콜라 문제

# 콜라를 받기 위해 마트에 주어야 하는 병 수 a, 빈 병 a개를 가져다 주면 마트가 주는 콜라 병 수 b, 
# 상빈이가 가지고 있는 빈 병의 개수 n이 매개변수로 주어집니다. 
# 상빈이가 받을 수 있는 콜라의 병 수를 return 하도록 solution 함수를 작성해주세요.

def solution(a, b, n):
    cnt = 0
    p = n
    while n >= a:
        p -= n - n%a
        cnt += (n - n%a)*b/a
        p += (n - n%a)*b/a
        n = p
        
    return int(cnt)
    
print(solution(2, 1, 20))
print(solution(3, 1, 20))