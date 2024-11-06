class Transaction:
    def __init__(self, t_amt,t_num):
        self.t_amt = t_amt
        self.t_num = t_num

    def compare_to(self, t):
        if self.t_amt > t.t_amt:
            return 1
        elif self.t_amt < t.t_amt:
            return -1
        else:
            return 0


class MaxHeap:
    def __init__(self, capacity=10):
            if capacity <= 0 or capacity > 10000:
                raise ValueError('Capacity must be between 0 and 10000')
            self.capacity = capacity
            self.transactions = [None] * (capacity+1)
            self.current_size = 0


    def isEmpty(self):
        return self.current_size == 0
    def swap(self, i,j):
        temp = self.transactions[i]
        self.transactions[i] = self.transactions[j]
        self.transactions[j] = temp

    def swim(self, k):
        while k > 1 and self.transactions[k].compare_to(self.transactions[k // 2]) > 0:
            self.swap(k, k // 2)
            k = k // 2

    def sink(self, k):
        while 2 * k <= self.current_size:
            j = 2 * k  # left child
            if j < self.current_size and self.transactions[j].compare_to(self.transactions[j + 1]) < 0:
                j += 1  # right child
            if self.transactions[k].compare_to(self.transactions[j]) >= 0:
                break
            self.swap(k, j)
            k = j

    def insert(self,k):
        if self.current_size >= self.capacity:
            raise Exception('Cannot insert more than capacity')
        self.current_size += 1
        self.transactions[self.current_size] = k
        self.swim(self.current_size)

    def removeMax(self):
        if self.isEmpty():
            raise Exception('the heap is empty')
        temp = self.transactions[1]
        self.transactions[1] = self.transactions[self.current_size]
        self.transactions[self.current_size]= None
        self.current_size -= 1
        self.sink(1)
        return temp
    