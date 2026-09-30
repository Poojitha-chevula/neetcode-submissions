class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
        if(len(nums)==1):
            return 1
        nums.sort()
        l=1
        ans=0
        for i in range(1,len(nums)):
            if(nums[i]-nums[i-1]==1):
                l=l+1
            elif(nums[i]-nums[i-1]>1):
                l=1
            ans=max(l,ans)
        return ans