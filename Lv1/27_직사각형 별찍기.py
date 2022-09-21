# 직사각형 별찍기

# 이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.
# 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

n, m = map(int, input().strip().split(' '))  # 표준 입력 시 이렇게 입력하자.
        
count = 0
while count != n*m:
    print('*', end = '')
    count += 1
    if count%n == 0:
        print()
        
# 더 짧고 빠른 알고리즘
n, m = map(int, input().strip().split(' '))  # 표준 입력 시 이렇게 입력하자.

print(('*'*n + '\n')*m)