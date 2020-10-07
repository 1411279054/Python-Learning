# class Solution:
#     def isValidSudoku(self, board: list[list[str]]) -> bool:
#         result = True
#         matrix = [[] for i in range(1,10)] #创造九个向量：判断列是否满足条件
#         matrix_nine = [[] for i in range(1, 10)]  # 创造九个向量：判断九格是否满足条件
#         for i in board:
#             points = [] # 提取出每行点的数量
#             nums = [] # 提取出每列数字的数量
#             num = 0
#             for j in i:
#                 matrix[num].append(j)
#                 if j == ".":
#                     points.append(j)
#                 else:
#                     nums.append(j)
#                 num = num + 1
#             # 验证行是否满足条件
#             if len(set(nums)) + len(nums) < 9:
#                 result = False
#         if result == True:
#             for i in matrix:
#                 # 验证列是否成立
#                 col_points = []
#                 col_nums = []
#                 for j in i:
#                     if j == ".":
#                         col_points.append(j)
#                     else:
#                         col_nums.append(j)
#                 if len(set(col_nums)) + len(col_nums)<9:
#                     result = False
#         for row in range(1,9):
#             for col in range(1,9):
#                 i = (row // 3) * 3
#                 j = col//3

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # init data
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3

                    # keep the current cell value
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True
matrix = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

result = Solution().isValidSudoku(matrix)
print(result)