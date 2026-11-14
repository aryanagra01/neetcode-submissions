class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        chardict = {}
        for char in nums:
            chardict[char] = chardict.get(char, 0) + 1
        sortdict = sorted(chardict.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in sortdict[:k]]