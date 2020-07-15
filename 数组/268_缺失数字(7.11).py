# class Solution(object):
#     def missingNumber(self, nums):
#         for i in range(len(nums)):
#             temp=sorted(nums)
#             if int(int(temp[i])+1) == int(temp[i+1]):
#                 continue
#             else:
#                 return temp[i]+1
#                 break
# nums=[9,6,4,2,3,5,7,0,1]
# solution=Solution()
# result=solution.missingNumber(nums)
# print(result)

# class Solution(object):
#     def missingNumber(self, nums):
#         #44 ms	13.1 MB
#         nums.sort()
#         print(nums)
#         for i in range(len(nums)):
#             if nums[i] == i:
#                 continue
#             else:
#                 return i
#         return i+1
# nums=[9,6,4,2,3,5,7,0,1]
# solution=Solution()
# result=solution.missingNumber(nums)
# print(result)

class Solution(object):
    def missingNumber(self, nums):
        #哈希表
        #因为缺了一个数，将两个数组进行比较，如果有一个数在这里面，确不在另一个里面，则返回
        #32 ms	14 MB
        num_set=set(nums)
        n=len(nums)+1
        for number in range(n):
            if number not in num_set:
                return number
nums=[9,6,4,2,3,5,7,0,1]
solution=Solution()
result=solution.missingNumber(nums)
print(result)


class Solution(object):
    def missingNumber(self, nums):
        #如果直接赋值列表，
        #2288 ms	13.1 MB，所以还是要通过set处理下
        num_set=nums
        n=len(nums)+1
        for number in range(n):
            if number not in num_set:
                return number
nums=[9,6,4,2,3,5,7,0,1]
solution=Solution()
result=solution.missingNumber(nums)
print(result)









