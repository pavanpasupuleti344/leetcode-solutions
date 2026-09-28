class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        # o=0
        for c in s:
            if c.isdigit():
                # if len(stack)==0:
                #     stack.append(int(c))
                if stack and str(stack[-1]).isdigit():
                    stack[-1]*=10
                    stack[-1]+=int(c)
                else:
                    stack.append(int(c))
                    
            elif c=='[':
                stack.append(c)
                # o+=1
            elif c==']':
                while True:
                    print(stack)
                    if stack[-1][0]=='[':
                        stack[-2]*=stack[-1][1:]
                        # o-=1
                        stack.pop()
                        print('finnally      ',stack)
                        break
                    else:
                        stack[-2]+=stack[-1]
                        stack.pop()
            else:
                if len(stack)==0:
                    stack.append(c)
                else:
                    stack[-1]+=c
        return ''.join(stack)