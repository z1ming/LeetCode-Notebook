import threading
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n+1
        self.Zero=threading.Semaphore(1)
        self.Even=threading.Semaphore(0)
        self.Odd=threading.Semaphore(0)
        
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,self.n):
            self.Zero.acquire()
            printNumber(0)
            if i%2==1:
                self.Odd.release()
            else:
                self.Even.release()
            
            
            
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,self.n):
            if i%2==0:
                self.Even.acquire()
                printNumber(i)
                self.Zero.release()
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,self.n):
            if i%2==1:
                self.Odd.acquire()
                printNumber(i)
                self.Zero.release()

