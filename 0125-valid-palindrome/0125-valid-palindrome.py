class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
        filtered = ''.join(char.lower() for char in s if char.isalnum())
        if filtered == filtered[::-1]:
            return True
        return False
        
        