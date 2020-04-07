# -*- coding: utf-8 -*- 
# @Time : 2020-04-07 20:42 
# @Author : LiChao
# @File : 水壶问题.py 

## 水壶问题（365）

##自己错误题解
import math
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        diff = abs(x-y) # 两水壶的差值
        if diff == z or 2*diff == z or x == z or y == z :
            return True
        else:
            return False
### DFS
    def canMeasureWater2(self, x: int, y: int, z: int) -> bool:
            stack = [(0, 0)]
            self.seen = set()
            while stack:
                remain_x, remain_y = stack.pop()
                if remain_x == z or remain_y == z or remain_x + remain_y == z:
                    return True
                if (remain_x, remain_y) in self.seen:
                    continue
                self.seen.add((remain_x, remain_y))
                # 把 X 壶灌满。
                stack.append((x, remain_y))
                # 把 Y 壶灌满。
                stack.append((remain_x, y))
                # 把 X 壶倒空。
                stack.append((0, remain_y))
                # 把 Y 壶倒空。
                stack.append((remain_x, 0))
                # 把 X 壶的水灌进 Y 壶，直至灌满或倒空。
                stack.append((remain_x - min(remain_x, y - remain_y), remain_y + min(remain_x, y - remain_y)))
                # 把 Y 壶的水灌进 X 壶，直至灌满或倒空。
                stack.append((remain_x + min(remain_y, x - remain_x), remain_y - min(remain_y, x - remain_x)))
            return False

### 数学知识 贝祖定理
    def canMeasureWater3(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if x == 0 or y == 0 :
            return z == 0 or x + y == z
        return z % math.gcd(x,y) == 0
def main():
    x,y = 0,0
    z = 1
    result = Solution().canMeasureWater(x,y,z)
    print(result)
if __name__ == '__main__':
    main()
