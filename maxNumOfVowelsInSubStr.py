# 4 trials 25 min
class Solution(object):
    def numOfVowels(self, st):
        # len([char for char in example if char in "aeiouAEIOU"])
        vowels=len([x for x in st if x in "aeiou"])
        # for x in st:
        #     if x in ['a','e','i','o','u']:
        #         vowels+=1
        return vowels
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        s=list(s)
        sub=s[:k]
        numVow=self.numOfVowels(sub)
        maxVow=numVow
        for i in range(len(s)-k):
            sub.remove(s[i])
            sub.append(s[i+k])
            # sub=sub-s[i]+s[i+k]
            numVow=numVow-self.numOfVowels(s[i])+self.numOfVowels(s[i+k])
            maxVow=max(numVow, maxVow)
        return maxVow