# -*- coding: utf-8 -*- 
# @Time : 2020/2/18 0:00 
# @Author : LiChao
# @File : Z字形变换.py 

def convert(s: str, numRows: int) -> str:
    if numRows < 2: return s
    res = ["" for i in range(numRows)]
    i, flag = 0, -1
    for c in s:
        res[i] += c
        if i == 0 or i == numRows - 1: flag = -flag
        i += flag
    return "".join(res)
def main():
    s = "LEETCODEISHIRING"
    num = 3
    result = convert(s,num)
    print(result)
if __name__ == '__main__':
    main()