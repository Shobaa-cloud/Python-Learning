nums=[1,2,3,0,4,5,0,6,0,0,7,8]
a=0
for i in range(len(nums)):
    if nums[i]!=0:
        nums[a]=nums[i]
        a+=1
for i in range(a,len(nums)):
    nums[i]=0
print(nums)

''' Shift zeros to the last without creating any list (i.e) make changes in-place'''