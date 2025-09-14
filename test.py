class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {"a","e","i","o","u"}
        vowels_dict = {}
        nonvowels_dict = {}

        for letter in s:
            if letter in vowels:
                vowels_dict[letter] = vowels_dict.get(letter,0)+1
            else:
                nonvowels_dict[letter] = nonvowels_dict.get(letter,0)+1
                
        max_vowel = max(vowels_dict, key=vowels_dict.get) if vowels_dict else 0
        max_nonvowel = max(nonvowels_dict, key=nonvowels_dict.get) if nonvowels_dict else 0
        return(vowels_dict.get(max_vowel,0) + nonvowels_dict.get(max_nonvowel,0))