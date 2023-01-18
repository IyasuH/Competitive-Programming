# 14 min 2 trials
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for x in tokens:
            if x=='+':
                val=stack[len(stack)-2]+stack[len(stack)-1]
                stack.pop(len(stack)-2)
                stack.pop(len(stack)-1)
                stack.append(val)
            elif x=='-':
                val=stack[len(stack)-2]-stack[len(stack)-1]
                stack.pop(len(stack)-2)
                stack.pop(len(stack)-1)
                stack.append(val)
            elif x=='*':
                val=int(stack[len(stack)-2]*stack[len(stack)-1])
                stack.pop(len(stack)-2)
                stack.pop(len(stack)-1)
                stack.append(val)
            elif x=='/':
                val=int(stack[len(stack)-2]/stack[len(stack)-1])
                stack.pop(len(stack)-2)
                stack.pop(len(stack)-1)
                stack.append(val)
            else:
                stack.append(int(x))
            # print(stack)
        return stack[0]