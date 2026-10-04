class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                oldIndex = stack.pop()
                output[oldIndex] = index - oldIndex

            stack.append(index)

        return output