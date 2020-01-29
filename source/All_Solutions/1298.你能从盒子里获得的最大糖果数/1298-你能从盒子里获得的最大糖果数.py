class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        if not initialBoxes:
            return 0
        cur_stack = initialBoxes
        seen = set([])  # visited boxes
        while cur_stack:
            next_stack = []
            for box in cur_stack:
                seen.add(box)
                for k in keys[box]:
                    status[k] = 1
                next_stack += containedBoxes[box]     
            cur_stack = next_stack

        return sum(candies[s] for s in seen if status[s])