#去掉末尾空格，再计数。
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        cnt, tail = 0, len(s) - 1
        while tail >= 0 and s[tail] == ' ':
            tail -= 1
        while tail >= 0 and s[tail] != ' ':
            cnt += 1
            tail -= 1
        return cnt
#利用python内置函数split函数来求解
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s.split())==0:
            return 0
        else:
            return len(s.split()[-1])
