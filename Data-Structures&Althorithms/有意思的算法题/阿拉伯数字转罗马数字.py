# -*- coding: utf-8 -*- 
# @Time : 2020/2/29 22:40 
# @Author : LiChao
# @File : 阿拉伯数字转罗马数字.py 

    #自己写的垃圾代码
    # def intToRoman(self, num: int) -> str:
    #     result= ""
    #     while num > 0:
    #         if num >= 1000:
    #             num -=1000
    #             result +="M"
    #         elif num >= 900:
    #             num -= 900
    #             result +="CM"
    #         elif num >= 500:
    #             num -= 500
    #             result +='D'
    #         elif num >= 400:
    #             num -= 400
    #             result +='CD'
    #         elif num >= 100:
    #             num -= 100
    #             result +='C'
    #         elif num >= 90:
    #             num -= 90
    #             result += 'XC'
    #         elif num >= 50 :
    #             num -= 50
    #             result +='L'
    #         elif num >= 40:
    #             num -=40
    #             result +='XL'
    #         elif num >= 10:
    #             num -=10
    #             result +='X'
    #         elif num >= 9:
    #             num -= 9
    #             result += 'IX'
    #         elif num >= 5:
    #             num -=5
    #             result +='V'
    #         elif num >= 4:
    #             num -= 4
    #             result += 'IV'
    #         elif num >= 1:
    #             num -=1
    #             result +='I'
    #     return result
class Solution:
        def intToRoman(self, num: int) -> str:
            # 把阿拉伯数字与罗马数字可能出现的所有情况和对应关系，放在两个数组中
            # 并且按照阿拉伯数字的大小降序排列，这是贪心选择思想
            nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
            romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

            index = 0
            res = ''
            while index < 13:
                # 注意：这里是等于号，表示尽量使用大的"面值"
                while num >= nums[index]:
                    res += romans[index]
                    num -= nums[index]
                index += 1
            return res
def main():
    num = 20
    answer = Solution().intToRoman(num)
    print(answer)
if __name__ == '__main__':
    main()