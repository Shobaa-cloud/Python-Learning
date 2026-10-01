class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        c=0
        a=[]
        for i in range(len(nums)-1):
            if nums[i]==1 and nums[i+1]==1:
                c+=1
            else:
                c=0
            a.append(c)
        if len(nums)>1 and 1 in nums:
            return max(a)+1
        elif len(nums)==1:
            return nums[0]
        elif nums.count(1)==1:
            return 1
        else:
            return 0
'''Try [1,0,1,1,0,1]'''