## 题目：旋转矩阵（）

import pandas
import copy
class Solution:
    ##利用pandas求解
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix2 = pandas.DataFrame(matrix)
        num = matrix2[0].size
        for i in range(num):
            matrix[i] =matrix2[i].values.tolist()
            matrix[i].reverse()
        print(matrix)
    ##辅助函数
    def rotate2(self, matrix:list):
        """
        Do not return anything, modify matrix in-place instead.
        """
        num = 0
        matrix2 = [[0]*len(matrix) for i in range(len(matrix))] ## 生成相同维度的二维矩阵
        while num < len(matrix2):
            for i in range(len(matrix)):
                matrix2[i][len(matrix)-num-1] = matrix[num][i]
            num += 1
        matrix[:] = matrix2 #重点
        print(matrix)
        ## 辅助函数+深拷贝
    def rotate3(self, matrix: list) -> None:
                """
                Do not return anything, modify matrix in-place instead.
                """
                num = 0
                matrix2 = copy.deepcopy(matrix)  ## 注意是深拷贝（区别 深拷贝和浅拷贝）
                while num < len(matrix2):
                    for i in range(len(matrix)):
                        matrix[i][len(matrix) - num - 1] = matrix2[num][i]
                        print(matrix[i][len(matrix) - num - 1] )
                    num += 1
                print(matrix)





def main():
    matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
    Solution().rotate3(matrix)
if __name__ == '__main__':
    main()