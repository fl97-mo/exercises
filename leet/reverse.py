#Given a signed 32-bit integer x, return x with its digits reversed. 
#If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



def reverse(x):
    is_negative = False
    if x <= 0:
        is_negative = True
        x = abs(x)
    if x > (2**31)-1 or x < -(2**31):
            return 0
    else:  
        i = 0
        y = 0
        while i <= 10 and x != 0:
            y = y * 10 + (x % 10)
            x //= 10
            i += 1
    if is_negative:
        y = -y        
            
    if y > (2**31)-1 or y < -(2**31):
        return 0                
    return y
    
print("Max =", (2**31)-1, "Min =", (-2**31)) 
print(reverse(-123))        
