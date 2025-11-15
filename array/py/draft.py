class Foo:
    def __init__(self, x: int):
        self.x = x

    def __repr__(self):
        return f'Foo({self.x})'
    
    lista_vazia_primitiva: list[int] = []
    print("lista_vazia_primitiva:", lista_vazia_primitiva, "tamanho:", len(lista_vazia_primitiva))

