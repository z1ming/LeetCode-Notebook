class Solution:
    def newInteger(self, n: int) -> int:

        temp = ''

        while n > 0:

            temp+=str(n%9)

            n = n//9
        
        temp = temp[::-1]

        return(int(temp)) 