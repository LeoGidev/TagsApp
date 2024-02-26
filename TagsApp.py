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