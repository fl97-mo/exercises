#Given a string and a non-negative int n, 
#return a larger string that is n copies of the original string.
#string_times('Hi', 2) → 'HiHi'
#string_times('Hi', 3) → 'HiHiHi'
#string_times('Hi', 1) → 'Hi'

def string_times(str, n):
    word = ""
    for i in range(n):
        word += str
    return word

print(string_times("Hi", 7))