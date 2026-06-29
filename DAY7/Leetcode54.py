def spiralOrder(matrix,m,n):
    top=0
    left=0
    bottom=m-1
    right=n-1

    while top<=bottom and left<=right:
        #First row
        for i in range(left,right+1):
            print(matrix[top][i],end=" ")
        top+=1
        #Right column
        for i in range(top,bottom+1):
            print(matrix[i][right],end=" ")
        right-=1
        #Bottom row
        if top<=bottom:
            for i in range(right,left-1,-1):
                print(matrix[bottom][i],end=" ")
            bottom-=1
        #print 4&5
        if left<=right:
            for i in range(bottom,top-1,-1):
                print(matrix[i][left],end=" ")
            left=left+1
    

#Main
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix,3,3))

#  To remove none
# . create an empty list ....to append
# . remove print statement by using it