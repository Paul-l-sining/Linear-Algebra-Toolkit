"""
[[ a1 a2 a3 ]
 [ a4 a5 a6 ]
 [ a7 a8 a9 ]]


Matric: A       Matric: B

[[ a b c ]     [[ j k l ]    [aj+bm+cp  ak+bn+cq  al+bo+cr]
 [ d e f ]  *   [ m n o ]  = [dj+em+fp  dk+en+fq  dl+eo+fr]
 [ g h i ]]     [ p q r ]]   [gj+hm+ip  gk+hn+iq  gl+ho+ir]
 
 
Requirement: Column A == Row B

"""

def matrics_multiplication (matricA, matricB):
    if len(matricA) == 0 or len(matricB) == 0:
        return  # empty matrics can't be multiplied
    
    if len(matricA[0]) != len(matricB):
        return   # 2 matrics can't be multiplied
    
    # initiate empty product matrics
    product = []
    for _ in range(len(matricA)):
        product.append([0]* len(matricB[0]))
    
    # calculate
    for j in range(len(matricB[0])):
        for k in range(len(matricA)):
            a = 0
            for i in range(len(matricA[0])):
                a += matricA[k][i] * matricB[i][j]  
            product[k][j] = a
            
    return product
    



if __name__ == "__main__":
    
    mA = []
    col_count = 0
    row_count = 1
    print("Press 'enter' to finish matric A")
    while True:
        r = input(f"Please enter matric A row {row_count}, seperate by ',' : ")
        
        
        if r == '': # finish constructing the matric
            break
        
        try:
            row_str = r.split(',') # convert input into int and store them.
            row = []
            for ele in row_str:
                row.append(int(ele))
        except:
            print("invalid input")
            mA = []
            break

        # check if the number of element is equivelent for each row.
        if col_count == 0:
            col_count = len(row)
        else:
            if len(row) != col_count:
                print('column elements number has to be equivelent, please try again.')
                mA = []
                break
            
        mA.append(row)
        row_count += 1
        
    
    mB = []
    col_count = 0
    row_count = 1
    
    if len(mA) != 0:
        print("Press 'enter' to finish matric B")
        while True:
            r = input(f"Please enter matric B row {row_count}, seperate by ',' : ")
            
            
            if r == '': # finish constructing the matric
                break
            
            try:
                row_str = r.split(',') # convert input into int and store them.
                row = []
                for ele in row_str:
                    row.append(int(ele))
            except:
                print("invalid input")
                mB = []
                break

            # check if the number of element is equivelent for each row.
            if col_count == 0:
                col_count = len(row)
            else:
                if len(row) != col_count:
                    print('column elements number has to be equivelent, please try again.')
                    mB = []
                    break
                
            mB.append(row)
            row_count += 1
    
    product = matrics_multiplication(mA, mB)
    print(f'Matric A is {mA}')
    print(f'Matric B is {mB}')
    print(f'Matric A * Matric B is {product}')
    
    
    
    #     mA = [[-2, 0, -2],
#           [0, 4, 2]]
#     mB = [[-2, 0],
#           [0, 4],
#           [-2,2]]
#     
#     """Result:
#         [[8, -4],
#          [-4, 20]]
#     """
#     mA = [[5, 1], [1, 2]]
#     mB = [[-2, 0, -2], [0, 4, 2]]