class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        s1=set()
        ans=0
        while(r<len(s)):
            if s[r] not in s1:
                s1.add(s[r])
                e=r-l+1
                ans=max(e,ans)
                r+=1
            else:
                s1.remove(s[l])
                l += 1      
        return ans