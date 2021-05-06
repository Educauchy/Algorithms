from typing import List, Optional


class StackOverflow(Exception):
    pass

class StackUnderflow(Exception):
    pass

class Stack():
    def __init__(self, capacity: int = 10):
        """
        :param capacity: Maximum capacity of stack

        :var top: Index of the current top element
        :var container: Container for elements
        """
        self.capacity: int = capacity
        self.top: Optional[int] = None
        self.container: List[int] = list()

    def is_empty(self) -> bool:
        return self.top is None

    def push(self, item) -> None:
        if self.top is not None and self.top + 1 == self.capacity:
            raise StackOverflow('Too much elements for the stack')
        else:
            self.container.append(item)
            if self.top is None:
                self.top = 0
            else:
                self.top += 1

    def pop(self) -> int:
        if self.top is None:
            raise StackUnderflow('No elements in the stack')
        else:
            self.top -= 1
            if self.top < 0:
                self.top = None
            return self.container.pop()

    def top(self) -> int:
        return self.container[self.top]

    def __str__(self):
        return 'Stack(capacity={}, [{}])'.format(self.capacity, ', '.join(str(el) for el in self.container))

    def __repr__(self):
        pass

if __name__ == '__main__':
    st = Stack(10)
    st.push(1)
    print(st)
    st.push(3)
    print(st)
    st.push(5)
    print(st)
    st.push(7)
    print(st)
    st.pop()
    print(st.is_empty())
    print(st)