class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=[item for items, c in Counter(nums).most_common() for item in [items] *c]
        print(freq)
        fre=list(dict.fromkeys(freq))
        print(fre)
        result=[]
        for x in range(k):
            result.append(fre[x])
        return result