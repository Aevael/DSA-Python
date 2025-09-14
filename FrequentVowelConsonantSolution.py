class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowelcount = 0
        consonantcount = 0
        scounter = Counter(s)
        for k, v in scounter.items():
            if k in vowels:
                vowelcount = max(vowelcount, v)
            else:
                consonantcount = max(consonantcount, v)
        return vowelcount + consonantcount