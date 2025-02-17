#Return the number of times that the string "hi" appears anywhere in the given string.
#count_hi('abc hi ho') → 1
#count_hi('ABChi hi') → 2
#count_hi('hihi') → 2

def count_hi(str):
    counter = 0 
    for i in range(len(str)):
        if str[i:i+2] == "hi":
            counter +=1

    return counter

print(count_hi("Hallo hi hi hallo hi"))