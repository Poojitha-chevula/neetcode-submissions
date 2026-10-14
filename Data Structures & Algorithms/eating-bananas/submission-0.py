class Solution:
    def check(self,piles,h,mid):
        hrs=0
        for i in range(len(piles)):
            hrs+=math.ceil(piles[i]/mid)
        return hrs<=h
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i=1
        j=max(piles)
        while(i<=j):
            mid=(i+j)//2
            if(self.check(piles,h,mid)):
                j=mid-1
            else:
                i=mid+1
        return i