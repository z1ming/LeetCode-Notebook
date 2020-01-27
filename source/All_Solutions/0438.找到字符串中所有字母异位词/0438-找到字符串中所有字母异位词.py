class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 滑动窗口模板解决此类问题
        # ord("a") = 97
        sArr = [ord(i)-97 for i in s]
        pArr = [ord(i)-97 for i in p]
        hash = [0 for i in range(26)]
        m,n  = len(s),len(p)
        # 构建hash映射数组
        for i in range(n):
            hash[pArr[i]] += 1
        l,r,count,res= 0,0,0,[]
        while r < m:
            hash[sArr[r]] -= 1
            if hash[sArr[r]] >= 0: 
                count += 1
            # 移动左指针
            if r > n - 1:
                hash[sArr[l]] += 1
                if hash[sArr[l]] > 0: 
                    count -= 1
                l += 1
            if count == n:
                res.append(l)
            r += 1            
        return res

