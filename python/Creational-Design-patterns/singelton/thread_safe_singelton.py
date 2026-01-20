import threading

class SingeltonThread:
    _instance = None
    _lock = threading.Lock() # class level lock 


    def __new__(self):
        if self._instance is None:
            with self._lock:
                if self._instance is None:
                    self._instance = super(SingeltonThread, self).__new__(self)
        
        return self._instance

    