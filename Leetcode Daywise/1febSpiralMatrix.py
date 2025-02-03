class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result=[]
        l, r = 0, len(matrix[0]) #r = no. of columns+1
        t,b=0,len(matrix) #b = no. of rows
        while l<r and t<b:
            #every i in the top row is fetched
            for i in range(l,r): #r -> non inclusive
                result.append(matrix[t][i])
            t+=1 #shift top down by 1
            #every i in the right column is fetched
            for i in range(t,b):
                result.append(matrix[i][r-1])#r -> out of bounce
            r-=1 
            if not (l<r and t<b):
                break
            #every i in the bottom row is fetched
            for i in range(r-1,l-1,-1):
                #l -> non inclusive and we want to to go all the way to left. That is R to L - reverse order
                result.append(matrix[b-1][i])
            b-=1
            #every i in the left column is fetched
            for i in range(b-1,t-1,-1):
                #t -> non inclusive and we want to to go all the way to top. That is B to T - reverse order
                result.append(matrix[i][l])
            l+=1
        return result
