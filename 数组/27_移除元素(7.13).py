# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#         l=[]
#         for i in range(len(nums)):
#             if nums[i] == val:
#                 pass
#             else:
#                 l.append(nums[i])
#         return len(l),l
#
#
# nums=[3,2,2,3]
# val=3
# solution=Solution()
# s=solution.removeElement(nums,val)
# print(s)


# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#         #采用倒序的话，不会影响前面的元素，就不会报错
#         #	20 ms	12.7 MB
#         for i in reversed(range(len(nums))):
#             if nums[i] == val:
#                 nums.pop(i)
#         return len(nums)
#
#
# nums=[3,2,2,3]
# val=3
# solution=Solution()
# s=solution.removeElement(nums,val)
# print(s)

# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#         #直接删除val值，惊为天人的解法
#         #	20 ms	12.7 MB
#         try:
#             while True:
#                 nums.remove(val)
#         except:
#             return len(nums)
#
#
# nums=[3,2,2,3]
# val=3
# solution=Solution()
# s=solution.removeElement(nums,val)
# print(s)

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #虽然没有移除元素，但是直接将值算出来了
        val_count=nums.count(val)
        return len(nums)-val_count

nums=[3,2,2,3]
val=3
solution=Solution()
s=solution.removeElement(nums,val)
print(s)
