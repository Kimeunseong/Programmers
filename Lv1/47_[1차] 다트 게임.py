# [1차] 다트 게임
# (문제 생략)

def solution(dartResult):
    a = ''
    return a

print(solution('1S2D*3T')) # 37
print(solution('1D2S#10S')) # 9


# 아직 미완성..

dart = '1D2S3T*'
num = ''
point = 0
po = []

for i in range(len(dart)) : 
    # i 가 숫자일 경우,
    if dart[i] in '1234567890':
        num += dart[i]
        print(f'num_{dart[i]} = {num}')
        
    elif dart[i] == 'S':
        point += int(num) **1
        po.append(int(num) **1)
        print(f'{po}')
        print(f'point_{dart[i]} = {point}')
        if i == len(dart) -1:
            print('end')
            break
        elif dart[i+1] == '#':
            point += int(num) * (-2)
            print(f'point_{dart[i+1]} = {point}')
        elif dart[i+1] == '*' and dart[i+1] == len(dart) -1:
            point += int(num) * 2
        elif dart[i+1] == '*':
            point = point * 2
            print(f'point_{dart[i+1]} = {point}')
        num = ''
        
    elif dart[i] == 'D':
        point += int(num) **2
        po.append(int(num) **2)
        print(f'{po}')
        print(f'point_{dart[i]} = {point}')
        if i == len(dart) -1:
            print('end')
            break
        elif dart[i+1] == '#':
            point += (int(num) **2) * (-2)
            print(f'point_{dart[i+1]} = {point}')
        elif dart[i+1] == '*' and dart[i+1] == len(dart) -1:
            point += int(num) * 2
        elif dart[i+1] == '*':
            point = point * 2
            print(f'point_{dart[i+1]} = {point}')
        num = ''
        
    elif dart[i] == 'T':
        point += int(num) **3
        po.append(int(num) **3)
        print(f'{po}')
        print(f'point_{dart[i]} = {point}')
        if i == len(dart) -1:
            print('end')
            break
        elif dart[i+1] == '#':
            point += (int(num) **3) * (-2)
            print(f'point_{dart[i+1]} = {point}')
        elif dart[i+1] == '*' and dart[i+1] == len(dart) -1:
            point += int(num) * 2
        elif dart[i+1] == '*':
            point = point * 2
            print(f'point_{dart[i+1]} = {point}')
        num = ''


print()
print(po)
print(f'return = {point}')


