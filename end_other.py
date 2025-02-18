#Given two strings, return True if either of the strings appears at the very end of the other string, 
#ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

#end_other('Hiabc', 'abc') → True
#end_other('AbC', 'HiaBc') → True
#end_other('abc', 'abXabc') → True


def end_other(a, b):
    for letter in a:
        if a.lower() == b[-len(a):].lower():
            return True
        elif b.lower() == a[-len(b):].lower():
            return True
        else:
            return False
  
  
print(end_other('AbC', 'HiaBc'))

