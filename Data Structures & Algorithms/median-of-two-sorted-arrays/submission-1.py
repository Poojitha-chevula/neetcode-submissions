class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=sorted(nums1+nums2)
        if(len(n)%2==0):
            return float(n[len(n)//2-1]+n[len(n)//2])/2
        else:
            return float(n[len(n)//2])