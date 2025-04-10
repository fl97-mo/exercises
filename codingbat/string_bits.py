#Given a string, return a new string made of every other 
#char starting with the first, so "Hello" yields "Hlo".
#string_bits('Hello') → 'Hlo'
#string_bits('Hi') → 'H'
#string_bits('Heeololeo') → 'Hello'

def string_bits(str):
    word = ""
    
    for letter in str[::2]:
        word += letter
        
    return word

print(string_bits('Heeololeo'))
        
    
