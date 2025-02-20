#Given a string of even length, 
# return the first half. So the string "WooHoo" yields "Woo".

#first_half('WooHoo') → 'Woo'
#first_half('HelloThere') → 'Hello'
#first_half('abcdef') → 'abc'

def first_half(str):
    i = len(str) * 0.5
    return str[:int(i)]

print(first_half("ABCDEF"))