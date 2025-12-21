class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        if self.head is None or self.tail is None:
            return -1

        pointer = self.head
        for i in range(index):
            if pointer is not None:
                pointer = pointer.next

        if pointer is not None:
            return pointer.value

        return -1

    def addAtHead(self, val: int) -> None:
        if self.head is None:
            self.head = Node(value=val, next=None, prev=None)
            self.tail = self.head

        else:
            newHead = Node(value=val, next=self.head)
            self.head.prev = newHead
            self.head = newHead

        self.length = self.length + 1

    def addAtTail(self, val: int) -> None:
        if self.tail is None:
            self.tail = Node(value=val)
            self.head = self.tail
        else:
            newTail = Node(value=val, prev=self.tail)
            self.tail.next = newTail
            self.tail = newTail

        self.length = self.length + 1

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = Node(value=val)
        pointer = self.head

        if index > self.length:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            for i in range(index):
                pointer = pointer.next
            newNode.next = pointer
            newNode.prev = pointer.prev
            pointer.prev.next = newNode
            pointer.prev = newNode
            self.length = self.length + 1

    def deleteAtIndex(self, index: int) -> None:
        pointer = self.head

        if index >= self.length:
            return

        for i in range(index):
            pointer = pointer.next

        if index == 0:
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif index == self.length - 1:
            if self.tail.prev is None:
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
        else:
            pointer.prev.next = pointer.next
            pointer.next.prev = pointer.prev

        self.length = self.length - 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
