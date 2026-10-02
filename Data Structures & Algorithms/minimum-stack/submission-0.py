class MinStack:
    
    def __init__(self):
        self.st=[]
        self.m= float('inf')
        self.pm=[]
    def push(self, val: int) -> None:
        if(len(self.pm)==0):
            self.m=val
            self.pm.append(val)
        elif(val<=self.pm[-1]):
            self.m=val
            self.pm.append(val)
        self.st.append(val)
    def pop(self) -> None:
        t=self.st.pop()
        if(t==self.m):
            self.pm.pop()
        if(len(self.pm)==0):
            self.m=float('inf')
        else:
            self.m=self.pm[-1]
    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.pm[-1]