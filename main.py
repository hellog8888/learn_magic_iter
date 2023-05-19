class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            self.last.next = obj
        self.last = obj

    def push_front(self, obj):
        if self.top is None:
            self.last = self.top = obj
        else:
            obj.next = self.top
            self.top = obj

    def __len__(self):
        return sum(1 for _ in self)

    def get_index(self, indx):
        if type(indx) != int or not (0 <= indx < len(self)):
            raise IndexError('неверный индекс')
        for i, obj in enumerate(self):
            if i == indx:
                return obj

    def __getitem__(self, item):
        return self.get_index(item).data

    def __setitem__(self, key, value):
        self.get_index(key).data = value

    def __iter__(self):
        h = self.top
        while h:
            yield h
            h = h.next