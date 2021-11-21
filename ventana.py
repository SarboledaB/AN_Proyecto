import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox, ttk

from numpy.lib import stride_tricks
from biseccion import biseccion
from punto_fijo import puntofijo
from regla_falsa import regla_falsa
from secante import secante
from busquedas import entrada as busquedas
from raices_multiples import raicesmlt
from newton import newton

def inicio():
    #intrucciones
    boton1 = Button(ventana_principal, text="Solucion numérica de ecuaciones no lineales", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: createNewWindow1())    
    boton2 = Button(ventana_principal, text="Solucion de sistemas de ecuaciones lineales", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: createNewWindow2())
    boton3 = Button(ventana_principal, text="Interpolación", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: createNewWindow3())

    boton1.grid(column=0, row=1, columnspan=2)
    boton2.grid(column=0,row=3, columnspan=2)
    boton3.grid(column=0,row=5, columnspan=2)

def createNewWindow1():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=14)
    boton4 = Button(newWindow, text="Busquedas", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: busquedass())
    boton5 = Button(newWindow, text="Biseccion", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: biseccionn())
    boton6 = Button(newWindow, text="Regla falsa", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: reglaFalsa())
    boton7 = Button(newWindow, text="Punto fijo", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: puntoFijo())
    boton8 = Button(newWindow, text="Newton", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: newwton())
    boton9 = Button(newWindow, text="Secante", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: secantee())
    boton10 = Button(newWindow, text="Raices multiples", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: raicesMultiples())

    boton4.grid(column=0, row=1, columnspan=2)
    label5.grid(column=0,row=2, columnspan=2)
    boton5.grid(column=0,row=3, columnspan=2)
    label5.grid(column=0,row=4, columnspan=2)
    boton6.grid(column=0,row=5, columnspan=2)
    label5.grid(column=0,row=6, columnspan=2)
    boton7.grid(column=0, row=7, columnspan=2)
    label5.grid(column=0,row=8, columnspan=2)
    boton8.grid(column=0,row=9, columnspan=2)
    label5.grid(column=0,row=10, columnspan=2)
    boton9.grid(column=0,row=11, columnspan=2)
    label5.grid(column=0,row=12, columnspan=2)
    boton10.grid(column=0, row=13, columnspan=2)
    label5.grid(column=0,row=14, columnspan=2)

def createNewWindow2():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=14)
    boton11 = Button(newWindow, text="Gaus Simple", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: gausSimple())
    boton12 = Button(newWindow, text="Gaus Pivote Parcial", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: gausPP())
    boton13 = Button(newWindow, text="Gaus Pivote Total", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: gausPT())
    boton14 = Button(newWindow, text="Factorizacion Lu Simple", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: factorizacionLuSimple())
    boton15 = Button(newWindow, text="Factorizacion Lu Parcial", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: factorizacionLuParcial())
    boton16 = Button(newWindow, text="Jacobi", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: jacobi())
    boton17 = Button(newWindow, text="Gaus Eidel", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: gausEidel())

    boton11.grid(column=0, row=1, columnspan=2)
    label5.grid(column=0,row=2, columnspan=2)
    boton12.grid(column=0,row=3, columnspan=2)
    label5.grid(column=0,row=4, columnspan=2)
    boton13.grid(column=0,row=5, columnspan=2)
    label5.grid(column=0,row=6, columnspan=2)
    boton14.grid(column=0, row=7, columnspan=2)
    label5.grid(column=0,row=8, columnspan=2)
    boton15.grid(column=0,row=9, columnspan=2)
    label5.grid(column=0,row=10, columnspan=2)
    boton16.grid(column=0,row=11, columnspan=2)
    label5.grid(column=0,row=12, columnspan=2)
    boton17.grid(column=0, row=13, columnspan=2)
    label5.grid(column=0,row=14, columnspan=2)

def createNewWindow3():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=5)
    boton18 = Button(newWindow,text="Vandermonde", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: vandermonde())
    boton19 = Button(newWindow,text="Diferencias Divididas", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: diferenciasDiv())
    boton20 = Button(newWindow,text="Lagrange", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: lagrange())

    boton18.grid(column=0, row=1, columnspan=2)
    boton19.grid(column=0,row=3, columnspan=2)
    boton20.grid(column=0,row=5, columnspan=2)

def busquedass():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=350)
    canvas.grid(columnspan=2, rowspan=7)
    Label(newWindow, text="Funcion").grid(column=0,row=1)
    funcion =Entry(newWindow)
    funcion.grid(column=1,row=1)
    
    Label(newWindow, text="Punto Inicial").grid(column=0,row=2)
    puntoInicial = Entry(newWindow)
    puntoInicial.grid(column=1,row=2)
    
    Label(newWindow, text="Maximo de Interaccioneses").grid(column=0,row=3)
    maxInteraccion = Entry(newWindow)
    maxInteraccion.grid(column=1,row=3)
    
    Label(newWindow, text="paso").grid(column=0,row=4)
    paso = Entry(newWindow)
    paso.grid(column=1,row=4)
    
    boton = Button(newWindow, text="Iniciar", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: busquedas(funcion.get(),float(puntoInicial.get()),float(paso.get()),int(maxInteraccion.get())))
    boton.grid(column=0, row=6, columnspan=2)
    #Label(newWindow, text='{}'.format(resultado)).grid(column=0,row=7, columnspan=2)
    

def biseccionn():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=5)
    
def reglaFalsa():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=5)
    
def puntoFijo():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=5)
    
def newwton():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=5)
    
def secantee():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=5)
    
def raicesMultiples():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=5)
    
def gausSimple():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=5)
    
def gausPP():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=5)
    
def gausPT():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=5)
    
def factorizacionLuSimple():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=5)
    
def factorizacionLuParcial():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=5)
    
def jacobi():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=5)
    
def gausEidel():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=5)
    
def vandermonde():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=5)
    
def diferenciasDiv():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=5)
    
def lagrange():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=5)
    
str = ''
pestas_color="DarkGrey"
ventana_principal = tk.Tk()
canvas = tk.Canvas(ventana_principal, width=400, height=450)
canvas.grid(columnspan=2, rowspan=14)
ventana_principal.title("Analisis numerico")#TITULO DE LA VENTANA
label1= Label(ventana_principal, text="Bienvenido a Analisis Numerico", bg="SkyBlue", font=("Calibri", 13))
label1.grid(column=0,row=0, columnspan=5)
botonback = Button(ventana_principal, text="back", bg="SkyBlue", fg="black", width=10, height=1, command= lambda: inicio())
boton = Button(ventana_principal, text="Iniciar", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: inicio())
boton.grid(column=0, row=1, columnspan=2)

label5 = Label(ventana_principal, text="")

ventana_principal.mainloop()