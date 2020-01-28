class Node:
    def __init__(self):
        self.content = ""
        self.isFile = False
        self.sub = {}

class FileSystem:

    def __init__(self):
        self.root = Node()

    def ls(self, path: str) -> List[str]:
        curr = self.root
        p = [x for x in path.split('/') if x]
        
        for x in p:
            print(x)
            if curr.sub.get(x) is None:
                return []
            curr = curr.sub[x]
            
        if curr.isFile is True:
            return [p[-1]]
        else:
            res = [x for x in curr.sub]
            res.sort()
            return res
           

    def mkdir(self, path: str) -> None:
        curr = self.root
        p = [x for x in path.split('/') if x]

        for x in p:
            if curr.sub.get(x) is None:
                curr.sub[x] = Node()
            curr = curr.sub[x]
        
    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.root
        p = [x for x in filePath.split('/') if x]

        for x in p:
            if curr.sub.get(x) is None:
                curr.sub[x] = Node()
            curr = curr.sub[x]
        
        curr.isFile = True
        curr.content += content
        
        
    def readContentFromFile(self, filePath: str) -> str:
        curr = self.root
        p = [x for x in filePath.split('/') if x]
        
        for x in p:
            if curr.sub.get(x) is None:
                return ""
            curr = curr.sub[x]
        
        if curr.isFile is not True:
            return ""
        else:
            return curr.content