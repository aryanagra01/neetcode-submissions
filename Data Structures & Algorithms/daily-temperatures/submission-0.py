class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        index = 0

        for i in temperatures:
            while stack and i > temperatures[stack[-1]]:
                oldindex = stack.pop()
                output[oldindex] = index - oldindex

            stack.append(index)
            index += 1
            
        
        return output
        