from ast import Index


class Vector:

    def __init__(self, a, b):
        self.a = a
        self.b = b


    def __str__(self):
        return f"({self.a};{self.b})"


    def __len__(self):
        return 2


    def __getitem__(self, index):
        if index == 0:
            return self.a
        elif index == 1:
            return self.b
        else:
            raise IndexError("Los vectores tienen solo 2 elementos")


    def __setitem__(self, indice, valor):
        if indice == 0:
            self.a = valor
        elif indice == 1:
            self.b = valor
        else:
            raise IndexError("Los vectores tienen solo 2 elementos")


    def __iter__(self):
        yield self.a
        yield self.b


vector1 = Vector(1,2)

# print(vector1)
# print( len(vector1) )
print( vector1[0] )

vector1[0] = 10
vector1[1] = 20

print(vector1)


for punto in vector1:
    print("Valor de punto:", punto)
