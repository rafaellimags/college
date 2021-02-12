class Frame:

    def __init__(self, color=(0, 0, 0), filled=False, size=None, density=0):
        self.__color = color
        self.__filled = filled
        self.__size = size
        self.__density = density

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_filled(self, filled):
        self.__filled = filled

    def get_filled(self):
        return self.__filled

    def set_size(self, size):
        self.__size = size

    def get_size(self):
        return self.__size

    def set_density(self, density):
        self.__density = density

    def get_density(self):
        return self.__density


class Fill(object):

    def __init__(self, color=(0, 0, 0), size=None):
        self.__color = color
        self.__size = size

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_size(self, size):
        self.__size = size

    def get_size(self):
        return self.__size
