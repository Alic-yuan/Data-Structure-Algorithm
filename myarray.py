from typing import Optional


class MyArray:

    def __init__(self, capacity: int):
        self._data = []
        self._count = 0
        self._capacity = capacity

    def __getitem__(self, position:int) -> int:
        return self._data[position]

    def find(self, index: int) -> Optional[int]:
        if index >= self._count or index <= -self._count:
            return None
        return self._data[index]

    def delete(self, index: int) -> bool:
        if index >= self._count or index <= -self._count:return False
        self._data[index:-1] = self._data[index+1:]
        self._count -= 1
        return True

    def insert(self, index: int, value: int) -> bool:
        if index >= self._count or index <= -self._count: return False
        if self._capacity == self._count: return False
        self._data.insert(index, value)
        self._count += 1
        return True

    def insert_to_tail(self, value: int) -> bool:
        if self._count == self._capacity: return False
        self._data.append(value)
        self._count += 1
        return True

    def __repr__(self) -> str:
        return " ".join(str(num) for num in self._data[:self._count])

    def print_all(self):
        for num in self._data[:self._count]:
            print(f"{num}", end=" ")
        print("\n", flush=True)

if __name__ == '__main__':
    a = MyArray(6)
    for i in range(5):
        a.insert_to_tail(i)
    a.insert(4, 5)
    a.print_all()
    # a.delete(2)
    # print(a)