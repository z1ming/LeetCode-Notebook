class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
      if not head: return
      self.printLinkedListInReverse(head.getNext())
      head.printValue()

