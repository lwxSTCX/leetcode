# class Solution(object):
#     def searchInsert(self, nums, target):
#         #36 ms	14.4 MB
#         #自己做的，终于通过
#         if target in nums:
#             for i in range(len(nums)):
#                 while nums[i] != target:
#                     i+=1
#                 return i
#         else:
#             for i in range(len(nums)):
#                 if target>nums[-1]:
#                     return len(nums)
#                 if target<nums[0]:
#                     return 0
#                 while (nums[i]<target and nums[i+1]>target):
#                     return i+1
#
#
#
# nums=[1,3,5,6]
# target=7
# solution=Solution()
# result=solution.searchInsert(nums,target)
# print(result)


class Solution(object):
    def searchInsert(self, nums, target):
        #44 ms	14.4 MB
        #简单解法
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)

nums=[1,3,5,6]
target=7
solution=Solution()
result=solution.searchInsert(nums,target)
print(result)

class Solution(object):
    def searchInsert(self, nums, target):
        #	40 ms	14.2 MB
        #因为按题意要求，不存在重复项，所以插入排序取index值就行
        nums.append(target)
        nums.sort()
        return nums.index(target)

nums=[1,3,5,6]
target=7
solution=Solution()
result=solution.searchInsert(nums,target)
print(result)


class Solution(object):
    def searchInsert(self, nums, target):
        #用二分法做题
        #40 ms	14.4 MB
        left=0
        right=len(nums)-1
        while left <= right:
            mid=left+(right-left)//2
            if nums[mid] < target:
                left =mid +1
            elif nums[mid] > target:
                right =mid - 1
            else:
                return mid
        return left

nums=[1,3,5,6]
target=7
solution=Solution()
result=solution.searchInsert(nums,target)
print(result)










