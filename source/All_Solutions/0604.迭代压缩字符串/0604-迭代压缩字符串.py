class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.comp = compressedString
        self.p_letter = 0
        self.p_num = 1
        self.currL = 0
        if self.comp!="":
            while self.p_num < len(self.comp) and self.comp[self.p_num].isdigit():
                self.p_num += 1
            self.currL = int(self.comp[self.p_letter+1:self.p_num])

    def next(self):
        """
        :rtype: str
        """
        if not self.hasNext(): return ' '
        res = self.comp[self.p_letter]
        self.currL -= 1
        if self.currL == 0:
            self.p_letter = self.p_num
            self.p_num = self.p_letter + 1
            if self.p_letter < len(self.comp):
                while self.p_num < len(self.comp) and self.comp[self.p_num].isdigit():
                    self.p_num += 1
                self.currL = int(self.comp[self.p_letter+1:self.p_num])
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.currL>0:
            return True
        return False