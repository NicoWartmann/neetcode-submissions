class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ""
        result = True
        for char in s:
            if char.isalnum():
                s2 += char.lower()
        print(s2)
        for i in range (len(s2)//2):
            if s2[i] != s2[-(i+1)]:
                result = False
        return result