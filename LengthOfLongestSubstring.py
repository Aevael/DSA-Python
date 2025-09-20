# The runtime complexity of this solution is O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_left = 0
        max_length = 0
        char_set = set()
        
        for window_right in range(len(s)):
            while s[window_right] in char_set:
                char_set.remove(s[window_left])
                window_left += 1

            char_set.add(s[window_right])
            max_length = max(max_length, window_right - window_left + 1)
        
        return max_length


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