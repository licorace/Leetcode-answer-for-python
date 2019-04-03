class Solution:
    def twoSum(self, nums,target):
        if not nums:
            return None

        d = dict()
        for i, item in enumerate(nums):
            tmp = target - item
            if tmp in d:
                return sorted([i, d[tmp]])
            d[item] = i

        return None

if __name__ == '__main__':
    s = Solution()
    #s.twoSum(nums,target)
    print(s.twoSum([1,9,2,3,7,11,15],9))
