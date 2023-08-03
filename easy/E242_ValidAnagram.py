'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # check if both the string lengths are not the same
        if(len(s) != len(t)):
            return False

        # create dictionary to store character counts
        dict_s = {}

        # iterate over string "s" and get character counts
        for char in s:
            if(char not in dict_s):
                # add character to dict if not present
                dict_s[char] = 1
            else:
                # increment character count since it exists in dict
                dict_s[char] += 1

        for char in t:
            if char not in dict_s:
                # character not found in string "s"
                return False
            elif(dict_s[char]):
                # decrement character count from dictionary
                dict_s[char] -= 1
            else:
                # character count exhausted
                return False
            
        return True


s, t = "anagram", "nagaramm"
print('Res:', Solution().isAnagram(s, t))
