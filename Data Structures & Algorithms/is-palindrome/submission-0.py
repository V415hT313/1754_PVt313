class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = [char.lower() for char in s if char.isalnum()]
        newString = "".join(newString)
        print(newString)
        reverseString = newString[::-1]
        if reverseString == newString:
            return True
        else:
            return False

        
        
            