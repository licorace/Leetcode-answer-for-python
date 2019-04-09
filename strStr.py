#方法一，用index或者find，这两个没有本质区别，而find在str不在string中会报一个异常，而find会直接返回-1，所以本题中选择用find
class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        return haystack.find(needle)
        
#方法二：暴力遍历算法，每次以needle的长度来遍历haystack，直到找到haystack中与needle相等的字符串，返回此时i的值
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        for i in range(len(haystack)):
            j = i + len(needle)
            if j<=len(haystack) and haystack[i:j] == needle:
                return i
        return -1
