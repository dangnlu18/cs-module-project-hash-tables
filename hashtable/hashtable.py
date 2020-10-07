class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.count = 0
        if capacity >= MIN_CAPACITY:
            self.data = [None] * capacity
            self.capacity = capacity
        else:
            [None]*capacity
            MIN_CAPACITY



    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.count / self.get_num_slots()


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        prime = 1099511628211
        basis = 14695981039346656037

        hash_id = basis
        enc_key = key.encode()

        for byte in enc_key:
            hash_id = hash_id * prime
            hash_id = hash_id ^ prime
        return hash_id



    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here

        hash = 5381
        for char in key:
            hash = hash * 33 + ord(char)    
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        hash_index = self.hash_index(key)

        slot = HashTableEntry(key, value)

        if not self.data[hash_index]:
            self.data[hash_index] = slot
            self.count +=1
        else:
            curr_node = self.data[hash_index]
            while curr_node.key != key and curr_node.next:
                curr_node = curr_node.next
                if curr_node.key ==key:
                    curr_node.value = curr_node.value
                else:
                    curr_node.next = slot
                    self.count +=1
                    if self.get_load_factor() > 0.7:
                        self.resize(self.capacity*2)




    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        prev_head = None
        hash_index = self.hash_index(key)

        curr_node = self.data[hash_index]

        if not curr_node:
            print('does not exist')

        elif not curr_node.next:
            self.data[hash_index] = None
            self.count -=1
        
        else:
            prev_head
        while curr_node.key != key and curr_node.next:
            prev_head = curr_node
            curr_node = curr_node.next 
        if not curr_node.next:
            prev_head.next = None
            self.count -=1
        else:
            prev_head.next = curr_node.next
            self.count -=1

        if self.get_load_factor() < 0.2:
            self.resize(self.capacity//2)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        hash_index = self.hash_index(key)

        if self.data[hash_index]:
            curr_node = self.data[hash_index]
            while curr_node.key is not key and curr_node.next:
                curr_node = curr_node.next
                
            if not curr_node.next:
                return curr_node
            else:
                return curr_node.value
        else:
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        old = self.data
        self.capacity = new_capacity
        self.data = new_capacity * [None]

        for node in old:
            if node:
                curr_node = node
                while curr_node is True:
                    self.put(curr_node.key, curr_node.value)
                    curr_node = curr_node.next



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
