class Solution:
    def printVertically(self, s: str) -> List[str]:
        return [''.join(i).rstrip() for i in itertools.zip_longest(*s.split(),fillvalue=' ')]