#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers 
    representing Pascals triangle of n:
    """

    if n <= 0:
        return []

    
    """ empty resulting array initialized """
    pascal = [[] for idx in range(n)]

    for li in range(n):
        for col in range(li+1):
            if(col < li):
                if(col == 0):
                    """ first column set to 1 """
                    pascal[li].append(1)
                else:
                    pascal[li].append(pascal[li-1][col] + pascal[li-1][col-1])
            elif(col == li):
                """ diagonal set to 1 """
                pascal[li].append(1)

    return pascal