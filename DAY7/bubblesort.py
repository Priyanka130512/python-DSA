"""
def Bubblesort(nums):
    if nums[0]>nums[1]:
     nums[0], nums[1] = nums[1], nums[0]
    return nums
nums=[5,4,3,2,1]
print(Bubblesort(nums))
"""
"""def Bubblesort(nums):
    L=len(nums)
    for i in range(L-1):
        if nums[i]>nums[i+1]:
            nums[i],nums[i+1]=nums[i+1],nums[i]
    return nums
nums=[5,4,3,2,1,2]
print(Bubblesort(nums))
"""
def Bubblesort(nums):
    L=len(nums)
    for j in range(L):
         for i in range(L-1):
            if nums[i]>nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]
    return i,nums
