# -*- coding: utf-8 -*- 
# @Time : 2020-04-08 8:45 
# @Author : LiChao
# @File : 可以被捕获的棋子数.py


### 参考官方题解
class Solution:
    def numRookCaptures(self, board: list) -> int:
        cnt,row,cow = 0,0,0
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    row,cow = i,j
        for i in range(4):
            step = 0
            while True:
                tx = row + step * dx[i]
                ty = cow + step * dy[i]
                if tx < 0 or tx >= 8 or ty < 0 or ty >= 8 or board[tx][ty] == "B":
                    break
                if board[tx][ty] == "p":
                    cnt += 1
                    break
                step += 1
        return cnt


def main():
    board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    result = Solution().numRookCaptures(board)
    print(result)
if __name__ == '__main__':
    main()
