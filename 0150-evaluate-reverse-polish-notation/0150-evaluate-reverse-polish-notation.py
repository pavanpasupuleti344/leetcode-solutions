class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        op=[]
        # op=['+','-','/','*']
        # d={}
        for i in tokens:
            if i in ('+','-','/','*'):
                op.append(i)
            else:
                stack.append(int(i))

            if len(op)!=0 and len(stack)>=2:
                # print(f'stack{stack} and op:{op}')
                if op[-1]=='+':
                    t=stack[-2]+stack[-1]
                elif op[-1]=='-':
                    t=stack[-2]-stack[-1]
                elif op[-1]=='*':
                    t=stack[-2]*stack[-1]
                elif op[-1]=='/':
                    t=int(stack[-2]/stack[-1])
                op.pop()
                stack.pop()
                stack.pop()
                stack.append(t)
                # print(f'stack{stack} and op:{op}\n')
        return stack[0]