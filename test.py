class A:
    def __init__(self):
        print("enter A")
        print("leave A")

    def init(self):
        print('init' + self.__str__())
        self.a = [1, 2, 3]


class B(A):
    def __init__(self):
        pass


    def print(self):
        self.a[1] = 5
        print(self.a)


if __name__ == '__main__':
    it = B()
    it.init()
    it.print()
