class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=sorted(s)
        s2=sorted(t)
        if(len(s1)!=len(s2)):
            return False
        for i in range(0,len(s)):
            if(s1[i]!=s2[i]):
                return False
        return True