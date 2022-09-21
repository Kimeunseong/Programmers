# 최대공약수와 최소공배수

# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 
# 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 
# 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

def solution(n, m):
    a = m if n > m else n
    max_factor = max([i for i in range(1, a+1) if n % i == 0 and m % i == 0])
    
    min_mul = int(max_factor * (n/max_factor) * (m/max_factor))
    return [max_factor, min_mul]
    
print(solution(3, 12)) # [3, 12]
print(solution(2, 5)) # [1, 10]

# 추가 : 다른 사람들 풀이 보니 유클리도 호재법? 이거 많이 써서 풀던데 나중에 한번 이걸로 해보자.