#动态规划法，不难发现，这个问题可以被分解为一些包含最优子结构的子问题，即它的最优解可以从其子问题的最优解来有效地构建，我们可以使用动态规划来解决这一问题。
#第 ii 阶可以由以下两种方法得到：
#在第 (i-1)(i−1) 阶后向上爬一阶。
#在第 (i-2)(i−2) 阶后向上爬 22 阶。
#所以到达第 ii 阶的方法总数就是到第 (i-1)(i−1) 阶和第 (i-2)(i−2) 阶的方法数之和。
#令s[i]表示能到达第 ii 阶的方法总数：
#s[i]=s[i-1]+s[i-2] 
class Solution:
    def climbStairs(self, n: int) -> int:
        s = [1,1,2]
        if n <= 2:
            return n
        for i in range(3,n+1):
            s.append(s[i-1] + s[i-2])
        return s[i]

#斐波那契算法
class Solution:
    def climbStairs(self, n: int) -> int:
        a ,b = 1,2
        if n <= 2:
            return n
        while n-2:
            a,b = b,a+b
            n -= 1
        return b
            
