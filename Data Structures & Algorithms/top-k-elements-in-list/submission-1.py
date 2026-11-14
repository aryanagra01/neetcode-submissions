class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        chardict = {}
        for char in nums:
            chardict[char] = chardict.get(char, 0) + 1
        return sorted(chardict, key=lambda x: chardict[x], reverse=True)[:k]