class Solution:
    def isValid(self, s: str) -> bool:
        stack=[] #empty list
        closeToOpen={")":"(",
                     "]":"[",
                     "}":"{"}
        #hash map mapping closing parentheses to open
        for c in s: #iterate through each character in input string
            if c in closeToOpen: #if character is a closing parentheses
                if stack and stack[-1]==closeToOpen[c]: #if closed parentheses is matching open parentheses
                    stack.pop()
                else:
                    return False #in cases like ")" and "[)"
            else:
                stack.append(c)
        return True if not stack else False
