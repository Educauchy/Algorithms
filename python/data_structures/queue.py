from typing import List, Optional


class QueueOverflow(Exception):
    pass

class QueueUnderflow(Exception):
    pass

class Queue():
    def __init__(self, capacity: int = 10):
        """
        :param capacity: Maximum capacity of queue

        :var front: Index of the current front element
        :var container: Container for elements
        """
        self.capacity: int = capacity
        self.front: Optional[int] = None
        self.container: List[int] = list()

    def is_empty(self) -> bool:
        return self.front is None

    def enqueue(self, item) -> None:
        if self.front is not None and self.front + 1 == self.capacity:
            raise QueueOverflow('Too much elements for the queue')
        else:
            self.container.insert(0, item)
            if self.front is None:
                self.front = 0
            else:
                self.front += 1

    def dequeue(self) -> int:
        if self.front is None:
            raise QueueUnderflow('No elements in the queue')
        else:
            self.front -= 1
            if self.front < 0:
                self.front = None
            return self.container.pop()

    def front(self) -> int:
        return self.container[self.front]

    def __str__(self):
        return 'Queue(capacity={}, [{}])'.format(self.capacity, ', '.join(str(el) for el in self.container))

    def __repr__(self):
        pass

if __name__ == '__main__':
    st = Queue(10)
    st.enqueue(1)
    print(st)
    st.enqueue(3)
    print(st)
    st.enqueue(5)
    print(st)
    st.enqueue(7)
    print(st)
    st.dequeue()
    print(st.is_empty())
    print(st)
