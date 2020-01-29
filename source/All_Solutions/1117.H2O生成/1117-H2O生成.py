import queue

class H2O:
    def __init__(self):
        self.h = queue.Queue(2)
        self.o = queue.Queue(1)


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h.put(0)
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        if self.h.full() and self.o.full():
            self.h.get()
            self.h.get()
            self.o.get()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o.put(0)
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        if self.h.full() and self.o.full():
            self.o.get()
            self.h.get()
            self.h.get()


