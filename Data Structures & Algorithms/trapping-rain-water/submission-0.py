class Solution:
    def trap(self, height: List[int]) -> int:
        p=[0]*(len(height))
        p[0]=height[0]
        s=[0]*(len(height))
        s[len(height)-1]=height[-1]
        for i in range(1,len(height)):
            p[i]=max(p[i-1],height[i])
        for i in range(len(height)-2,-1,-1):
            s[i]=max(s[i+1],height[i])
        ans=0
        for i in range(len(height)):
            ans+=min(p[i],s[i])-height[i]
        return ans