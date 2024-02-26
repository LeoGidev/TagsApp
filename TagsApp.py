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
        self.root.geometry("940x500")
        self.root.configure(bg='#414141')
        
        #estilos de los frames
        style = ttk.Style()        
        self.root.set_theme('equilux')  
        style.configure('barratop.TFrame', background='#414141')
        style.configure('modulo.TFrame', background='white')
        
        
        #configuración de la prioridad para achicar columnas o rows en el resize de la ventana
        self.root.columnconfigure(0, weight=0)
        self.root.columnconfigure(1, weight=0)
        #self.root.rowconfigure(3, weight=1)
        #Configuración del icono
        self.root.iconbitmap(os.path.abspath("icon.ico"))

        #frame nav        
        self.nav_bar = ttk.Frame(self.root, height=50, style='barratop.TFrame')
        self.nav_bar.grid(row=0, column=0, sticky='ew', pady=0, padx=0, columnspan=4)
        #frame lateral1       
        self.lat1 = ttk.Frame(self.root, width=50, style='barratop.TFrame')
        self.lat1.grid(row=0, column=0, sticky='ns', pady=0, padx=0, rowspan=4)
        #frame lateral2       
        self.lat2 = ttk.Frame(self.root, width=50, style='barratop.TFrame')
        self.lat2.grid(row=0, column=3, sticky='ns', pady=0, padx=0, rowspan=4)
        #frame campo de selección de fondo
        self.fondo = ttk.Frame(self.root, width=300, style='barratop.TFrame')
        self.fondo = ttk.LabelFrame(self.root, text='Seleccione la imagene de fondo', padding=(10,10))
        self.fondo.grid(row=1, column=1, sticky='ew', padx=0, pady=3, columnspan=2)
        
        #Frame de datos1
        self.datos1 = ttk.Frame(self.root, width=300, style='barratop.TFrame')
        self.datos1 = ttk.LabelFrame(self.root, text='Datos a inculuir desde Excel', padding=(10,10))
        self.datos1.grid(row=2, column=1, sticky='ew', padx=0, pady=3, columnspan=2)
        #Frame de datosExtras1
        self.datoEx1 = ttk.Frame(self.root, width=300, style='barratop.TFrame')
        self.datoEx1 = ttk.LabelFrame(self.root, text='Datos Extras a incluir', padding=(10,10))
        self.datoEx1.grid(row=3, column=1, sticky='ew', padx=0, pady=3)
        #Frame de datosExtras2
        self.datoEx2 = ttk.Frame(self.root, width=300, style='barratop.TFrame')
        self.datoEx2 = ttk.LabelFrame(self.root, text='Datos Extras a incluir', padding=(10,10))
        self.datoEx2.grid(row=3, column=2, sticky='ew', padx=0, pady=3)
        #Frame de boton
        self.listo = ttk.Frame(self.root, width=300, style='barratop.TFrame')
        self.listo = ttk.LabelFrame(self.root, text='Crear Etiquetas', padding=(10,10))
        self.listo.grid(row=4, column=1, sticky='ew', padx=0, pady=3, columnspan=2)
        
        self.create_widgets()

    def create_widgets(self):
        self.create_labels_and_entries()
        self.create_buttons()
    
    def create_labels_and_entries(self):
        style = ttk.Style()        
        style.configure("Dark.TFrame", foreground="white", background="#414141", borderwidth=0) 
        #primer campo
        self.fonint1 = ttk.Frame(self.fondo, width=10, style='Dark.TFrame')
        self.fonint1.grid(row=0, column=0, sticky='ns', padx=0, pady=3, rowspan=2)
        self.arch = Label(self.fondo, text="Imagen no seleccionada:",background="#414141", foreground="white")
        self.arch.grid(row=1,column=1, sticky="ew", pady=10)
        #Label de datos excel
        self.lab1 = Label(self.datos1, text="Ingrese el nombre de cada celda:", background="#414141", foreground="white")
        self.lab1.grid(row=1, column=0, pady=10, padx=10)
        self.texto1 = Text(self.datos1, height=1, width=10)
        self.texto1.grid(row=1, column=1, sticky='e', pady=10, padx=10)
        self.texto2 = Text(self.datos1, height=1, width=10)
        self.texto2.grid(row=1, column=2, sticky='e', pady=10, padx=10)
        self.texto3 = Text(self.datos1, height=1, width=10)
        self.texto3.grid(row=1, column=3, sticky='e', pady=10, padx=10)
        self.texto1.bind('<KeyRelease>', self.check_entries)
        self.texto2.bind('<KeyRelease>', self.check_entries)
        self.texto3.bind('<KeyRelease>', self.check_entries)
        self.reslt1 = Label(self.datos1, text="No se ha seleccionado ningun archivo aún", background="#414141", foreground="white")
        self.reslt1.grid(row=2, column=0, pady=10, padx=10, columnspan=5)
        #Label de datos Extras
        self.lab2 = Label(self.datoEx1, text="Ingrese el dato a incluir:", background="#414141", foreground="white")
        self.lab2.grid(row=1, column=0, pady=10, padx=10)
        self.texto4 = Text(self.datoEx1, height=1, width=40)
        self.texto4.grid(row=2, column=0, sticky='we', pady=10, padx=10)
        #Label de datos Extras2
        self.lab3 = Label(self.datoEx2, text="Ingrese el dato a incluir:", background="#414141", foreground="white")
        self.lab3.grid(row=1, column=0, pady=10, padx=10)
        self.texto5 = Text(self.datoEx2, height=1, width=40)
        self.texto5.grid(row=2, column=0, sticky='we', pady=10, padx=10)
       
        

    def create_buttons(self):

        style = ttk.Style()        
        style.configure("Fancy.TButton", foreground="white", background="#0099ff", borderwidth=0) 
               
        style.configure("Dark.TFrame", foreground="white", background="#414141", borderwidth=0) 
        
        #boton de imagenes
        self.btn1 = ttk.Button(self.fondo, text="Abrir", command=self.buscador1, style='Fancy.TButton')
        self.btn1.grid(row=1, column=2, sticky='we', pady=10, padx=10)
        #boton de datoexcel
        self.btn2 = ttk.Button(self.datos1, text="Abrir", command=self.buscador2, state='disabled', style='Fancy.TButton')
        self.btn2.grid(row=1, column=4, sticky='w', pady=10, padx=10)
        
        #frame para el boton final
        self.fonint2 = ttk.Frame(self.listo, width=300)
        self.fonint2.grid(row=0, column=0, sticky='ew', padx=0, pady=3, rowspan=2)
        #boton de crear
        
        self.dale = ttk.Button(self.listo, text="Crear etiquetas", command=self.dibujar, width=30, style='Fancy.TButton')
        self.dale.grid(row=1, column=1, sticky='ew', pady=10, padx=10)
        
        self.fonint3 = ttk.Frame(self.listo, width=300)
        self.fonint3.grid(row=0, column=2, sticky='ew', padx=0, pady=3, rowspan=2)
        
        
    
    def check_entries(self, event):
            # Verificar si ambos campos de entrada tienen contenido y habilitar los botones en consecuencia
            if self.texto1.get("1.0", "end-1c") and self.texto2.get("1.0", "end-1c") and self.texto3.get("1.0", "end-1c"):
                self.btn2['state'] = 'normal'              
                
                print("habilitar")
            else:
                print("deshabilitados")
                self.btn2['state'] = 'disabled'
    
                
                
    
    def buscador1(self):
        try:
            self.archivo = filedialog.askopenfilename(initialdir="/",
                                                 title="Elija un archivo",
                                                 filetypes=(("imagen", "*.jpg*"),
                                                            ("all files", "*.*")))

           
            cuadromensaje = Label(self.arch, text="Archivo abierto: " + self.archivo, background="#414141", foreground="white")
            cuadromensaje.pack()
            
            
        except Exception as e:
            
            print('error')

    def buscador2(self):
        try:
            archivo2 = filedialog.askopenfilename(initialdir="/",
                                                  title="Elija un archivo",
                                                  filetypes=(("Hoja de Excel", "*.xls*"),
                                                             ("all files", "*.*")))
            result1 = self.texto1.get("1.0", "end")
            self.resultado1 = result1.strip('\n')

            result2 = self.texto2.get("1.0", "end")
            self.resultado2 = result2.strip('\n')

            result3 = self.texto3.get("1.0", "end")
            self.resultado3 = result3.strip('\n')

            cuadromensaje = Label(self.reslt1, text="Columnas a buscar: "+ self.resultado1 + "-" + self.resultado2 + '-' + self.resultado3, background="#414141", foreground="white")
            cuadromensaje.pack()
            
            hoja = pd.read_excel(archivo2)
            self.datA = hoja[self.resultado1]
            self.datB = hoja[self.resultado2]
            self.datC = hoja[self.resultado3]
        except Exception as e:
            cuadromensaje = Label(self.reslt1, text="Error: " + str(e),background="#414141", foreground="white")
            cuadromensaje.pack()
            print('error')

    def dibujar(self):
        img = cv2.imread(self.archivo)
        tamañoLetra = 3
        colorLetra = (255, 255, 255)
        grosorLetra = 3
        i = 0

        for a, b, c in zip(list(self.datA), list(self.datB), list(self.datC)):
            texto = self.resultado1 + ": " + str(a)
            ubicacion = (100, 200)
            cv2.putText(img, texto, ubicacion, cv2.FONT_HERSHEY_PLAIN, tamañoLetra, colorLetra, grosorLetra)

            texto2 = self.resultado2 + ": " + str(b)
            ubicacion2 = (100, 300)
            cv2.putText(img, texto2, ubicacion2, cv2.FONT_HERSHEY_PLAIN, tamañoLetra, colorLetra, grosorLetra)

            texto3 = self.resultado3 + ": " + str(c)
            ubicacion3 = (100, 400)
            cv2.putText(img, texto3, ubicacion3, cv2.FONT_HERSHEY_PLAIN, tamañoLetra, colorLetra, grosorLetra)

            self.rutaresult = 'C:\\Users\\work\\Desktop\\imagenes\\etiqueta' + str(i) + '.jpg'
            cv2.imwrite(self.rutaresult, img)
            i += 1
            print('dibujando', self.rutaresult)
        i = 0

    
    


if __name__ == "__main__":
    root = ThemedTk(theme="equilux")
    app = TagsApp(root)
    root.mainloop()
