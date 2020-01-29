import queue
class Foo(object):
    def __init__(self):
        self.q2 = queue.Queue()
        self.q3 = queue.Queue()


    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.q2.put("")


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """

        # printSecond() outputs "second". Do not change or remove this line.
        self.q2.get()
        printSecond()
        self.q3.put("")


    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """

        # printThird() outputs "third". Do not change or remove this line.
        self.q3.get()
        printThird()