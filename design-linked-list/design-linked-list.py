class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        if index < 0 or index > 1000:
            return -1
        currIdx = 0
        temp = self.head
        while temp is not None:
            if index == currIdx:
                return temp.value
            currIdx += 1
            temp = temp.next
        return -1
        

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
            

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        temp = self.head
        if temp is None:
            self.addAtHead(val)
            return
        
        while temp.next is not None:
            temp = temp.next
        temp.next = node
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > 1000:
            return
        if index == 0:
            self.addAtHead(val)
            return
        temp = self.head
        if temp is None:
            return
        
        node = Node(val)
        currIdx = 1
        
        while temp.next is not None:
            if index == currIdx:
                node.next = temp.next
                temp.next = node
                return
            currIdx += 1
            temp = temp.next
        
        if index == currIdx:
            temp.next = node
        
                

    def deleteAtIndex(self, index: int) -> None:
        temp = self.head
        
        if temp is None:
            return
        if index == 0:
            self.head = self.head.next
            return
        
        currIdx = 1
        while temp.next is not None:
            if index == currIdx:
                temp.next = temp.next.next
                break
            temp = temp.next
            currIdx += 1
        
        
    
    def printLinkedList(self) -> None:
        temp = self.head
        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)