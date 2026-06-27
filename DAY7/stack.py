"""
stack=[]
stack.append(5)
stack.append(6)
print(stack)  #[5,6]
stack.pop() # last one removed 6
print(stack)
stack.append(7)
stack.append(4)
print('stack',stack)   #[5,7,4]
print(stack[-1]) #[4]
print(len(stack)==0)
"""
"""
stack=[5,3,8,2,3] 
for i in stack:
        print(stack.pop())  # iteration ni batti remove avuthai last number
"""

stack=[5,3,8,2,9]
l=len(stack)
t=8
for i in range(l):
    if stack.pop()==t:
        print("stack")
        break
