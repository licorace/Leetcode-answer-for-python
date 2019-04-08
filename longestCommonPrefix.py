#方法一：
#1、利用python的max()和min()，在Python里字符串是可以比较的，按照ascII值排，举例abb， aba，abac，最大为abb，最小为aba,
#即比较的是每一个字符的大小，如果当前位置字符已经比较出大小，则不必再进行下一位的比较
#所以只需要比较最大最小的公共前缀就是整个数组的公共前缀
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i, item in enumerate(s1):
            if item != s2[i]:
                return s2[:i]
        return s1

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(['javk','jacjkk','jacghhj']))
    
#方法二：    
#利用python的zip函数，把str看成list然后把输入看成二维数组，左对齐纵向压缩，然后把每项利用集合去重，
#之后遍历list中找到元素长度大于1之前的就是公共前缀
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:return ""
        ss = list(map(set,zip(*strs)))
        res = ''
        for i,item in enumerate(ss):
            x = list(item)
            if len(x) > 1:
                break
            res = res + x[0]
        return res
        
