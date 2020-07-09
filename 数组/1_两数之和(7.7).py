class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #	运行时长5332ms 内存消耗13.5 MB
        for i in range(len(nums)):
            j=i+1
            while 1:
                if nums[i]+nums[j] == target:
                    return i,j
                else:
                    j+=1
                    if j>len(nums):
                        break

class Solution(object):
    def twoSum(self, nums, target):
        #直接双层循环
        #	运行时间3156 ms	内存消耗13.5 MB
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] ==target:
                    return i,j
        return []

class Solution(object):
    def twoSum(self, nums, target):
        #采用排序加双指针
        #52 ms	14.7 MB
        temp=nums.copy() #复制一个浅复制
        temp.sort()
        i=0
        j=len(nums)-1
        while i<j:
            if (temp[i]+temp[j])>target:
                j=j-1
            elif (temp[i]+temp[j])<target:
                i=i+1
            else:
                break
        p=nums.index(temp[i]) #Python index() 方法检测字符串中是否包含子字符串 str
        nums.pop(p) #pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
        k=nums.index(temp[j])
        #从这儿开始，有点没懂什么意思
        if k>=p:
            k=k+1
        return [p,k]

class Solution(object):
    def twoSum(self, nums, target):
        #哈希做
        #	72 ms	15 MB
        #看的一脸懵逼
        haseset={}
        for i in range(len(nums)):
            if hashset.get(target-nums[i]) is not None:
                return [haseset.get(target-nums[i]),i]
            haseset[nums[i]]=i

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
        #64 ms	15.2 MB
        dic = {}
        for k, v in enumerate(nums):
            if target - v in dic:  # 写之前判断，避免了重复元素的覆盖
                return [dic[target - v], k]
            dic[v] = k #一开始d为空，else之后会给字典赋键值

class Solution:
    def twosum(self,nums,target):
        #直接用target 减去 取出的数字，看结果有没有在数组里
        #760 ms	13.5 MB
        n=len(nums)
        for x in range(n):
            a=target - nums[x]
            if a in nums:
                y=nums.index(a)
                if x == y:
                    continue
                else:
                    return x,y
                    break
            else:
                continue

class Solution:
    def twosum(self,nums,target):
        #用字典提高速度，将原先的数组转化为字典，通过字典去查询速度会快很多
        d={}
        n=len(nums)
        for x in range(n):
            d[nums[x]]=x #把数组中的数字看做key,下标作为value存在d字典中
            if target - nums[x] in d: #看另一个数字有没有在字典中，但是target-nums[x]的值很可能等于num[x]，所有还要改进一下
                return d[target-nums[x]],x

class Solution:
    def twosum(self,nums,target):
        #用字典提高速度，将原先的数组转化为字典，通过字典去查询速度会快很多
        d={}
        n=len(nums)
        for x in range(n):
            if target - nums[x] in d:
                return d[target-nums[x]],x
            else:
                d[nums[x]]=x #一开始d为空，else之后会给字典赋键值，意思是第一次判断肯定会else，然后赋值才进行第二次判断

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #判断target - nums[i]的值是否等于i之后的元素，只需一个for循环
        #968 ms	14.5 MB
        lens = len(nums)
        for i in range(lens):
            temp = nums[i+1:]
            if (target - nums[i]) in temp:
                j = temp.index(target - nums[i])+i+1
                return i,j

 class Solution:
     def twoSum(self, nums: List[int], target: int) -> List[int]:
         lens = len(nums)
         for i in range(lens):
            #调换一下顺序
            temp = nums[:i]
            if (target - nums[i]) in temp:
                j = temp.index(target - nums[i])
                return [j,i]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #用字典，key为list中的元素的值，value为元素值对应的index
        dict = {}
        lens = len(nums)
        for i in range(lens):
            if target - nums[i] in dict:
                return dict[target - nums[i]], i
            else:
                dict[nums[i]] = i












































