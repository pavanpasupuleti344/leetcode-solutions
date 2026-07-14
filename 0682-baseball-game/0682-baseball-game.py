class Solution:
    def calPoints(self, operations: List[str]) -> int:
        o=[]
        for i in operations:
            # if i.isdigit() or (i.lstrip('-').isdigit()):
            #     o.append(int(i))
            if i=='D':
                o.append(o[-1]*2)
            elif i=='C':
                o.pop(-1)
            elif i=='+':
                o.append(o[-1]+o[-2])
            else:
                o.append(int(i))
        return sum(o)