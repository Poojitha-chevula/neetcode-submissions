class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        s=s.lower()
        while(i<len(s) and j>=0 and i<=j):
            while (i<len(s) and i<=j) and( not s[i].isalnum()):
                i=i+1
            while (j>0 and i<=j) and( not s[j].isalnum()):
                j=j-1
            if i>j:
                break
            if (s[i]!=s[j]):
                return False
            i=i+1
            j=j-1
        return True