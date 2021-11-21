class Student:
    def __init__(self, id : int, name : str) -> None:
        self._id = id
        self._name = name
    def display(self) -> None:
        print('Id:', self._id, 'Name:', self._name)