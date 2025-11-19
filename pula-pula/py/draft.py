class Kid:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}:{self.age}"
    
class Trampoline:
    def __init__(self):
        self.waiting = []
        self.playing = []
    
    def arrive(self, name, age):
        self.waiting.insert(0, Kid(name,age))
    
    def enter(self):
        if len(self.waiting) > 0:
            kid = self.waiting.pop()
            self.playing.insert(0, kid)
    
    def leave(self):
        if len(self.playing) >0:
            kid = self.playing.pop()
            self.waiting.insert(0, kid)

    def remove(self, name): 
        for i, kid in enumerate(self.waiting):
            if kid.name == name:
                self.waiting.pop(i)
                return
        for i, kid in enumerate (self.playing):
            if kid.name == name:
                self.waiting.pop(i)
                return
            
        for i, kid in enumerate(self.playing):
            if kid.name == name:
                self.playing.pop(i)
               
            
        print(f"fail: {name} nao esta no pula-pula")
    def show(self):
        w = ", ".join(str(k) for k in self.waiting)
        p = ", ".join(str(k) for k in self.playing)
        print(f"[{w}] => [{p}]")
    
def main():
    toy = Trampoline()
    while True:
        try:
        
            line = input().strip()
        except EOFError:
            break
       
        if line == "":
            continue
        
        print(f"${line}")
        parts = line.split()
        cmd = parts[0]

        if cmd == "end":
            break

        elif cmd == "show":
            toy.show()

        
        elif cmd == "arrive":
            name = parts[1]
            age = int(parts[2])
            toy.arrive(name, age)
        
        elif cmd == "enter":
            toy.enter()

        elif cmd == "leave":
            toy.leave()
         
        elif cmd == "remove":
            name = parts[1]
            toy.remove(name)
main()






