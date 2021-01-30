class DualVector:

    def __init__(self):
        self._coords = [0] * 3

    
    def __len__(self):
        return len(self._coords)

    def __getitem__(self, index):
        if index > len(self):
            raise IndexError
        return self._coords[index]

    def __setitem__(self, key, value):
        if key > len(self._coords):
            raise IndexError
        self._coords[key] = value





a = DualVector()
a[0] = 300

print(a[0])
# print(len(a))

