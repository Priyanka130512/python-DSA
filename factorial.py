"""
#factorial of a number
def sum_n(n):
    if n<=0:
         return 0

    return n+sum_n(n-1)
"""
"""
def factorial(n):
    if n==0:  #/n==1
        return 1
    return n*factorial(n-1)
print(factorial(5))
"""
"""
# Merge sort

def split(nums):
    mid = len(nums) // 2
    print(nums[:mid], nums[mid:])

nums = [1,2,3,4,5]
split(nums)
"""

"""
def split(nums):
    mid = len(nums) // 2
    return nums[:mid], nums[mid:]

nums = [1,2,3,4,5]

left, right = split(nums)

print("Left:", left)
print("Right:", right) 
"""

