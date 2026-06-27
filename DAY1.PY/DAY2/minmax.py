"""
#find min and max
nums=input().split()
print(nums)
nums[0]=int(nums[0])
print(nums)  
"""
"""
nums=input().split()
print(nums)
for i in range(len(nums)):
    nums[i]=int(nums[i])
print(nums)
"""
"""
nums=input().split()
print(nums)
for i in range(len(nums)):
    nums[i]=int(nums[i])**2
    print(nums)
nums=input().split()
print(nums)
for i in range(len(nums)):
    if i%2==0:
        nums[i]=int(nums[i])*2
    else :
        nums[i]=int(nums[i]*3)
    print(nums)
"""
"""
nums=list(map(int,input().split()))
for i in range(1,len(nums)):
    if i+i>len(nums):
        break
    nums[i+1]=nums[i*1]**2
print(nums)
"""
"""
nums=list(map(int,input().split()))
list2=[]
for i in range(1,len(nums)):
    if i*
"""










"""
    #minimum
nums=list(map(int,input().split()))
curr_min=nums[0]
for i in range(len(nums)):
    if curr_min>nums[i]:
        curr_min=nums[i]
print(curr_min)
"""
"""
#maximum
nums=list(map(int,input().split()))
curr_max=nums[0]
for i in range(len(nums)):
    if curr_max<nums[i]:
        curr_max=nums[i]
print(curr_max)
"""
# sorting

"""
num=3
if num%2==0:
    if num>1:
        print("even positive")
    else:
         print("even negative")
else:
    if num>1:
        print("odd positive")
    else:
        if num>0:
            print("odd negative")
"""
"""
num=2
if num%2==0 and num>1:
    print("even positive")
    if 100%num==0:
         print("super number")
elif num%2==0 and num<0:
    print("even negative ")
elif num%2==1 and num>1:
    print("odd positive")
elif num%2==1 and num<0:
    print("odd negative")
"""
"""
def h():
    for i in range(3):
        print(i)
result=(h())
print(result)
"""
