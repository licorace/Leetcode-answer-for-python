class Solution:
    def reverse(self, x):
        if x == 0:
            return 0
        else:
            x = str(x)
            i = len(x) - 1
            if x[0] == "-":
                y = x[i]
                while i > 1:
                    i = i - 1
                    y+=x[i]
                y = -int(y)
            else:
                y = x[i]
                while i > 0:
                    i = i -1
                    y+=x[i]
                y = int(y)
            if -2**31<=y<=2**31-1:
                return y
            else:
                return 0    
a = input()
s = Solution()
print(s.reverse(a))

    
