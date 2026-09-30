class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans=[]
        i=0
        j=len(numbers)-1
        while(i<len(numbers) and j>=0 and i<=j):
            if numbers[i]+numbers[j]>target:
                j=j-1
            elif numbers[i]+numbers[j]<target:
                i=i+1
            else:
                ans.append(i+1)
                ans.append(j+1)
                return ans
        return ans