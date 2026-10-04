class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictCheck = {}
        index = 0
        for i in nums:
            if dictCheck and i in dictCheck:
                return [dictCheck[i], index]
            else:
                diff = target - i
                dictCheck[diff] = index
                index += 1

        