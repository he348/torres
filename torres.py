import tkinter as tk
 
class TorreHanoi:
    def __init__(self, master):
        self.master = master
        self.master.title("Torre de Hanói")
        self.canvas = tk.Canvas(master, width=600, height=400, bg="white")
        self.canvas.pack()
 
        # Número de discos e torres de origem e destino são solicitados ao usuário
        self.num_discos = int(input("Informe o número de discos: "))
        self.origem = input("Informe a torre de origem (A, B ou C): ").upper()
        self.destino = input("Informe a torre de destino (A, B ou C): ").upper()
 
        # Definição da torre auxiliar
        torres = ['A', 'B', 'C']
        torres.remove(self.origem)
        torres.remove(self.destino)
        self.auxiliar = torres[0]
 
        self.torres = {'A': [], 'B': [], 'C': []}
        self.discos = []
        self.labels = []
        self.movimentos = 0
 
        # Inicializa os discos na torre de origem
        tower_positions = {'A': 150, 'B': 300, 'C': 450}
        for i in range(1, self.num_discos + 1):
            self.torres[self.origem].append(i)
            x = tower_positions[self.origem]
            y = 200 - (i - 1) * 20
            width = (self.num_discos - i + 1) * 15  # Tamanho decrescente dos discos
            self.discos.append(self.canvas.create_rectangle(x - width, y, x + width, y + 20, fill="blue"))
            self.labels.append(self.canvas.create_text(x, y + 10, text=str(i), fill="white", font=("Arial", 10)))
 
        # Rótulos das torres
        self.canvas.create_text(150, 350, text="Torre A", font=("Arial", 12))
        self.canvas.create_text(300, 350, text="Torre B", font=("Arial", 12))
        self.canvas.create_text(450, 350, text="Torre C", font=("Arial", 12))
 
        # Resolução do problema
        self.resolve_hanoi(self.num_discos, self.origem, self.destino, self.auxiliar)
        print(f"Número total de movimentos: {self.movimentos}")
 
    def move_disco(self, origem, destino):
        disco_id = self.torres[origem].pop()
        self.torres[destino].append(disco_id)
        self.movimentos += 1
        print(f"Mova o disco {disco_id} da torre {origem} para a torre {destino}")
        self.update_canvas(disco_id, destino)
        self.master.update()
        self.master.after(500)  # Visualização dos movimentos
 
    def update_canvas(self, disco_id, destino):
        tower_positions = {'A': 150, 'B': 300, 'C': 450}
        x = tower_positions[destino]
        y = 200 - (len(self.torres[destino]) - 1) * 20
        width = (self.num_discos - disco_id + 1) * 15
        self.canvas.coords(self.discos[disco_id - 1], x - width, y, x + width, y + 20)
        self.canvas.coords(self.labels[disco_id - 1], x, y + 10)
 
    def resolve_hanoi(self, n, origem, destino, aux):
        if n == 1:
            self.move_disco(origem, destino)
        else:
            self.resolve_hanoi(n - 1, origem, aux, destino)
            self.move_disco(origem, destino)
            self.resolve_hanoi(n - 1, aux, destino, origem)
 
def main():
    root = tk.Tk()
    TorreHanoi(root)
    root.mainloop()
 
if __name__ == "__main__":
    main()
