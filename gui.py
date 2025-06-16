import tkinter as tk
from tkinter import messagebox
from tic_tac_toe import TicTacToe

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tres en Raya Extendido")
        self.root.resizable(False, False)  # bloquear redimensionado

        self.vs_maquina = True
        self.botones = []
        self.juego = None
        self.bloqueado = False

        self.label_turno = None  # para mostrar el turno

        self.pantalla_inicio()

    def centrar_ventana(self, ancho, alto):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.root.winfo_screenheight() // 2) - (alto // 2)
        self.root.geometry(f"{ancho}x{alto}+{x}+{y}")

    def pantalla_inicio(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.geometry("400x300")
        self.centrar_ventana(400, 300)

        tk.Label(self.root, text="Seleccione el tamaño del tablero (N x N):", font=("Arial", 14)).pack(pady=10)

        self.entrada_tamano = tk.Spinbox(self.root, from_=3, to=7, font=("Arial", 14), width=5)
        self.entrada_tamano.pack(pady=5)

        boton_jugar = tk.Button(self.root, text="Iniciar Juego", font=("Arial", 14), command=self.iniciar_juego)
        boton_jugar.pack(pady=20)

    def iniciar_juego(self):
        try:
            self.tamano_tablero = int(self.entrada_tamano.get())
            if not 3 <= self.tamano_tablero <= 7:
                raise ValueError
            self.juego = TicTacToe(self.tamano_tablero)

            # 🔧 ajustar tamaño de ventana
            tam_celda = 90
            ancho = self.tamano_tablero * tam_celda
            alto = self.tamano_tablero * tam_celda + 120
            self.root.geometry(f"{ancho}x{alto}")
            self.centrar_ventana(ancho, alto)

        except:
            messagebox.showerror("Error", "El tamaño debe estar entre 3 y 7.")
            return

        self.crear_tablero()

    def crear_tablero(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.botones = []

        # 🔲 Etiqueta de turno
        self.label_turno = tk.Label(self.root, text=f"Turno: {self.juego.turno}", font=("Arial", 14))
        self.label_turno.pack(pady=5)

        frame_tablero = tk.Frame(self.root)
        frame_tablero.pack(pady=10)

        for fila in range(self.tamano_tablero):
            fila_botones = []
            for col in range(self.tamano_tablero):
                boton = tk.Button(frame_tablero, text="", font=("Arial", 20), width=3, height=1,
                                  command=lambda f=fila, c=col: self.clic(f, c))
                boton.grid(row=fila, column=col, padx=2, pady=2)
                fila_botones.append(boton)
            self.botones.append(fila_botones)

        boton_volver = tk.Button(self.root, text="Volver al Inicio", font=("Arial", 12),
                                 command=self.pantalla_inicio)
        boton_volver.pack(pady=10)

    def clic(self, fila, columna):
        if self.bloqueado:
            return

        if self.juego.jugar(fila, columna):
            self.botones[fila][columna].config(text=self.juego.tablero[fila][columna])
            self.label_turno.config(text=f"Turno: {self.juego.turno}")  # actualizar turno
            if self.verificar_estado():
                return

            if self.vs_maquina and self.juego.turno == "O":
                self.bloqueado = True
                self.root.after(300, self.turno_maquina)

    def turno_maquina(self):
        fila, col = self.juego.obtener_jugada_maquina()
        if fila is not None:
            self.juego.jugar(fila, col)
            self.botones[fila][col].config(text="O")
            self.label_turno.config(text=f"Turno: {self.juego.turno}")
            self.verificar_estado()
        self.bloqueado = False

    def verificar_estado(self):
        if self.juego.ganador:
            messagebox.showinfo("¡Fin del juego!", f"¡Ganó {self.juego.ganador}!")
            self.reiniciar()
            return True
        elif self.juego.es_empate():
            messagebox.showinfo("Empate", "¡Es un empate!")
            self.reiniciar()
            return True
        return False

    def reiniciar(self):
        self.juego.reiniciar()
        self.crear_tablero()

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
