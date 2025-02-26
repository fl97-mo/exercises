#[1,1,2,3,3]
def deleteDuplicates(head):
    unique = {}
    
    for i in range(len(head)):    
        unique.setdefault(head[i])
            
    return list(unique.keys())


print(deleteDuplicates([1,1,1,1,2,3,4,5]))