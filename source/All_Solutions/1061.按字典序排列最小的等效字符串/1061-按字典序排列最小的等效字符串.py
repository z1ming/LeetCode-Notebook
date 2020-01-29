class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        all_sets = self.build_str_2_sets(A, B)
        res_sets = self.merge_all_sets_till_inmergable(all_sets)
        res_word = []
        for letter in S:
            find = False
            for m_set in res_sets:
                if letter in m_set:
                    res_word.append(sorted(m_set)[0])
                    find = True
            if not find:
                res_word.append(letter)
        return ''.join(res_word)
    def build_str_2_sets(self,a, b):
        list_a = list(a)
        list_b = list(b)
        all_sets = []
        for index, letter in enumerate(list_a):
            all_sets.append({letter, list_b[index]})
        return all_sets
    def merge_all_sets_till_inmergable(self,sets_list):
        def simple_merge_sets_list(set_list):
            for m_set in set_list:
                if set_list[-1] & m_set != set():
                    set_list[-1] = set_list[-1] | m_set
            temp_set = set_list.pop()
            set_list = [temp_set] + [i for i in set_list if not i.issubset(temp_set)]
            return set_list
        while True:
            len1 = len(sets_list)
            sets_list = simple_merge_sets_list(sets_list)
            len2 = len(sets_list)
            if len1 == len2:
                break
        return sets_list

