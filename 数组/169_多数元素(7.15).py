class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #因为一定有众数，且众数个数大于n/2，所以直接输出排序n/2位置的数即可
        #32 ms	13.8 MB
        #因为大于一半，所以排序后中间那个数就是众数
        nums.sort()
        return nums[int(len(nums)/2)]

nums=[3,2,3]
solution=Solution()
result=solution.majorityElement(nums)
print(result)














