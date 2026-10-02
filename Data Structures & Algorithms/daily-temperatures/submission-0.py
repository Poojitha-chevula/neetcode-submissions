class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=[]
        st.append(0)
        r=[0]*len(temperatures)
        for i in range(1,len(temperatures)):
            while(len(st)!=0) and (temperatures[i]>temperatures[st[-1]]):
                r[st[-1]]=i-st[-1]
                st.pop()
            else:
                st.append(i)
        return r