import tkinter as tk
from tkinter import ttk


class Trivia:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Trivia')
        self.wind.geometry('400x400')

        # frame de registro
        self.frame_registro = ttk.Frame(self.wind)
        self.frame_registro.grid(column=0, row=0, padx=10, pady=10, sticky='w,s,n,e')

        self.label_registro = ttk.Label(self.frame_registro, text='Cual es tu nombre: ')
        self.label_registro.grid(sticky="w,s,e,n")





if __name__=='__main__':
    window = tk.Tk()
    my_app = Trivia(window)
    window.mainloop()
