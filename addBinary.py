 #方法一，利用python的内置函数int和bin
 class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c =  int(a,2)+int(b,2)     #class int(x, base=10)  base表示进制数，默认为10
        return bin(c)[2:]          #bin(10),返回'0b1010',所以要从2开始，去掉0b
        
 #方法二，
