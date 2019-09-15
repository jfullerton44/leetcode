class Node:
    def __init__(self, key:int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

        
class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.previous = self.head
        
    def get(self, key: int) -> int:
        if(key in self.dict):
            node = self.dict[key]
            self.removeNode(node)
            self.addNode(node)
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        node = None
        if key in self.dict:
            self.removeNode(self.dict[key])
            node = Node(key,value)
            self.addNode(node)
            return
        
        if(len(self.dict)==self.capacity):
            print("Removing: ", self.tail.previous.key)
            self.removeNode(self.tail.previous)
        node = Node(key,value)
        self.addNode(node)
        return
    
    def removeNode(self, node):
        node.previous.next =  node.next
        node.next.previous =  node.previous
        self.dict.pop(node.key)
        
    def addNode(self, node):
        self.head.next.previous = node
        node.next = self.head.next
        self.head.next = node
        node.previous = self.head
        self.dict[node.key] = node
        
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)