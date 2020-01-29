from queue import Queue
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.q = Queue(capacity)
        

    def enqueue(self, element: int) -> None:
        self.q.put(element)
        

    def dequeue(self) -> int:
        return self.q.get()
        

    def size(self) -> int:
        return self.q.qsize()


