 #方法一，利用python的内置函数int和bin
 class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c =  int(a,2)+int(b,2)     #class int(x, base=10)  base表示进制数，默认为10
        return bin(c)[2:]          #bin(10),返回'0b1010',所以要从2开始，去掉0b
        
 #方法二，先把字符串反转，补零使其对齐，然后逐位相加，逢二进一，再把最后得到的数逆序输出
 class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a[::-1]    #字符串逆序
        b = b[::-1]    #字符串逆序
        c = str()      #初始化一个空字符串
        up = 0         #进位数先设为0
        a += '0'*max(0, len(b)-len(a))   #补零使a，b对齐
        b += '0'*max(0, len(a)-len(b))   #补零使a，b对齐
        for i in range(len(a)):
            sum = int(a[i]) + int(b[i]) + up   #a的数加上b的数再加上进位数
            if sum == 3:
                c += '1'                       #该位为1
                up = 1                          
            elif sum == 2:
                c += '0'
                up = 1
            else:
                c += str(sum)
                up = 0
        if up:
            c += str(up)            #如果循环结束之后进位数还不为0的话，说明需要再补充一个进位
        return c[::-1]
