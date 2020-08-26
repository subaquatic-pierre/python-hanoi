import copy


class Disk:
    """ A disk object to be placed on a stack within the game.
    Disks properties are defined by global variable states such as
    total sizes and colors, colors are currently limited to 8 """
    total_sizes = 1

    def colors_gen():
        colors = ['Red', 'Green', 'Blue', 'Yellow',
                  'Brown', 'Purple', 'Pink', 'Orange']
        for color in colors:
            yield color

    colors = colors_gen()

    def __init__(self):
        self.size = self.total_sizes
        try:
            self.color = next(self.colors)
        except StopIteration:
            raise 'Error, end of color choices'
        Disk.total_sizes = Disk.total_sizes * 2

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        """ Color of the disk must be a string """
        if not type(color) == str:
            raise TypeError(
                f'The type of the color must be a string, {repr(self)}')
        self.__color = color

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        """ Size of the disk must be an integer """
        if not type(size) == int:
            raise TypeError(f'Size must be an integer {repr(self)}')
        self.__size = size

    def __str__(self):
        return f'{self.color} - {self.size}'

    def __repr__(self):
        try:
            return f'{self.color} - {self.size}'
        except AttributeError:
            return f'Disk(int, str)'
