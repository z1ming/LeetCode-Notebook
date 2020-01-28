import re
class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        return re.sub(f"\\b({'|'.join(dict)})\w*", r'\1', sentence)