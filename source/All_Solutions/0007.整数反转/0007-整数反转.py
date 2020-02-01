class Solution:
    def reverse(self, x: int) -> int:
        flag = False  # 设置flag表示是否为负数
        if x < 0: 
            flag = True
            x = -x
        res = 0
        #  x  = 123 -> 12 ->  1
        # res =  3  -> 32 -> 321
        while x > 0:
            res = res * 10 + x % 10 
            x //= 10  
        if -2**31 <= res <= 2**31:
            return res if not flag else -res
        return 0