# class Solution(object):
#     def merge(self,nums1,m,nums2,n):
#         s=[]
#         for i in range(len(nums1)):
#             if nums1[i] != 0:
#                 s.append(nums1[i])
#         for j in range(len(nums2)):
#             if nums2[j] != 0:
#                 s.append(nums2[j])
#         return sorted(s)
#
#
# nums1=[1,2,3,0,0,0]
# m=3
# nums2 = [2,5,6]
# n = 3
# solution=Solution()
# result=solution.merge(nums1,m,nums2,n)
# print(result)

class Solution(object):
    def merge(self,nums1,m,nums2,n):
        #直接合并两个数组再排序
        #24 ms	12.7 MB
        nums1[:]=sorted(nums1[:m]+nums2)
        '''
        我们需要辨析：nums1 = A和nums1[:] = A的不同之处：
        nums1 = A  # 更改 nums1 这一变量名所指向的对象。让 nums1 变量指向 A 所指向的对象
        nums1[:] = A  # 对 nums1 指向的对象赋值。把 A 变量指向的对象的值逐个 copy 到 nums1 指向的对象中并覆盖 nums1 指向的对象的原来值。
        nums1[:]等价于nums1[0:len(nums1)],相当于取nums1对应的对象的一个视图，通常用这个来改变原对象的某几位值。
        比如有时候，我们用A[:2] = [0, 1], 来改变A所指向的list对象的前两个值。
        而如果用A = [0, 1], 则是让A这一变量名指向新的list对象[0, 1]
        '''
        return nums1

nums1=[1,2,3,0,0,0]
m=3
nums2 = [2,5,6]
n = 3
solution=Solution()
result=solution.merge(nums1,m,nums2,n)
print(result)



