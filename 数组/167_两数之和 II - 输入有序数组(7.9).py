# class Solution(object):
#     def twoSum(self,nums,target):
#         #超时
#         for i in range(len(nums)):
#             for j in range(1,len(nums)):
#                 if i<j:
#                     if nums[i] + nums[j] == target:
#                         return i+1,j+1
#         return []
#
#
# nums=[1,2,3,4,4,9,56,90]
# target=8
# solution=Solution()
# result=solution.twoSum(nums,target)
# print(result)

# class Solution(object):
#     def twoSum(self,nums,target):
#         #双指针
#         #24 ms	13 MB
#         i=0
#         j=len(nums)-1
#         while i<j:
#             if nums[i]+nums[j]>target:
#                 j=j-1
#             elif nums[i]+nums[j]<target:
#                 i=i+1
#             else:
#                 break
#         return i+1,j+1
#
# nums=[1,2,3,4,4,9,56,90]
# target=8
# solution=Solution()
# result=solution.twoSum(nums,target)
# print(result)

# class Solution(object):
#     def twoSum(self,nums,target):
#         #用减法做
#         #可能存在相同元素啊，直接减就会有两个答案
#         #不行，两个0不好处理
#         #失败
#         for i in range(len(nums)):
#             temp=nums[i+1:]
#             j=target - nums[i]
#             if j in temp:
#                 k=nums.index(j)
#                 print(i,k+1)
#                 if i<k:
#                     return i+1,k+1
#                     break
#                 else:
#                     continue
#             else:
#                 continue
#
# nums=[0,0,3,4]
# target=0
# solution=Solution()
# result=solution.twoSum(nums,target)
# print(result)

# class Solution(object):
#     def twoSum(self,nums,target):
#         #用哈希做
#         #	16 ms	13.3 MB
#         hashset={}
#         for i in range(len(nums)):
#             if hashset.get(target-nums[i]) is not None:
#                 return (hashset.get(target-nums[i])+1,i+1)
#             hashset[nums[i]]=i
#
# nums=[0,0,3,4]
# target=0
# solution=Solution()
# result=solution.twoSum(nums,target)
# print(result)
#
# class Solution(object):
#     def twoSum(self,nums,target):
#         #用字典做
#         #24 ms	13.4 MB
#         #感觉跟hash解法差不多
#         #字典跟列表的区别就体现出来了，列表就存在两个答案，字典就是一个答案
#         dic={}
#         for i in range(len(nums)):
#             if (target-nums[i]) in dic:
#                 return dic[target-nums[i]]+1,i+1
#             else:
#                 dic[nums[i]]=i
#
# nums=[0,0,3,4]
# target=0
# solution=Solution()
# result=solution.twoSum(nums,target)
# print(result)
