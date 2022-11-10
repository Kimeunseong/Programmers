# [1차] 다트 게임
# (문제 생략)

def solution(dartResult):
    arr = ''
    point = []

    for i in dartResult : 
        if i.isdigit():
            arr += i
        elif i == 'S':
            point.append(int(arr)**1)
            arr = ''
        elif i == 'D':
            point.append(int(arr)**2)
            arr = ''
        elif i == 'T':
            point.append(int(arr)**3)
            arr = ''
        elif i == '#':
            point.append(point.pop()*(-1))
        elif i == '*':
            tmp = point[:-2]
            for i in point[-2:]:
                tmp.append(i*2)
            point = tmp
    
    return sum(point)
    

print(solution('1S2D*3T')) # 37
print(solution('1D2S#10S')) # 9
print(solution('1D2S0T')) # 3
print(solution('1S*2T*3S')) # 23
print(solution('1D#2S*3S')) # 5
print(solution('1T2D3D#')) # -4
print(solution('1D2S3T*')) # 59