# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 22:13:58 2021

@author: Abeg
"""

#matrix input
"""nge(column)]for j in range(rrow=int(input("enter the row"))
column=int(input("enter the column"))"""
"""mat=[[int(input()) for i in raow)]
print(mat)"""
"""matrix=[]
for i in range(row):
  a=[]
  for j in range(column):
    a.append(int(input()))
  matrix.append(a)
for r in range(row):
  for c in range(column):
    print(matrix[i][j],end="")
  print( )"""
#rotate clockwise-----anti
"""def rotatematrixclo(mat):
  if not len(mat):
    return
  top=0
  bottom=len(mat)-1
  left=0
  right=len(mat[0])-1
  while(left<right and top <bottom):
    prev=mat[top+1][left]
    #top element to right
    for i in range(left,right+1):
      curr=mat[top][i]
      mat[top][i]=prev
      prev=curr
    top=top+1
    for i in range(top,bottom+1):
      curr=mat[i][right]
      mat[i][right]=prev
      prev=curr
    right-=1
    for i in range(right,left-1,-1):
      curr=mat[bottom][i]
      mat[bottom][i]=prev
      prev=curr
    bottom-=1
    for i in range(bottom,top+1):
      curr=mat[i][left]
      mat[i][left]=prev
      prev=curr
    left=left+1
  return mat
row=int(input("row:"))
column=int(input("column:"))
mat=[]
for i in range(row):
  a=[]
  for j in range(column):
    a.append(int(input()))
  mat.append(a)
print(rotatematrixclo(mat))
for r in range(row):
  for c in range(column):
    print(mat[r][c],end="")
  print( )"""
#rotate matrix 90 degree-anticlockwise
#transpose+reverse column
#clockwise-transpose
"""
row=int(input("row:"))
column=int(input("column:"))
def transpose(mat):
  for i in range(row):
    for j in range(i,column):
      temp=mat[i][j]
      mat[i][j]=mat[j][i]
      mat[j][i]=temp
def reversecol(mat):
  for i in range(column):
    j=0
    k=column-1
    while j<k:
      temp=mat[j][i]
      mat[j][i]=mat[k][i]
      mat[k][i]=temp
      j+=1
      k-=1
mat=[]
for i in range(row):
  a=[]
  for j in range(column):
    a.append(int(input()))
  mat.append(a)
transpose(mat)
print(reversecol(mat))
for r in range(row):
  for c in range(column):
    print(mat[r][c],end="")
  print( )"""
#print the mAX ELEMENT OF EACH ROW
"""def maxelement(arr): 
      
    # get number of rows and columns 
    no_of_rows = len(arr) 
    no_of_column = len(arr[0]) 
      
    for i in range(no_of_rows): 
          
        # Initialize max1 to 0 at beginning 
        # of finding max element of each row 
        max1 = 0
        for j in range(no_of_column): 
            if arr[i][j] > max1 : 
                max1 = arr[i][j] 
                  
        # print maximum element of each row 
        print(max1,end=" ",sep=" ")
row=int(input("input the row"))
col=int(input("input the column"))
arr=[]
for i in range(row):
  a=[]
  for j in range(col):
    a.append(int(input()))
  arr.append(a)
for r in range(row):
  for c in range(col):
    print(arr[r][c],end=" ")
  print( )

maxelement(arr)"""
#print in spiral form
"""def spiralPrint(m, n, a):
    k = 0
    l = 0
 
    ''' k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator '''
 
    while (k < m and l < n):
 
        # Print the first row from
        # the remaining rows
        for i in range(l, n):
            print(a[k][i], end=" ")
 
        k += 1
 
        # Print the last column from
        # the remaining columns
        for i in range(k, m):
            print(a[i][n - 1], end=" ")
 
        n -= 1
 
        # Print the last row from
        # the remaining rows
        if (k < m):
 
            for i in range(n - 1, (l - 1), -1):
                print(a[m - 1][i], end=" ")
 
            m -= 1
 
        # Print the first column from
        # the remaining columns
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                print(a[i][l], end=" ")
 
            l += 1
 
 
# Driver Code
a = [[1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 11, 12],
     [13, 14, 15, 16, 17, 18]]
 
R = 3
C = 6
 
# Function Call
spiralPrint(R, C, a)"""
 


