# 2 trials 15 min
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        words.sort()
        result = sorted(words, key = words.count, reverse = True)
        print(result)
        res=[]
        [res.append(x) for x in result if x not in res]
        print(res)
        return res[:k]