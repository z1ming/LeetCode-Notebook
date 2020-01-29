class Solution(object):
    def leadsToDestination(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        for i in range(len(edges)):
            if edges[i][0] == destination:
                return False
        return self.check(edges, [source], destination)
        
    def check(self, e, s, d):
        n = []
        start = s[-1]
        if start == d:
            return True
        for i in e:
            if i[0] == start:
                if i[1] in s:
                    return False
                elif i[1] not in n:
                    n.append(i[1])
        if not n:
            return False
        for i in n:
            if self.check(e,s+[i],d) == False:
                return False
        return True