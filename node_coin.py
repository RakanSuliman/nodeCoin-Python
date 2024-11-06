from node import Node

class NodeCoin:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def insert(self, node):
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            node.next_head = self.head
            self.head.prev = node
            self.head = node

        self.size += 1

    def get_max(self,date):
        if self.isEmpty():
            return None

        temp = self.head
        while temp != None:
            if temp.get_date() == date:
                return temp
            temp = temp.next_hash

        return None

    def remove_max(self,date):
        if self.isEmpty():
            return None
        temp = self.head
        while temp != None:
            if temp.get_date() == date:
                temp.root.remove_max()
                return temp
            temp = temp.next_hash

    def get_all(self,date):
        current = self.head
        temp = ""

        while current is not None:
            if current.get_date() == date:
                while not current.root.isEmpty():
                    maxt = current.root.removeMax()
                    temp+= f"{maxt.t_amt} {maxt.t_num}\n"
                if (current == self.head):
                    self.head = current.next_hash
                    if self.head is not None:
                        self.head.prev_hash = None
                elif current == self.tail:
                         self.tail = current.prev_hash
                         if self.tail is not None:
                             self.tail.next_hash = None
                else:
                    current.prev_hash.next_hash = current.next_hash
                    current.next_hash.prev_hash = current.prev_hash

                self.size -=1
                return temp.strip()
            current = current.next_hash

        return "-1"
