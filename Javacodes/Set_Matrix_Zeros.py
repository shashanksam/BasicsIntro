#VERSION 1


from math import *
from collections import *
from sys import *
from os import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
	# Write your code here.

    rows0=[]
    cols0=[]
    for a,row in enumerate( matrix):
        for b,ele in enumerate(row):
            if(ele ==0):
                rows0.append(a)
                cols0.append(b)
    # print("rows are "+ str(rows0))

    for i in rows0:
        for a in range(len(matrix[0])) :
            matrix[i][a]=0

    # print("cols are "+ str(cols0))
    
    for i in cols0:
        for b in range(len(matrix)):
            matrix[b][i]=0


    # print(matrix)
    pass





#VERSION 2

from math import *
from collections import *
from sys import *
from os import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
	# Write your code here.

    rows0=[]
    cols0=[]
    r=len(matrix)
    c=len(matrix[0])
    for i in range(r):
        for j in range(c):
            if(matrix[i][j] ==0):
                rows0.append(i)
                cols0.append(j)
    # print("rows are "+ str(rows0))

    for i in rows0:
        for a in range(len(matrix[0])) :
            matrix[i][a]=0

    # print("cols are "+ str(cols0))
    
    for i in cols0:
        for b in range(len(matrix)):
            matrix[b][i]=0


    # print(matrix)
    pass




