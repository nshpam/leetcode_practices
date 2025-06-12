class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 1st brute force
        # time => O(log n)
        # space => O(log n)
        # palindrome = str(x)[::-1] # string reverse
        # if str(x) == palindrome:
        #     return True
        # return False

        # 2nd optimization => solve without converting the integer to a string
        # time => O(log n)
        # space => O(1)
        # new_x = 0
        # copy_x = x
        # while copy_x>0:
        #     # remove remainder
        #     remainder = copy_x % 10
        #     # remove new x
        #     copy_x = copy_x // 10
        #     # create reverse
        #     new_x = new_x * 10 + remainder
        # if new_x == x:
        #     return True
        # return False

        # 3rd optimization => half reversal : faster than integer reversal
        # time => O(log n)
        # space => O(1)
        reverse_half = 0
        # check if the last digit is 0 or negative value
        if (x%10 == 0 and x!=0) or x<0:
            return False

        while x>reverse_half:
            remainder = x%10
            reverse_half = reverse_half*10 + remainder
            x = x//10
            # print(remainder, reverse_half, x)
        
        return x==reverse_half or x==reverse_half//10
