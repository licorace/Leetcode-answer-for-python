#这个方法十分暴力，但是很简单，对于正确的来说，每一次都能去掉一个括号，最后就成了空，就拿举例来说，先去掉[],再去掉(),最后去掉{}
class Solution:
    def isValid(self, s: str) -> bool:
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''  #这一步是判断s是否为空，是的话返回True，不是的话返回False

if __name__ == '__main__':
    s = Solution()
    print(s.isValid('{([])}'))
