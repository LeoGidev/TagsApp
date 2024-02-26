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
        self.root.geometry("900x600")
        self.root.configure(bg='#414141')
        
        #estilos de los frames
        style = ttk.Style()        
        self.root.set_theme('equilux')  
        style.configure('barratop.TFrame', background='#414141')
        style.configure('modulo.TFrame', background='#414141')
        
        
        #configuración de la prioridad para achicar columnas o rows en el resize de la ventana
        self.root.columnconfigure(0, weight=0)
        self.root.columnconfigure(1, weight=0)
        self.root.rowconfigure(3, weight=1)
        #Configuración del icono
        self.root.iconbitmap(os.path.abspath("icon.ico"))

        #frame nav        
        self.nav_bar = ttk.Frame(self.root, height=50, style='barratop.TFrame')
        self.nav_bar.grid(row=0, column=0, sticky='ew', pady=0, padx=0, columnspan=4)
        #frame lateral1       
        self.lat1 = ttk.Frame(self.root, width=50, style='barratop.TFrame')
        self.lat1.grid(row=0, column=0, sticky='ns', pady=0, padx=0, rowspan=3)
        #frame lateral2       
        self.lat2 = ttk.Frame(self.root, width=50, style='barratop.TFrame')
        self.lat2.grid(row=0, column=3, sticky='ns', pady=0, padx=0, rowspan=3)
        #frame campo de selección de fondo
        self.fondo = ttk.Frame(self.root, width=300, style='barratop.TFrame')
        self.fondo = ttk.LabelFrame(self.root, text='Seleccione la imagene de fondo', padding=(10,10))
        self.fondo.grid(row=1, column=1, sticky='ew', padx=0, pady=3, columnspan=2)
        #Frame de datos1
        self.datos1 = ttk.Frame(self.root, width=300, style='barratop.TFrame')
        self.datos1 = ttk.LabelFrame(self.root, text='Primer Dato a incluir de Excel', padding=(10,10))
        self.datos1.grid(row=2, column=1, sticky='ew', padx=0, pady=3)
        #Frame de datos2
        self.datos2 = ttk.Frame(self.root, width=300, style='barratop.TFrame')
        self.datos2 = ttk.LabelFrame(self.root, text='Primer Dato a incluir de Excel', padding=(10,10))
        self.datos2.grid(row=2, column=2, sticky='ew', padx=0, pady=3)
        
        self.create_widgets()

    def create_widgets(self):
        self.create_labels_and_entries()
        self.create_buttons()
    
    def create_labels_and_entries(self):
        self.arch = Label(self.fondo, text="Imagen no seleccionada:",background="#414141", foreground="white")
        self.arch.grid(row=1,column=0, pady=10)
        #Label de dato1
        self.lab1 = Label(self.datos1, text="Ingrese el nombre de dato", background="#414141", foreground="white")
        self.lab1.grid(row=1, column=0, pady=10, padx=10)
        self.texto1 = Text(self.datos1, height=1, width=10)
        self.texto1.grid(row=1, column=1, sticky='e', pady=10, padx=10)
        self.texto1.bind('<KeyRelease>', self.check_entries)
        self.reslt1 = Label(self.datos1, text="No se ha seleccionado ningun archivo aún", background="#414141", foreground="white")
        self.reslt1.grid(row=2, column=0, pady=10, padx=10, columnspan=3)
        ##Label de dato2
        self.lab2 = Label(self.datos2, text="Ingrese el nombre de dato", background="#414141", foreground="white")
        self.lab2.grid(row=1, column=0, pady=10, padx=10)
        self.texto2 = Text(self.datos2, height=1, width=10)
        self.texto2.grid(row=1, column=1, sticky='e', pady=10, padx=10)
        self.texto2.bind('<KeyRelease>', self.check_entries2)
        self.reslt2 = Label(self.datos2, text="No se ha seleccionado ningun archivo aún", background="#414141", foreground="white")
        self.reslt2.grid(row=2, column=0, pady=10, padx=10, columnspan=3)
        

    def create_buttons(self):
        self.btn1 = ttk.Button(self.fondo, text="Abrir", command=self.buscador1)
        self.btn1.grid(row=1, column=1, sticky='w', pady=10, padx=10)
        #boton de dato1
        self.btn2 = ttk.Button(self.datos1, text="Abrir", command=self.buscador2, state='disabled')
        self.btn2.grid(row=1, column=2, sticky='w', pady=10, padx=10)
        #button datos2
        #boton de dato1
        self.btn3 = ttk.Button(self.datos2, text="Abrir", command=self.buscador3, state='disabled')
        self.btn3.grid(row=1, column=2, sticky='w', pady=10, padx=10)
    
    def check_entries(self, event):
            # Verificar si ambos campos de entrada tienen contenido y habilitar los botones en consecuencia
            if self.texto1.get("1.0", "end-1c"):
                self.btn2['state'] = 'normal'              
                
                print("habilitar")
            else:
                print("deshabilitados")
                self.btn2['state'] = 'disabled'
    def check_entries2(self, event):
            # Verificar si ambos campos de entrada tienen contenido y habilitar los botones en consecuencia
            if self.texto2.get("1.0", "end-1c"):
                self.btn3['state'] = 'normal'              
                
                print("habilitar")
            else:
                print("deshabilitados")
                self.btn3['state'] = 'disabled'
                
                
    
    def buscador1(self):
        try:
            archivo = filedialog.askopenfilename(initialdir="/",
                                                 title="Elija un archivo",
                                                 filetypes=(("imagen", "*.jpg*"),
                                                            ("all files", "*.*")))

           
            cuadromensaje = Label(self.arch, text="Archivo abierto: " + archivo, background="#414141", foreground="white")
            cuadromensaje.pack()
            
            
        except Exception as e:
            
            print('error')

    def buscador2(self):
        try:
            archivo2 = filedialog.askopenfilename(initialdir="/",
                                                  title="Elija un archivo",
                                                  filetypes=(("Hoja de Excel", "*.xls*"),
                                                             ("all files", "*.*")))
            result2 = self.texto1.get("1.0", "end")
            resultado2 = result2.strip('\n')
            cuadromensaje = Label(self.reslt1, text="dato: " +resultado2 +'del archivo:' + archivo2, background="#414141", foreground="white")
            cuadromensaje.pack()
            
            #hoja2 = pd.read_excel(archivo2)
            #self.dato2 = hoja2[resultado2]
        except Exception as e:
            #cuadromensaje = Label(self.ResultadoGeneral, text="Error: " + str(e),background="#414141", foreground="white")
            #cuadromensaje.pack()
            print('error')
    
    def buscador3(self):
        try:
            archivo3 = filedialog.askopenfilename(initialdir="/",
                                                  title="Elija un archivo",
                                                  filetypes=(("Hoja de Excel", "*.xls*"),
                                                             ("all files", "*.*")))
            result3 = self.texto2.get("1.0", "end")
            resultado3 = result3.strip('\n')
            cuadromensaje = Label(self.reslt2, text="dato: " +resultado3 +'del archivo:' + archivo3, background="#414141", foreground="white")
            cuadromensaje.pack()
            
            #hoja2 = pd.read_excel(archivo2)
            #self.dato2 = hoja2[resultado2]
        except Exception as e:
            #cuadromensaje = Label(self.ResultadoGeneral, text="Error: " + str(e),background="#414141", foreground="white")
            #cuadromensaje.pack()
            print('error')


if __name__ == "__main__":
    root = ThemedTk(theme="equilux")
    app = TagsApp(root)
    root.mainloop()
