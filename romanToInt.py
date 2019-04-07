#这道题的关键在于先建立一个哈希表来映射符号和值，然后对字符串从左往右来遍历，如果当前字符代表的值小于其右边字符所代表的值，就减去该值，反之则加上该值
#需要注意的是最后一位右边没有值，所以无需判断，直接加上该值。
class Solution:
    def romanToInt(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}        
        ans=0        
        for i in range(len(s)):            
            if i<len(s)-1 and a[s[i]]<a[s[i+1]]:                
                ans-=a[s[i]]
            else:
                ans+=a[s[i]]
        return ans
        
        
