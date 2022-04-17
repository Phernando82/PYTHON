class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        y = x[::-1]
        if str(x) == y:
            return True
        else:
            return False


solution_1 = Solution()
solution_1.isPalindrome(121)