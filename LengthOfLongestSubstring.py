# The runtime complexity of this solution is O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windowleft = 0
        maxlength = 0
        charset = set()
        
        for windowright in range(len(s)):
            while s[windowright] in charset:
                charset.remove(s[windowleft])
                left += 1

            charset.add(s[windowright])
            max_length = max(max_length, windowright - windowleft + 1)
        
        return maxlength


'''
Given a string s, find the length of the longest substring without duplicate characters.

 

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