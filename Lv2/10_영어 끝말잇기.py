# 영어 끝말잇기
# (문제 생략)


def solution(n, words):
    used = []
    player = [0 for i in range(n)]

    for i in range(len(words)):
        used.append(words[i])
        player[i%n] += 1
        if i == len(words) -1:
            break
        else:
            if words[i+1] in used:
                return [(i+1)%n +1, player[(i+1)%n]+1]
                break
            elif used[i][-1] != words[i+1][0]:
                return [(i+1)%n +1, player[(i+1)%n]+1]
                break
                
    return [0,0]
    
    
print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", 
                   "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))