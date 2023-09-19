class HashTable():
    """Maps keys to values using Python's hash function to enable lookup
    in O(1) time. 
    
    Collisions are resolved using the open addressing technique with
    linear probing.
    """
    def __init__(self, size=1000):
        self.__buckets = [None] * size
        self.__assigned_indices = []

    def insert(self, key, value):
        if value == None:
            raise ValueError("Invalid value provided; cannot use None")
        
        hash_idx = hash(key) % len(self.__buckets)
        assigned_idx = hash_idx

        # Loop until an empty bucket is found
        while self.__buckets[assigned_idx] != None:
            assigned_idx += 1
            if assigned_idx == len(self.__buckets):
                assigned_idx = 0

            # If we make it back to the original hash index, no empty
            # bucket was available and the new key cannot be inserted
            if assigned_idx == hash_idx:
                raise MemoryError("HashTable full, insertion aborted")
            
        self.__assigned_indices.append(assigned_idx)
        self.__buckets[assigned_idx] = tuple([key, value])

    def __str__(self):
        str_vect = [''] * len(self.__assigned_indices)
        for i in range(len(self.__assigned_indices)):
            prefix = '' if i != 0 else '{'
            suffix = ', ' if i != len(self.__assigned_indices) - 1 else '}'
            str_vect.append(
                prefix
                + str(self.__buckets[self.__assigned_indices[i]][0]) 
                + ': ' 
                + str(self.__buckets[self.__assigned_indices[i]][1]) 
                + suffix)
        str_vect.append('}')
        return ''.join(str_vect)
    
    def __get_idx(self, key):
        hash_idx = hash(key) % len(self.__buckets)
        search_idx = hash_idx
        while self.__buckets[search_idx][0] != key:
            search_idx += 1
            if search_idx == len(self.__buckets):
                search_idx = 0
            if search_idx == hash_idx:
                raise ValueError("Key {0} not found in HashTable".format(key))
    
    def calc_acmpl(self):
        pass
    
    def __getitem__(self, key):
            
        return self.__buckets[self.__get_idx(key)][1]

