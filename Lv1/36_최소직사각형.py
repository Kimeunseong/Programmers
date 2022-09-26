# 최소직사각형 - 완전탐색
# 명함 지갑을 만드는 회사에서 지갑의 크기를 정하려고 합니다. 
# 다양한 모양과 크기의 명함들을 모두 수납할 수 있으면서, 작아서 들고 다니기 편한 지갑을 만들어야 합니다. 
# 이러한 요건을 만족하는 지갑을 만들기 위해 디자인팀은 모든 명함의 가로 길이와 세로 길이를 조사했습니다.

# 아래 표는 4가지 명함의 가로 길이와 세로 길이를 나타냅니다.
# 명함 번호	가로 길이	세로 길이
# 1	60	50
# 2	30	70
# 3	60	30
# 4	80	40

# 가장 긴 가로 길이와 세로 길이가 각각 80, 70이기 때문에 80(가로) x 70(세로) 크기의 지갑을 만들면 모든 명함들을 수납할 수 있습니다. 
# 하지만 2번 명함을 가로로 눕혀 수납한다면 80(가로) x 50(세로) 크기의 지갑으로 모든 명함들을 수납할 수 있습니다. 
# 이때의 지갑 크기는 4000(=80 x 50)입니다.

# 모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열 sizes가 매개변수로 주어집니다. 
# 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return 하도록 solution 함수를 완성해주세요.

def solution(sizes):
    temp_w = sizes[0][0]
    temp_h = sizes[0][1]

    for w, h in sizes:
        if temp_w >= w and temp_h >= h:
            p_left = [temp_w, temp_h]
        elif temp_w < w and temp_h >= h:
            p_left = [w, temp_h]
        elif temp_w >= w and temp_h < h:
            p_left = [temp_w, h]
        else:
            p_left = [w, h]

        if temp_w >= h and temp_h >= w:
            p_right = [temp_w, temp_h]
        elif temp_w < h and temp_h >= w:
            p_right = [h, temp_h]
        elif temp_w >= h and temp_h < w:
            p_right = [temp_w, w]
        else:
            p_right= [h, w]


        if sum(p_left) >= sum(p_right):
            temp_w = p_right[0]
            temp_h = p_right[1]
        else:
            temp_w = p_left[0]
            temp_h = p_left[1]

    return temp_w * temp_h
    
    
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]])) # 4000 (=80*50)
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])) # 120 (=8*15)
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])) # 133 (=8*15)

# 후기 : 허허.. 세상에.. 나는 이 문제를 이렇게 고생해서 풀었는데, 사람들 생각보다 쉽게 풀다니.,,,,,


# [220925] 추가 더 좋은 코드

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes) 
# 큰 수 중에 가장 큰 수 X 작은 수 중에 가장 큰 수 OMG.. 괜히 나는 이진 탐색에만 꽂혀서...ㅠㅜ

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]])) # 4000 (=80*50)
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])) # 120 (=8*15)
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])) # 133 (=8*15)