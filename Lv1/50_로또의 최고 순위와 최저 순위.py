# 로또의 최고 순위와 최저 순위

# 민우가 구매한 로또 번호를 담은 배열 lottos, 당첨 번호를 담은 배열 win_nums가 매개변수로 주어집니다. 
# 이때, 당첨 가능한 최고 순위와 최저 순위를 차례대로 배열에 담아서 return 하도록 solution 함수를 완성해주세요.

def solution(lottos, win_nums):
    arr = []
    zeros, cnt = 0, 0
    
    for i in lottos:
        if i == 0: zeros += 1
        else: arr.append(i)
    for i in arr:
        if i in win_nums: cnt += 1

    if cnt == 0:
        return [6, 6] if zeros == 0 else [7 - (cnt + zeros), 6]
    else:
        return [7 - (cnt + zeros), 7 - cnt]

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])) # [3, 5]
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])) # [1, 6]
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])) # [1, 1]
print(solution([21, 10, 2, 44, 5, 36], [20, 9, 3, 45, 4, 35])) # [6, 6]