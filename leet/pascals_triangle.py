def generate_pascals_triangle(numRows):
    list = []
    
    for i in range(numRows):
        row = [1] * (i + 1)
        
        for j in range(1, i):
            row[j] = list[i-1][j-1] + list[i - 1][j]
        list.append(row)
    
    return list

pascals_triangle = generate_pascals_triangle(5)
print(pascals_triangle)



    





        
        