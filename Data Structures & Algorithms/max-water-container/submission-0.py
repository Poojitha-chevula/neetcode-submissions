class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans=0
        i=0
        j=len(heights)-1
        while (i<len(heights) and j>0 and i<j):
            k=(j-i)*(min(heights[i],heights[j]))
            ans=max(ans,k)
            if(heights[i]<heights[j]):
                i=i+1
            else:
                j=j-1
        return ans