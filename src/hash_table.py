class HashTable():
    """Maps keys to values using Python's hash function to enable lookup
    in O(1) time. 
    
    Collisions are resolved with the open addressing technique with
    linear probing.
    """
    def __init__(self, size=1000):
        """Initializes a HashTable object.

        Parameters:
        size (int): The number of entries to allow

        Returns:
        None

        """
        self.__buckets = [None] * size
        self.__assigned_indices = []

    def insert(self, key, value):
        """Inserts a new entry into the hash table.

        Parameters:
        key (any): The key to be inserted into the hash table

        value (any): The value associated with the provided key

        Returns:
        None

        """
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
    
    def __get_idx(self, key):
        """Returns the index of the bucket in which a key-value pair is
        stored.

        Parameters:
        key (any): The key whose assigned bucket index is to be
        retrieved

        Returns:
        int: The index of the bucket in which the key value-pair is
        stored

        """
        hash_idx = hash(key) % len(self.__buckets)
        search_idx = hash_idx
        while self.__buckets[search_idx][0] != key:
            search_idx += 1
            if search_idx == len(self.__buckets):
                search_idx = 0
            if search_idx == hash_idx:
                raise ValueError("Key {0} not found in HashTable".format(key))
    
    def calc_acmpl(self):
        """Calculates the average collisions per lookup for the hash
        table in its current form.

        A collision occurs when two or more keys are mapped to the same
        index by the hash function.

        """
        n_collisions = 0
        for assigned_idx in self.__assigned_indices:
            hash_idx = hash(self.__buckets[assigned_idx][0]) % len(self.__buckets)
            while hash_idx != assigned_idx:
                n_collisions += 1
                hash_idx += 1
                if hash_idx == len(self.__buckets):
                    hash_idx = 0

        return n_collisions / len(self.__assigned_indices)
    
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
    
    def __getitem__(self, key):
        return self.__buckets[self.__get_idx(key)][1]