class Solution:
    def sortedSquares(self, A: list) -> list:
       for i in range(len(A)):
           if A[i] < 0:
               A[i] = A[i] * -1
           A[i] = A[i] * A[i]
       A.sort()
       return A
def main():
    A = [-4,-1,0,3,10]
    result = Solution().sortedSquares(A)
    print(result)
if __name__ == '__main__':
    main()