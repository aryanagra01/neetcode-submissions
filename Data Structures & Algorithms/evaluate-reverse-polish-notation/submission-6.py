class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        outputStack = []
        for i in tokens:
            if i.lstrip("-").isdigit():
                outputStack.append(i)
            else:
                if outputStack and len(outputStack) < 2:
                    return False
                else:
                    op2 = outputStack.pop()
                    op1 = outputStack.pop()
                    
                    if i == "+":
                        outputStack.append(int(op1) + int(op2))
                    if i == "-":
                        outputStack.append(int(op1) - int(op2))              
                    if i == "*":
                        outputStack.append(int(op1) * int(op2))        
                    if i == "/":
                        outputStack.append(int(op1) / int(op2))

        if len(outputStack) != 1:
            return False
        else:
            return int(outputStack[0])

