class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {")" : "(", "]" : "[" , "}" : "{"}

        for i in s:
            if i in dict.values():
                stack.append(i)
            else:
                if stack and dict[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        else:
            return True

        