class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        l = []

        for s, n in counts.most_common(k):
            
            if True:
            
                l.append(s)  #Map[1] -> Map[1, 0]
            
            else:
            
                continue

        return l