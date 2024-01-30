class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        x_str = str(x)
        return x_str == x_str[::-1]

def main():
    sol= Solution()
    print(sol.isPalindrome(121))
    print(sol.isPalindrome(12322))

if __name__=="__main__":
    main()