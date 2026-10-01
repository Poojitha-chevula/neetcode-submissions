class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pm=[0]*len(prices)
        pm[0]=prices[0]
        for i in range(1,len(prices)):
            pm[i]=min(pm[i-1],prices[i-1])
        ans=0
        for i in range(len(pm)):
            k=prices[i]-pm[i]
            ans=max(ans,k)
        return ans