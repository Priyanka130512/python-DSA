"""
def fib(n):
    if n<=1:
        return n
    dp=[0]*(n+1)
    dp[1]=1
    for i in range(2,n+1):  # dynamic -programming
        dp[i]=dp[i-1]+ dp[i-2]
    return dp[n]
print (fib(7))
"""
def fib(n):
    if n<=1:
        return n
    prev2=0
    prev=1
    for i in range(2,n+1):
        i=prev+prev2
        prev2=prev
        prev=i
    return prev 
print(fib(9))