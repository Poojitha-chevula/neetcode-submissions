class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            f=target-nums[i]
            for j in range(0,len(nums)):
                if(nums[j]==f and j!=i):
                    return [i,j]
        return []