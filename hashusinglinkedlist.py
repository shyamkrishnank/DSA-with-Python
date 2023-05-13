
class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class hashTable:
    def __init__(self,size = 7):
        self.data_set = [None] * size
        self.size = size
    def hashing(self,key):
        my_hash = 0
        for i in key:
            my_hash = my_hash + ord(i)
        return my_hash
    def set(self,key,value):
        new_node = Node(key,value)
        val = self.hashing(key)
        index = val % self.size
        if self.data_set[index] == None:
            self.data_set[index] = new_node
        else:
            for i in range(self.size):
                index = (val + i) % self.size
                if self.data_set[index] == None:
                    self.data_set[index] = new_node
                    return
    def get(self,key):
        val = self.hashing(key)
        index = val % self.size
        if self.data_set[index].key == key:
            return self.data_set[index].value
        for i in range(self.size):
            index = (val + i) % self.size
            if self.data_set[index].key == key:
                return self.data_set[index].value
