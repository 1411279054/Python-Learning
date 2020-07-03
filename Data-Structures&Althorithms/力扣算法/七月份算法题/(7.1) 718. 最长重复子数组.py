class Solution:
    def findLength(self, A: list, B: list) -> int:
        length_A,length_B = len(A),len(B)
        num = list()
        for i in range(length_A):
            num.append(A[i])
            for j in num:
                if j not in B:
                    num.clear()
        return len(num)
def main():
    A = [1, 2, 3, 2, 1]
    B = [3, 2, 1, 4, 7]
    result = Solution().findLength(A,B)
    print(result)
if __name__ == '__main__':
    main()