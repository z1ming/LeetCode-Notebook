import queue

class FooBar:
    def __init__(self, n):
        self.n = n
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        self.q1.put('')


    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.q1.get()
            printFoo()
            self.q2.put('')


    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.q2.get()
            printBar()
            self.q1.put('')
