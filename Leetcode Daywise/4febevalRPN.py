class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[] #a list
        for char in tokens: #iterate through every char in tokens
            #5 cases -> Any one of the 4 operations or Any of the other chars - that is numbers in this case
            if char=="+":
                stack.append(stack.pop()+stack.pop())
            elif char=="*":
                stack.append(stack.pop()*stack.pop())
            elif char=="-":
                q,p=stack.pop(),stack.pop()
                stack.append(p-q)
            elif char=="/":
                a,b=stack.pop(),stack.pop()
                stack.append(int(b/a)) #round to zero
            else:
                stack.append(int(char))#simplest step - take the char change into int and append to the list (stack)
        return stack[0]
