class Client:
    def __init__(self, id, fone):
        self.id = id
        self.fone = fone

    def __str__(self):
        return f"{self.id}:{self.fone}"
    
class Theater:
    def __init__(self):
        self.seats = []
    
    def init(self, n):
        self.seats = [None] * n
    
    def show(self):
        out = []
        for seat in self.seats:
            if seat is None:
                out.append("-")
            else:
                out.append(str(seat))
        return "[" + " ".join(out) + "]"

       
    def reserve(self, id, phone, index):
        if index < 0 or index >= len(self.seats):
            print("fail: cadeira nao existe")
            return
        
        for seat in self.seats:
             if seat is not None and seat.id == id:
                print("fail: cliente ja esta no cinema")
                return
               
            
        if self.seats[index] is not None:
            print("fail: cadeira ja esta ocupada")
            return
        
        self.seats[index] = Client(id, phone)
    
    def cancel(self, id):
        for i in range(len(self.seats)):
            if self.seats[i] is not None and self.seats[i].id == id:
                self.seats[i] = None
                return

def main():
    theater = Theater()
    
    while True:
        try:
            line = input().strip()
        except EOFError:
            break

        if line == "end":
            print("$end")
            break

        parts = line.split()
        cmd = parts[0]

        if cmd == "show":
            print("$show")
            print(theater.show())
            continue

        if cmd == "init":
            print(f"$init {parts[1]}")
            n = int(parts[1])
            theater.init(n)
            continue

        if cmd == "reserve":
            print(f"$reserve {parts[1]} {parts[2]} {parts[3]}")
            id = parts[1]
            phone = parts[2]
            index = int(parts[3])
            theater.reserve(id, phone, index)
            continue

        if cmd == "cancel":
            print(f"$cancel {parts[1]}")
            theater.cancel(parts[1])
            continue

        print(f"${line}")
main()
