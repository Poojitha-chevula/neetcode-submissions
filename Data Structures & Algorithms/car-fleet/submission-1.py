class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hp={}
        for i in range(len(position)):
            hp[position[i]]=speed[i]
        mp=dict(sorted(hp.items(), reverse=True))
        st=[]
        for p,s in mp.items():
            v=(target-p)/s
            if len(st)==0:
                st.append(v)
            elif v>st[-1]:
                st.append(v)
        return len(st)