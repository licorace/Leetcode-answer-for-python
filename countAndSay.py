#根据前一个字符串的情况计算出下一个字符串的情况，核心思想就是比较相邻的两个字符是否是连续的数字。不是连续的基础计数就不加一。
#两个循环，第一个循环是从第三个数推进到第n个数，第二个循环是将每个整数所对应的的报数序列加入到报数序列池中
class Solution:
    def countAndSay(self, n: int) -> str:
        lst = ['1', '11', '21']  #这里写了三个，你也可以写两个或者四个，都可以
        if n <= 3:
            return lst[n-1]      #当n <= 3时，不用想，直接干
        for i in range(3, n):
            before = str(lst[i-1])  #这里我们提取前一个字符串
            base_num = 1            #计数为1
            base = ''
            for j in range(1, len(before)):
                if before[j] == before[j-1]:    #从首位开始判断相邻两位是否相等
                    base_num += 1               #如果相等则计数加一
                else:
                    base = base + str(base_num) + str(before[j-1])  #如果相邻两位不相等，先把第一位数字报出来，当再次循环到这步时，把j所在位置数报出来
                    base_num = 1                                    #计数初始化为1
            base = base + str(base_num) + str(before[j])           #将最后一位数报出来
            lst.append(base)                                       #将字符串添加到lst数据池里
        return lst[n-1]                        
        
       
