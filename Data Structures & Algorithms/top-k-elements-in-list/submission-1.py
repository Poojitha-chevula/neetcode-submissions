class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l={}
        ans=[]
        for i in nums:
            l[i]=l.get(i,0)+1;
        sorted_list=sorted(l.items(),key=lambda x: x[1], reverse=True)
        for pair in sorted_list[:k]:
            ans.append(pair[0])
        return ans