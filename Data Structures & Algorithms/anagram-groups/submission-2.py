class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if(len(strs)==1):
            return [strs]
        l={}
        for i in strs:
            k=tuple(sorted(i))
            if k not in l:
                l[k]=[]
            l[k].append(i)
        return list(l.values())