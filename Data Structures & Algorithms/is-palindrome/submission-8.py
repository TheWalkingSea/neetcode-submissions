class Solution:
    def isPalindrome(self, s: str) -> bool:

        allowedCharacters = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')


        l = 0
        r = len(s) - 1

        while l < len(s) and s[l] not in allowedCharacters:
            l += 1
        while r > 0 and s[r] not in allowedCharacters:
            r -= 1

        while r >= l:
            if (s[l].lower() != s[r].lower()):
                return False

            l += 1
            r -= 1

            while l < len(s) and s[l] not in allowedCharacters:
                l += 1
            while r > 0 and s[r] not in allowedCharacters:
                r -= 1
        return True
