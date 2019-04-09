#这个解法的思想是动态规划，nums[i-1]并不是数组前一项的意思，而是到前一项为止的最大子序和，和0比较是因为只要大于0，就可以相加构造最大子序和。
#如果小于0则相加为0，nums[i]=nums[i]，相当于最大子序和又重新计算。其实是一边遍历一边计算最大序和。
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
         """
        for i in range(1, len(nums)):
            nums[i]= nums[i] + max(nums[i-1], 0)
        return max(nums)
        
