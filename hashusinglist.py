class Hash:
    def __init__(self,size = 7):
        self.data_set = [None] * size
        self.size = size
    def _hash(self,key):
        my_hash = 0
        for i in key:
            my_hash = my_hash + ord(i)
        index = my_hash % self.size
        return index
    def set(self,key,value):
        index = self._hash(key)
        if self.data_set[index] == None:
            self.data_set[index] = []
        self.data_set[index].append([key,value])
    def get(self,key):
        index = self._hash(key)
        if self.data_set[index] is not None:
            for i in range(len(self.data_set[index])):
                    if self.data_set[index][i][0] == key:
                         return self.data_set[index][i][1]
        return None