

def duplicate_or_unique(inList):
    dict = {}

    for num in inList:
        dict[num] = dict.get(num, 0) + 1

    expected_size = (len(dict) + 1) if len(inList) % 2 == 0 else (2 * len(dict) - 1)
    for num, count in dict.items():
        if expected_size == len(inList):
            if count == 2:
                return num
        else:
            if count == 1:
                return num


print(duplicate_or_unique([3,6,9,2,5,8,1,4,8,7]))