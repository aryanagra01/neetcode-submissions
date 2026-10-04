class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        outputStack = []
        for i in tokens:
            if i not in "+-*/":
                outputStack.append(int(i))
            else:
                op2 = outputStack.pop()
                op1 = outputStack.pop()
                
                if i == "+":
                    outputStack.append(op1 + op2)
                if i == "-":
                    outputStack.append(op1 - op2)              
                if i == "*":
                    outputStack.append(op1 * op2)        
                if i == "/":
                    outputStack.append(int(op1 / op2))


        return outputStack[0]

