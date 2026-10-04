class Solution:
    def isPalindrome(self, s: str) -> bool:
        #2 pointer solution
        #use ascii values, and find the space ascii vlaue
        #create a while loop for if it not alphanumerical
        #o(n) time complexity but only o(1) space because a new string is not created

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r> l and not self.alphaNum(s[r]):
                r -= 1    
            if s[l].lower() != s[r].lower():
                return False
            l , r = l + 1, r - 1
        return True
            
 
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
