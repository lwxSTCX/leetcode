class Solution(object):
    def maxSubArray(self,nums):
        for i in range(1,len(nums)):
            nums[i]=nums[i]+max(nums[i-1],0)
            #动态规划
            #如果nums[i-0]大于0的话，新的nums[i]就是和前一项的和，否则就是自身
            #32 ms	13.5 MB
        return max(nums)

nums=[-2,1,-3,4,-1,2,1,-5,4]
solution=Solution()
result=solution.maxSubArray(nums)
print(result)


class Solution(object):
    def maxSubArray(self,nums):
        tmp=nums[0]
        max_=tmp
        n=len(nums)
        for i in range(1,n):
            #当当前序列加上此时的元素的值大于tmp的值，说明最大序列和可能出现在后续序列中，记录此时的最大值
            if tmp + nums[i] > nums[i]:
                max_ = max(max_,tmp+nums[i])
                tmp = tmp+nums[i]
            else:
            #当tmp(当前和)小于下一个元素时，当前最长序列到此为止。以该元素为起点继续找最大子序列,
            # 并记录此时的最大值
            #28 ms	13.2 MB
                max_=max(max_,tmp,tmp+nums[i],nums[i])
                tmp=nums[i]
        return max_

nums=[-2,1,-3,4,-1,2,1,-5,4]
solution=Solution()
result=solution.maxSubArray(nums)
print(result)












