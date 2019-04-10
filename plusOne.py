#方法一，和方法二思路没什么区别，只是将列表转化为整数的方法不一样
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = 0
        for i in digits:
            s *= 10
            s += i
        res = s + 1
        return [int(x) for x in str(res)]

#方法二
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''
        for i in digits:
            num += str(i)
        res = int(num) + 1
        return [int(x) for x in str(res)]
        
