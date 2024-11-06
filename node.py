from max_heap import MaxHeap

class Node:
    def __init__(self, date, capacity=100):
        self.date = self.date_dating(date)
        self.next_hash = None
        self.prev_hash = None
        self.root = MaxHeap(capacity)
        self.transaction_num = 1

    def date_dating(self, date):
        if len(date) == 7:
            return "0" + date
        return date

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = self.date_dating(date)

    def __str__(self):
        return self.date

