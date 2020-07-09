class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=list(set(nums))
        return (int((len(a))),a)

nums = [1,1,2]
solution=Solution()
print(solution.removeDuplicates(nums=nums))


class Solution(object):
    def removeDuplicates(self, nums):
        #双指针解法
        #28 ms	14 MB
        i=0
        j=1
        while j<len(nums):
            if nums[i]!=nums[j]:
                nums[i+1]=nums[j]
                i+=1
            else:
                j+=1

        return i+1

nums = [0,0,1,1,1,2,2,3,3,4]
solution=Solution()
print(solution.removeDuplicates(nums=nums))

class Solution(object):
    def removeDuplicates(self, nums):
        #反向遍历,倒着走
        #36 ms	14.5 MB
        for num_index in range(len(nums)-1,0,-1):
            if nums[num_index] == nums[num_index-1]:
                nums.pop(num_index)
        return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
solution=Solution()
print(solution.removeDuplicates(nums=nums))

class Solution(object):
    def removeDuplicates(self, nums):
        #两个一组扫描数组
        #48 ms	14.1 MB
        i,j=0,1
        while j<len(nums):
            if nums[i] == nums[j]:
                nums.pop(j)
            else:
                i+=1
                j+=1
        return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
solution=Solution()
print(solution.removeDuplicates(nums=nums))


