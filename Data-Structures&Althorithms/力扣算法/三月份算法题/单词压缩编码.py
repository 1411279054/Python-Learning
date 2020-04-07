# -*- coding: utf-8 -*- 
# @Time : 2020-04-07 21:43 
# @Author : LiChao
# @File : 单词压缩编码.py

##存储后缀
class Solution:
    def minimumLengthEncoding(self, words: list) -> int:
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])
        return sum(len(word) + 1 for word in good)
def main():
    words = ["time", "me", "bell"]
    result = Solution().minimumLengthEncoding(words)
    print(result)
if __name__ == '__main__':
    main()