class Node:

    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_to_node = dict()
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]
        self.node_use(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self.key_to_node[key].val = value
            self.node_use(self.key_to_node[key])
            
        
        else:
            if self.size == self.capacity:
                node_to_del = self.tail.prev
                del self.key_to_node[node_to_del.key]
                self.node_delete(self.node_del)
                self.size -= 1
            
            node_to_add = Node(value, key)
            self.key_to_node[key] = node_to_add
            self.node_insert_front(node_to_add)
            self.size += 1
    
    def node_use(self, node):
        self.node_delete(node)
        self.node_insert_front(node)

    def node_delete(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def node_insert_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)