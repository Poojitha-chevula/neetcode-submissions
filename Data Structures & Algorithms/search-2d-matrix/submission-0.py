class Solution:
    def search(self, matrix, tar, k):
        i=0
        j=len(matrix[k])-1
        while(i<=j):
            mid=(i+j)//2
            if(matrix[k][mid]==tar):
                return True
            elif(matrix[k][mid]>tar):
                j=mid-1
            else:
                i=mid+1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        j=len(matrix[0])-1
        ans=False
        for k in range(len(matrix)):
            if(matrix[k][0]>target):
                continue
            if(matrix[k][j]<target):
                continue
            else:
                ans=self.search(matrix,target,k)
                return ans
        return ans