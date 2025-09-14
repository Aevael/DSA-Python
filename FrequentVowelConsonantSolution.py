class Solution:
    def maxFreqSum(self, s: str) -> int:
        lettercount = {}
        maxconsonant = 0
        maxvowel = 0
        for letter in s:
            match letter:
                case 'a':
                    if 'a' in lettercount:
                        currentcount = lettercount['a'] + 1
                        lettercount.update({'a' : currentcount})
                        if currentcount > maxvowel:
                            maxvowel = currentcount
                    else:
                        lettercount.update({'a' : 1})
                        if maxvowel == 0:
                            maxvowel = 1
                case 'e':
                    if 'e' in lettercount:
                        currentcount = lettercount['e'] + 1
                        lettercount.update({'e' : currentcount})
                        if currentcount > maxvowel:
                            maxvowel = currentcount
                    else:
                        lettercount.update({'e' : 1})
                        if maxvowel == 0:
                            maxvowel = 1
                case 'i':
                    if 'i' in lettercount:
                        currentcount = lettercount['i'] + 1
                        lettercount.update({'i' : currentcount})
                        if currentcount > maxvowel:
                            maxvowel = currentcount
                    else:
                        lettercount.update({'i' : 1})
                        if maxvowel == 0:
                            maxvowel = 1
                case 'o':
                    if 'o' in lettercount:
                        currentcount = lettercount['o'] + 1
                        lettercount.update({'o' : currentcount})
                        if currentcount > maxvowel:
                            maxvowel = currentcount
                    else:
                        lettercount.update({'o' : 1})
                        if maxvowel == 0:
                            maxvowel = 1
                case 'u':
                    if 'u' in lettercount:
                        currentcount = lettercount['u'] + 1
                        lettercount.update({'u' : currentcount})
                        if currentcount > maxvowel:
                            maxvowel = currentcount
                    else:
                        lettercount.update({'u' : 1})
                        if maxvowel == 0:
                            maxvowel = 1
                case _:
                    if letter in lettercount:
                        currentcount = lettercount[letter] + 1
                        lettercount.update({letter : currentcount})
                        if currentcount > maxconsonant:
                            maxconsonant = currentcount
                    else:
                        lettercount.update({letter : 1})
                        if maxconsonant == 0:
                            maxconsonant = 1
        return maxconsonant + maxvowel