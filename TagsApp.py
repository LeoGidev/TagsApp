import pandas as pd
import openpyxl
import time
import cv2
from tkinter import Tk, Label, Text, Button, filedialog, Frame, ttk, Scale, Canvas
import os
from ttkthemes import ThemedTk
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import imageio



class TagsApp:
    def __init__(self, root):
        #configuración de ventana
        self.root = root
        self.root.title('Tags App')
        self.root.geometry("860x600")
        self.root.configure(bg='#414141')
        
        #estilos de los frames
        style = ttk.Style()        
        self.root.set_theme('equilux')  
        style.configure('barratop.TFrame', background='#414141')
        style.configure('modulo.TFrame', background='#414141')
        #frame nav        
        self.nav_bar = ttk.Frame(self.root, height=50, style='barratop.TFrame')
        self.nav_bar.grid(row=0, column=0, sticky='ew', pady=0, padx=0, columnspan=3)
        #frame campo de selección de fondo
        self.fondo = ttk.Frame(self.root, width=300, style='barratop.TFrame')
        self.fondo = ttk.LabelFrame(self.root, text='Seleccione la imagene de fondo', padding=(10,10))
        self.fondo.grid(row=1, column=0, sticky='we', padx=0, pady=0, columnspan=3)
        
        #configuración de la prioridad para achicar columnas o rows en el resize de la ventana
        self.root.columnconfigure(0, weight=0)
        self.root.columnconfigure(1, weight=0)
        self.root.rowconfigure(3, weight=1)
        #Configuración del icono
        self.root.iconbitmap(os.path.abspath("icon.ico"))
        
        self.create_widgets()

    def create_widgets(self):
        self.create_labels_and_entries()
        self.create_buttons()
    
    def create_labels_and_entries(self):
        Label(self.fondo, text="Ingrese La máscara en formato Slash sin la barra:",background="#414141", foreground="white").grid(row=1,column=2, pady=10)
        

    def create_buttons(self):
        self.btn1 = ttk.Button(self.fondo, text="Abrir", command=self.buscador1, state='disabled')
        self.btn1.grid(row=0, column=2, sticky='w', pady=10, padx=10)


if __name__ == "__main__":
    root = ThemedTk(theme="equilux")
    app = TagsApp(root)
    root.mainloop()
