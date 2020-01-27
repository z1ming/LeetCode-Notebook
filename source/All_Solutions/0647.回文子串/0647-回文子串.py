class Solution:
    def countSubstrings(self, s: str) -> int:
        # 先把字符串转换成(字符,计数)的列表形式，如'aabccc'变为[('a',2),('b',1),('c',3)]，后续加速计算
        counts, count = [], 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
            else:
                counts.append((s[i], count))
                count = 1
        counts.append((s[-1], count))
        res = 0
        for i in range(len(counts)):
            res += counts[i][1]*(counts[i][1]+1)//2
            # 单个(字符,计数)能构成的回文串个数，排列组合知识，即在x个字母构成的x+1个空里选两个隔板截取子串
            # 即组合数C_(x+1)^2，如计数为3，则构成(3+1)*3/2=6个
            j = 1  # 以counts[i]为中心串后往两边考虑的扩张(字符，计数）个数
            while i-j >= 0 and i+j < len(counts):
                left, right = counts[i-j], counts[i+j]
                if left[0] == right[0]:  # 左右字符相同
                    if left[1] != right[1]:  # 计数不同
                        res += min(left[1], right[1])  # 加上最小值
                        break  # 停止扩张
                    else:
                        res += left[1]  # 左右计数相同，则直接加上其计数
                        j += 1  # 继续扩张
                else:
                    break  # 字符不同直接停止扩张
        return res

