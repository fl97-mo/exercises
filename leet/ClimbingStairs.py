#You are climbing a staircase. It takes n steps to reach the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#Example 1:

#Input: n = 2
#Output: 2
#Explanation: There are two ways to climb to the top.
#1. 1 step + 1 step
#2. 2 steps
#Input: n = 3
#Output: 3
#Explanation: There are three ways to climb to the top.
#1. 1 step + 1 step + 1 step
#2. 1 step + 2 steps
#3. 2 steps + 1 step

def climbStairs(n):    
    if n <= 2:
        return n
    two_steps = 2
    one_step = 1

    for i in range(3, n + 1):
        current = two_steps + one_step
        one_step = two_steps
        two_steps = current

    return two_steps

print(climbStairs(5)) 
