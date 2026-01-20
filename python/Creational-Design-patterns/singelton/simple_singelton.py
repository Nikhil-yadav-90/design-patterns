

class Singelton:
    _instance = None

# # using constructor approach

# # !this is wrong approach it will cause two different objects with shared data 

#     def __init__(self):
#         if self._instance is None:
#             self._instance = self
        



#  Using new dungeon method right Approach
    def __new__(self):
        if self._instance is None:
            print (" Object is created")
            self._instance = super(Singelton, self).__new__(self)
        return self._instance