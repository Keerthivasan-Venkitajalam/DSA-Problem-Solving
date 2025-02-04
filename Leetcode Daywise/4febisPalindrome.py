class Solution:
    def isPalindrome(self, x: int) -> bool:
        #if the number is -ve or ends in 0 (except 0 itself), it cannot be a palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_half = 0
        while x > reversed_half:
            #reverse the last digit and build the reversed number
            reversed_half = reversed_half * 10 + x % 10
            x //= 10  #remove the last digit
        
        # If the number is a palindrome, the first half will equal the reversed second half.
        return x==reversed_half or x==reversed_half//10


# class Solution:
#     def isPalindrome(self, x:int)->bool:
#         #convert integer to string
#         x_str = str(x)
#         #check if the string is equal to its reverse
#         return x_str==x_str[::-1]
