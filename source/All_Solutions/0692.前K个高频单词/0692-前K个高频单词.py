class Solution(object):
    def topKFrequent(self, words, k):
        return [x[1] for x in heapq.nsmallest(k, [(v, k) for k, v in collections.Counter(words).items()], key=lambda a: (-a[0], a[1]))]
