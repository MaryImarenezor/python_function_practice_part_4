# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a,b,c):
    return max(a,b,c)


max_num(4,7,5)
# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(list):
    
    result = list[0]
    if len(list) == 0:
        return 0
    else:
        for num in list[1:]:
            result = result * num
        return result


mult_list([4,6,8,23,5,6])
# Write a Python function called rev_string() to reverse a string.
def rev_string(string):
    return string[::-1]


rev_string("Hello there, world!")
# Write a Python function called num_within() to check whether a number falls in a given range.
def num_whithin(x,a,b):
    return x in range(a,b+1)


num_whithin(4,2,10)
# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
triangle = [[1],[1,1]]
def pascal(n):
    #base case
    if n < 1:
        print("invalid number of rows")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
        row = []
        row_prev = triangle[row_number - 1]
    #create correct row, then add to triangle (this row will be 1 longer than row before it)
        length = len(row_prev)+1
        for i in range(length):
        #first number is 1
            if i == 0:
                row.append(1)
        #intermediate nunmbers get added from previous rows
            elif i > 0 and i < length-1:
                row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
            else:
                row.append(1)
        triangle.append(row)
        row_number += 1

    #print triangle
    for row in triangle:
        print(row)



pascal(3)
