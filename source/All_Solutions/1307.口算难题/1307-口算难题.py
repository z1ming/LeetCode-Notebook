class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        used, carry = [False] * 10, [0] * 10
        lead_zero, rep = dict(), dict()

        for word in words:
            if len(word) > len(result):
                return False
            for ch in word:
                rep[ch] = -1
                lead_zero[ch] = max(lead_zero.get(ch, 0), 0)
            if len(word) > 1:
                lead_zero[word[0]] = 1
        for ch in result:
            rep[ch] = -1
            lead_zero[ch] = max(lead_zero.get(ch, 0), 0)
        if len(result) > 1:
            lead_zero[result[0]] = 1
        
        def dfs(pos, iden, length):
            if pos == length:
                return carry[pos] == 0
            elif iden < len(words):
                sz = len(words[iden])
                if sz < pos or rep[words[iden][sz - pos - 1]] != -1:
                    return dfs(pos, iden + 1, length)
                else:
                    ch = words[iden][sz - pos - 1]
                    for i in range(lead_zero[ch], 10):
                        if not used[i]:
                            used[i], rep[ch] = True, i
                            check = dfs(pos, iden + 1, length)
                            used[i], rep[ch] = False, -1
                            if check:
                                return True
                    return False
            else:
                left = carry[pos] + sum(rep[word[len(word) - pos - 1]] for word in words if len(word) > pos)
                carry[pos + 1], left = left // 10, left % 10
                ch = result[len(result) - pos - 1]
                if rep[ch] == left:
                    return dfs(pos + 1, 0, length)
                elif rep[ch] == -1 and not used[left] and not (lead_zero[ch] == 1 and left == 0):
                    used[left], rep[ch] = True, left
                    check = dfs(pos + 1, 0, length)
                    used[left], rep[ch] = False, -1
                    return check
                else:
                    return False

        return dfs(0, 0, len(result))

