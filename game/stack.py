from .disk import Disk
from copy import deepcopy


class Stack:
    total_stacks = 0

    def __init__(self, name):
        self.disks = []
        self.name = name
        self.index = Stack.total_stacks
        Stack.total_stacks += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def get_disks(self):
        return self.disks

    def add_disk(self, disk):
        # if not isinstance(disk, Disk):
        #     raise TypeError('Type of object must be a Disk')
        self.disks.append(disk)

    def remove_disk(self):
        try:
            return self.disks.pop()
        except IndexError:
            pass

    def peek_top(self):
        return deepcopy(self.disks[-1])

    def __str__(self):
        return f'{self.name} - {[disk for disk in self.get_disks]}'
