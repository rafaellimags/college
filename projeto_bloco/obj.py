class Frame(object):

    def __init__(self, color = 0, jk = None):
        self.__color = color
        self.__jk = jk

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_jk(self, color):
        self.__jk = jk

    def get_jk(self):
        return self.__jk


frame_color = Frame()
print(frame_color.get_color())
print(frame_color.get_jk())

