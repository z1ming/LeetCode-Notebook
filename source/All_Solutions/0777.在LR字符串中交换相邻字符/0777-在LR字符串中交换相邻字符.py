class Solution:
    def canTransform(self, start: str, end: str) -> bool:

        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        n=len(start)
        if len(end)!=n:
            return False
        i=j=0
        start+='A'
        end+='A'
        while i<n and j<n:
            while start[i]=='X':i=i+1
            while end[j]=='X':j=j+1
            if start[i]!=end[j]:
                return False
            if start[i]=='R' and i>j:
                return False
            if start[i]=='L' and i<j:
                return False
            i+=1
            j+=1
        return True