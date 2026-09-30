class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s=s+str(len(i))+"#"+i
        return s
    def decode(self, s: str) -> List[str]:
        strs=[]
        p=0
        while (p<len(s)):
            l=""
            while s[p]!="#":
                l=l+s[p]
                p=p+1
            l=int(l)
            p=p+1
            k=""
            for _ in range(l):
                k+=s[p]
                p=p+1
            strs.append(k)
        return strs