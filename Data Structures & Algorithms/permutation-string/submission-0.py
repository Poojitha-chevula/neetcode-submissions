class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False 
        o=[0]*26
        for i in s1:
            o[ord(i)-ord('a')]+=1
        l=0
        r=0
        re=[0]*26
        while(r<len(s1)):
            re[ord(s2[r])-ord('a')]+=1
            r+=1
        if re==o:
            return True
        while(r<len(s2)):
            re[ord(s2[l])-ord('a')]-=1
            l+=1
            re[ord(s2[r])-ord('a')]+=1
            r+=1
            if(re==o):
                return True
        return False