#方法一：暴力破解，没啥好说的，代码易懂但时间复杂度高
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        for i in range(len(nums) - 1):
            if nums[i] < target and target < nums[i+1]:
                return i+1
 #方法二，用了一点技巧，先把目标值插入，再排序，最后输出下标索引 
 class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
 #方法三，二分法，时间复杂度较低，程序运行更快
 class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)
        while low < high:
            mid = low + (high - low)//2
            if nums[mid] > target:
                high = mid
            elif nums[mid] < target:
                low = mid +1
            else:
                return mid
        return low
        
 
        
