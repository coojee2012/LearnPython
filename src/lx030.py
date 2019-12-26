class A:
    @classmethod
    def cm(cls):
        print("c")

class B(A):
    __b__ = ""

B.cm()