# 서울에서 김서방 찾기

# String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. 
# seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.



def solution(seoul):
    return f'김서방은 {seoul.index("Kim")}에 있다'
    
print(solution(["Jane", "Kim"])) # "김서방은 1에 있다"
print(solution(["Jane", 'hello', "Kim"]))
print(solution(["Jane", 'hello', 'hi', "Kim"]))

# for문을 굳이 쓸 일 없으면 안 써도 된다..;;ㅎㅎ