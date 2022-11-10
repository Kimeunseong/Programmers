# [카카오 인턴] 키패드 누르기

# 순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 
# 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.

def solution(numbers, hand):

    answer = ''

    pad = {1:[0,0], 2:[0,1], 3:[0,2],
           4:[1,0], 5:[1,1], 6:[1,2],
           7:[2,0], 8:[2,1], 9:[2,2],
           '*':[3,0], 0:[3,1], '#':[3,1]}

    target_left = [3,0]
    target_right = [3,1]

    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            target_left = pad[i]
        elif i in [3, 6, 9]:
            answer += 'R'
            target_right = pad[i]
        else:
            target = pad[i]
            cntL = abs(target_left[0] - target[0]) + abs(target_left[1] - target[1])
            cntR = abs(target_right[0] - target[0]) + abs(target_right[1] - target[1])
            if cntL < cntR:
                answer += 'L'
                target_left = pad[i]
            elif cntL > cntR:
                answer +='R'
                target_right = pad[i]
            else:
                if hand == 'left':
                    answer += 'L'
                    target_left = pad[i]
                else:
                    answer += 'R'
                    target_right = pad[i]
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")) # "LRLLLRLLRRL"
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")) # "LRLLRRLLLRR"
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")) # "LLRLLRLLRL"

# => 테스트 2, 8, 12, 17, 18 실패...