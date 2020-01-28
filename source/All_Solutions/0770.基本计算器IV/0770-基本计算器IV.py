import re
from collections import namedtuple
left = r'(?P<LEFT>\()'
right = r'(?P<RIGHT>\))'
var = r'(?P<VAR>[a-z]+)'
num = r'(?P<NUM>\d+)'
add = r'(?P<ADD>\+)'
sub = r'(?P<SUB>\-)'
mul = r'(?P<MUL>\*)'
ws = r'(?P<WS> +)'
pt=  re.compile('|'.join([left,right,var,ws,num,add,sub,mul]))

token = namedtuple('token',['type','value'])

def genToken(s):
    scanner = pt.scanner(s)
    for i in iter(scanner.match,None):
        if i.lastgroup!='WS':yield token(i.lastgroup,i.group(0))

'''grammar
expr -> expr {'+'|'-'} term | term
term -> term '*' item | item
item -> num | var | '(' expr ')'
'''  

class Solution(object):
    def init(self,s):
        self.token = [i for i in genToken(s)]
        self.lookahead = 0
    def match(self,curType=None):
        sym = self.token[self.lookahead]
        #print(sym,curType)
        if curType is None or sym.type ==curType:
            self.lookahead +=1            
            return sym.value
        raise Exception('Invalid input string')
    def isType(self,*s):
        sym = self.token[self.lookahead]
        return any(sym.type==i for i in s)
    def parse(self):
        dic = self.term()
        while  self.lookahead<len(self.token) and not self.isType('RIGHT'): # terminate symbol
            assert self.isType('SUB','ADD')
            sign =1 if  self.match()=='+' else -1
            var = self.term()
            for i in var:
                if i in dic:
                    dic[i]+=var[i]*sign
                else:
                    dic[i]= var[i]*sign
        return dic
    def term(self):
        li = []
        dic =self.item()
        while  self.lookahead<len(self.token) and self.isType('MUL'):
            self.match()
            li.append(self.item())
        for d2 in li:
            newDic = {}
            for v1 in dic:
                for v2 in d2:
                    s = ''
                    if v1=='':
                        s=v2
                    elif v2=='':
                        s=v1
                    else:
                        s = '*'.join(sorted(v1.split('*')+v2.split('*')))
                    if s in newDic:
                        newDic[s]+=dic[v1]*d2[v2]
                    else:
                        newDic[s]=dic[v1]*d2[v2]
            dic=newDic
        return dic
    
    def item(self):
        if self.isType('NUM'):
            return {'':int(self.match())}
        elif self.isType('VAR'):
            name = self.match()
            if name in self.var:
                return {'':self.var[name]}
            else:return {name:1}
        elif self.isType('LEFT'):
            self.match()
            dic= self.parse()
            self.match('RIGHT')
            return dic
        else:
            print(self.token[self.lookahead])
            raise Exception('invalid string')   
    def basicCalculatorIV(self, expression, evalvars, evalints):
        """
        :type expression: str
        :type evalvars: List[str]
        :type evalints: List[int]
        :rtype: List[str]
        """
        self.var = dict(zip(evalvars,evalints))
        self.init(expression)
        dic =  self.parse()
        n= dic.pop('') if '' in dic else 0
        ret = []
        li = sorted(dic,key=lambda s:(-s.count('*'),s))
        for i in li:
            if dic[i]!=0: 
                s = str(dic[i])
                ret.append(s+ ('*'+i) if i else s)
        if n!=0:ret.append(str(n))
        return ret