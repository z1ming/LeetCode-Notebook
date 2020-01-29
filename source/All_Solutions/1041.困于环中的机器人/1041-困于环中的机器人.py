class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        d = 0  #方向，0上1右2下3左
        x = 0
        y = 0
        while True:
            for i in instructions:
                if i == 'R':
                    d+=1
                elif i == 'L':
                    d-=1
                else:
                    if d%4==1:
                        x+=1
                    elif d%4==3:
                        x-=1
                    elif d%4==0:
                        y+=1
                    else:
                        y-=1
            if d%4==0:
                break
        return (x,y)==(0,0)