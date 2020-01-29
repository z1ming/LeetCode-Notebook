class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.d = itertools.combinations(characters, combinationLength)
        self.n = math.comb(len(characters), combinationLength)

    def next(self) -> str:
        self.n -= 1
        return ''.join(next(self.d))

    def hasNext(self) -> bool:
        return self.n