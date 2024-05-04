class A:
    def __init__(self):
        print("Start A.__init__")


class B(A):
    def __init__(self):
        print("Start B.__init__")
        super().__init__()
        print("Finish B.__init__")


class C(A):
    def __init__(self):
        print("Start C.__init__")
        super().__init__()
        print("Finish C.__init__")


class D(B, C):
    def __init__(self):
        print("Start D.__init__")
        super().__init__()
        print("Finish D.__init__")


d = D()
