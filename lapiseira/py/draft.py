class Grafite:
    def __init__(self, calibre, dureza, tamanho):
        self.calibre = calibre
        self.dureza = dureza
        self.tamanho = tamanho
        
    def desgaste_por_folha(self):
        tabela = {"HB":1, "2B": 2, "4B": 4, "6B": 6}
        return tabela.get(self.dureza, 0)
        
    def __str__(self):
        return f"{self.calibre}:{self.dureza}:{self.tamanho}"
    
class Lapiseira:
    def __init__(self, calibre):
        self.calibre = calibre
        self.bico = None
        self.tambor = []

    def insert(self, calibre, dureza, tamanho):
        if calibre != self.calibre:
            print("fail: calibre incompatível")
            return
        self.tambor.append(Grafite(calibre, dureza, tamanho))

    def pull(self):
        if self.bico is not None:
            print("fail: ja existe grafite no bico")
            return    
        if not self.tambor:
            print("fail: tambor vazio")
            return
                
        self.bico = self.tambor.pop(0)

    def remove(self):
        if self.bico is None:
            print("fail: nao existe grafite no bico")
            return
        self.bico = None
        
    def write(self):
        if self.bico is None:
            print ("fail: nao existe grafite no bico")
            return
            
        gasto = self.bico.desgaste_por_folha()

        if self.bico.tamanho <= 10:
            print("fail: tamanho insuficiente")
            return
        
        if self.bico.tamanho - gasto < 10:
            self.bico.tamanho = 10
            print("fail: folha incompleta")
            return

        self.bico.tamanho -= gasto
        

    def show (self):
        bico = f"[{self.bico}]" if self.bico else "[]"
        tambor = "<" + "".join(f"[{g}]" for g in self.tambor) + ">"
        print(f"calibre: {self.calibre}, bico: {bico}, tambor: {tambor}")
        
def main():
            lao = None

            while True:
                try:
                    line = input().strip()
                except EOFError:
                    break

                if not line:
                    continue
                
                cmd = line.split()

                if cmd[0] == "end":
                    print("$end")
                    break

                elif cmd[0] =="init":
                    print(f"$init {cmd[1]}")
                    lap = Lapiseira(float(cmd[1]))
                
                elif cmd[0] == "show":
                    print("$show")
                    lap.show()
                
                elif cmd[0] == "insert":
                    print(f"$insert {cmd[1]} {cmd[2]} {cmd[3]}")
                    lap.insert(float(cmd[1]), (cmd[2]), int(cmd[3]))
                
                elif cmd[0] == "pull":
                    print("$pull")
                    lap.pull()

                elif cmd[0] == "remove":
                    print("$remove")
                    lap.remove()

                elif cmd[0] == "write":
                    print("$write")
                    lap.write()
                else:
                    print("fail: comando invalido")
main()
