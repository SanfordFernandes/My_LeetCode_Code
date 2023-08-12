'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        longest_len = 0

        while(1 <= len(s)):
            selected = []
            for i in s:
                if(i not in selected):
                    selected.append(i)
                else:
                    break                
            longest_len = max(longest_len, len(selected))
            s = s[1:]

        return longest_len



s = "baa"
print('Res:', Solution().lengthOfLongestSubstring(s))