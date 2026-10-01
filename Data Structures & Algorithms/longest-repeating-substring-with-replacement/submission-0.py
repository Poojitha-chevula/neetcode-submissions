class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hp={}
        l=0
        r=0
        ans=0
        while(r<len(s)):
            hp[s[r]]=hp.get(s[r],0)+1
            repl=(r-l+1)-max(hp.values())
            if(repl>k):
                hp[s[l]]-=1
                l=l+1
            ans=max(ans,r-l+1)
            r+=1
        return ans