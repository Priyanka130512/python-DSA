#print all unique pair combinations in the given
nums=input().split(",")
l=len(nums)
for j in range(l):
    for i in range(j+l,l):
        print(nums[j],nums[j])