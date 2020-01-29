class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices&1 or tomatoSlices>cheeseSlices<<2 or tomatoSlices<cheeseSlices<<1:
            return []
        jumbo=tomatoSlices-(cheeseSlices<<1)>>1
        small=cheeseSlices-jumbo
        return jumbo,small