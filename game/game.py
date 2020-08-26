from .disk import Disk
from .stack import Stack
from time import sleep


class Game:
    """ Creates the entire game initial state, takes as input
    a starting number of disks. It sets up all the stacks and creates
    all the disks needed to play the game """

    def __init__(self, disks):
        self.origin_stack = Stack('Origin')
        self.spare_stack = Stack('Middle')
        self.target_stack = Stack('Target')
        self.build_stack(self.origin_stack, disks)

    @property
    def get_disks(self):
        return self.disks

    @property
    def get_origin_stack(self):
        return self.origin_stack

    @property
    def get_target_stack(self):
        return self.target_stack

    @property
    def get_spare_stack(self):
        return self.spare_stack

    def build_stack(self, stack, disks):
        """ Build the initial stack of disks on the origin """
        self.disks = [Disk() for disk in range(disks)]
        for disk in reversed(self.disks):
            stack.add_disk(disk)

    def move(self, from_stack, to_stack):
        """ Makes an individual move of a disk from stack to
        another stack """
        disk = from_stack.remove_disk()
        to_stack.add_disk(disk)
        # print(from_stack, to_stack)
        self.print_game()

    def print_game(self):
        print('\n----------------------------\n')
        print(f'{self.origin_stack}')
        print(f'{self.spare_stack}')
        print(f'{self.target_stack}')
        print('\n----------------------------\n')

    def play_game(self, disks, origin_stack, spare_stack, target_stack):
        """ Recursive function which implements logic to break the stacks
        into smaller sizes, once the stack is of size zero, the function
        then calls the move function to move than disk, and then continues
        until all disks are moved """
        if len(disks) == 0:
            pass
        else:
            self.play_game(disks[:-1], origin_stack,
                           target_stack, spare_stack)
            sleep(.5)
            self.move(origin_stack, target_stack)
            self.play_game(disks[:-1], spare_stack,
                           origin_stack, target_stack)
