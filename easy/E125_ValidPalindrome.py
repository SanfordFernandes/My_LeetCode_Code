'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''

class Solution(object):
    def isPalindrome(self, s = str):
        """
        :type s: str
        :rtype: bool
        """

        start, end, s = 0, len(list(s)) - 1, s.lower()

        while start < end:
            if(s[start].isalnum() and s[end].isalnum()):
                if(s[start] != s[end]):
                    return False
                start += 1
                end -= 1
            else:
                if(not s[start].isalnum()):
                    start += 1

                if(not s[end].isalnum()):
                    end -= 1
                
        return True


s = '*&tellet""'
print('Res:', Solution().isPalindrome(s))