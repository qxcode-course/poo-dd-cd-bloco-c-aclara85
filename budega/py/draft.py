class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
    
class Market:
    def __init__(self, qtd):
        self.counters = [None] * qtd
        self.waiting = []
    
    def __str__(self):
        caixas = []
        for c in self.counters:
            if c is None:
                caixas.append("-----")
            else:
                caixas.append(str(c))

        espera = [str(p) for p in self.waiting]
        return f"Caixas: [{', '.join(caixas)}]\nEspera: [{', '.join(espera)}]"

    def arrive(self,name):
        self.waiting.append(Person(name))

    def call(self, index):
        if len(self.waiting) == 0:
            print("fail: sem clientes")
            return
       
        if index < 0 or index >= len(self.counters):
            print("fail: caixa inexistente")
            return
        
        if self.counters[index] is not None:
            print("fail: caixa ocupado")
            return
    
        self.counters[index] = self.waiting.pop(0)
    
    def finish(self, index):
        
        if index < 0 or index >= len(self.counters):
            print("fail: caixa inexistente")
            return
        
        if self.counters[index] is None:
            print("fail: caixa vazio")
            return
        
        self.counters [index] = None

def main():
        market = None

        while True:
            try:
                line = input().strip()
            except EOFError:
                break

            if not line:
                continue

            print(f"${line}")
            parts = line.split()
            cmd = parts[0]

            if cmd == "end":
                break

            if cmd == "init":
                qtd = int(parts[1])
                market = Market(qtd)
                continue

            if market is None:
                print("fail: mercantil nao iniciado")
                continue

            
            elif cmd == "show":
                print(market)

            elif cmd == "arrive":
                market.arrive(parts[1])

            elif cmd =="call":
                market.call(int(parts[1]))

            elif cmd == "finish":
                market.finish(int(parts[1]))
main()       
