#二分法
#参考网址：https://www.cnblogs.com/qlky/p/7735145.html
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        high = x
        low = 0
        while low < high:
            mid = low + (high - low)//2 
            if mid * mid > x:    #如果mid的平方在x的右边
                high = mid       #将mid的值赋给高值
            elif mid * mid < x:
                low = mid + 1    #如果mid的平方在x的左边，将mid值加一赋给低值
            else:
                return mid       #如果mid的平方恰好等于x，那恭喜我们找到了
        return low-1             #如果没有找到正好相等的值，只能把最逼近的低值输出，由于之前低值是mid加了一的，故这里减去1
