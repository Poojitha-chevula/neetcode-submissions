class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for i in tokens:
            if(i.lstrip("-").isdigit()):
                st.append(int(i))
            elif(len(st)!=0):
                b=st.pop()
                a=st.pop()
                if(i=="+"):
                    st.append(a+b)
                elif(i=="-"):
                    st.append(a-b)
                elif(i=="*"):
                    st.append(a*b)
                else:
                    st.append(int(a/b))
        return st[-1]