# 크레인 인형뽑기 게임

# (문제 생략)
# 게임 화면의 격자의 상태가 담긴 2차원 배열 board와 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves가 매개변수로 주어질 때, 
# 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return 하도록 solution 함수를 완성해주세요.

def solution(board, moves):
    
    basket = []
    count = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                if len(basket) == 0:   # 바구니가 비어있을 경우, 뽑은 인형을 그냥 바구니에 넣는다.
                    basket.append(board[j][i-1])
                    board[j][i-1] = 0 # 인형을 뽑고 빈 자리에는 0을 채워넣는다.
                    break
                elif basket[-1] == board[j][i-1]: # 이전에 채운 인형과 같은 인형이 들어올 경우,
                    basket.pop()   # 이전에 채운 값을 삭제
                    board[j][i-1] = 0 # 인형을 뽑고 빈 자리에는 0을 채워넣는다.
                    count += 2   # 인형이 2개 사라짐.
                    break
                else:
                    basket.append(board[j][i-1]) 
                    board[j][i-1] = 0
                    break
    return count
    
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))