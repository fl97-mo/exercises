#given a string, return a new string where the first and last chars have been exchanged.
#front_back('code') → 'eodc'
#front_back('a') → 'a'
#front_back('ab') → 'ba'

def front_back(string):
        if len(string) < 2:
            return string
        else:
            return string[-1] + string[1:-1] + string[0]
    
print(front_back("a"))
#
print(front_back("apfelkuchen"))
#npfelkuchea