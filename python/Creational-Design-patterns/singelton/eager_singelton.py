class EagerSingelton:
    _instance = object()

    @classmethod
    def get_instance(self):
        return self._instance