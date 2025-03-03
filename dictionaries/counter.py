# 
dict = {}
list = [1,2,3,4,5,2,3,5,4,9,9,9,9,5,5,5,5,5,5,5,5]

for num in list:
    dict[num] = dict.get(num,0) + 1
    

print(dict)
print(max(dict.items()))