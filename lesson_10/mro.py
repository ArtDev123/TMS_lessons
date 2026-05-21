class A:
    def process(self) -> None:
        print("A")


class B(A):
    def process(self) -> None:
        print("B")


class C(A):
    def process(self) -> None:
        print("C")


class D(B, C):  # D наследует B и C (ромбовидное наследование)
    pass


obj = D()
obj.process()  # Выведет "B". Почему? Смотрим MRO!
print(D.__mro__)
# Порядок С3 линеаризации: D -> B -> C -> A -> object
