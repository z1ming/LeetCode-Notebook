class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        C, R = set(), {id}
        for i in range(level):
            C |= R
            R = set(sum([friends[r] for r in R], [])) - C
        D = collections.Counter(sum([watchedVideos[r] for r in R], []))
        return sorted(D, key = lambda a: (D[a], a))