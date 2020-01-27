class Solution(object):
    def minDeletionSize(self, A):
        def is_sorted(A):
            return all(A[i] <= A[i+1] for i in xrange(len(A) - 1))

        ans = 0
        # cur : all rows we have written
        # For example, with A = ["abc","def","ghi"] we might have
        # cur = ["ab", "de", "gh"].
        cur = [""] * len(A)

        for col in zip(*A):
            # cur2 : What we potentially can write, including the
            #        newest column 'col'.
            # Eg. if cur = ["ab","de","gh"] and col = ("c","f","i"),
            # then cur2 = ["abc","def","ghi"].
            cur2 = cur[:]
            for i, letter in enumerate(col):
                cur2[i] = cur2[i] + letter

            if is_sorted(cur2):
                cur = cur2
            else:
                ans += 1

        return ans
