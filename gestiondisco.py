from tkinter import ttk
from heapq import *

class Producto:
    
    def __init__(self, window):
        self.wind = window
        self.wind.title('GESTION DE DISCO')
        self.wind.geometry("800x500")
        
        #contenedor
       frame = Frame(self.wind, text = 'PLANIFICADOR DE DISCO')
        frame.grid(row = 0, column = 0, columpnspan = 3, pady = 20)
        
        Label(frame, text = 'INGRESE NUMERO DE PETICIONES').grid(row = 1, column =  0)
        self.name = Entry(frame)
        self.name.grid(row =1, column = 1)
        
        Label(frame, text = '     n,n' ),grid(row = 2, column = 0)
        self.disco = Entry(frame)
        self.disco.grid(row = 2, column = 1)
        
    if __name__ == '__main__':
        window = Tk()
        application = Producto(window)
        window.mainloop()
        