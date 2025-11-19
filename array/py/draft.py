class Foo:
    def __init__(self, x: int):
        self.x = x

    def __str__(self):
        return f'Foo({self.x})'
    
    def __repr__(self):
        return str(self)
    
    #vazia
    lista_vazia: list[int] = []
    lista_vazia_obj: list[Foo] = []

    #preenchida array
    lista_preenchida: list[int] = [1,2,3,4,5]
    lista_preenchida_obj: list[Foo] = [Foo(1), Foo(2), Foo(3), Foo(4), Foo(5)]

    #size do array
    tam = len(lista_preenchida)

    lista_preenchida.append(6)
    ultimo = lista_preenchida.pop()

    lista_preenchida.insert(0,999)
    primeiro = lista_preenchida.pop(0)

    lista_preenchida.insert(2,123)
    removido = lista_preenchida.pop(2)

    str_formatada = ", ".join(map(str, lista_preenchida))
kkkokojiiii


