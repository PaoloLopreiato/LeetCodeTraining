"""
Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
"""
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = {}  # Map key to Node
        
        # Dummy nodes for boundary (left = LRU, right = MRU)
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        """ Remove a node from the linked list """
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        """ Insert a node at the right end (MRU) of the linked list """
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key):
        """
        Get the value of the key if the key exists in the cache, otherwise return -1.
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            # Remove the node and insert it to the right (MRU position)
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key, value):
        """
        Put the key and value in the cache. If the capacity is exceeded, evict the least recently used item.
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            # If key exists, remove it and insert the new value as MRU
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            # Evict the LRU item from the cache (leftmost item in the linked list)
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)