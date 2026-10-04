class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #list in list, index and temp
        output = [0] * len(temperatures)


        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                oldIndex, oldT = stack.pop()
                output[oldIndex] = index - oldIndex
            stack.append([index,temp])
        
        return output
        