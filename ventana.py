import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox, ttk
from AN_Proyecto.raices_multiples import raicesmlt

from numpy.lib import stride_tricks
from biseccion import entrada as biseccion
from punto_fijo import entrada as puntofijo
from regla_falsa import entrada as regla_falsa
from secante import entrada as secante
from busquedas import entrada as busquedas
from raices_multiples import entrada as raicesmlps
from newton import entrada as newton
from gausspl import gausspl
from gausspar import gausspar
from gausstot import gausspar as gausstot
from lusimpl import lusimpl
from lupar import lupar
from jacobi import entrada as jacobi
from gseidel import gauss_seidel

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
    boton11 = Button(newWindow, text="Gauss Simple", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: gausSimple())
    boton12 = Button(newWindow, text="Gauss Pivote Parcial", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: gausPP())
    boton13 = Button(newWindow, text="Gauss Pivote Total", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: gausPT())
    boton14 = Button(newWindow, text="Factorizacion Lu Simple", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: factorizacionLuSimple())
    boton15 = Button(newWindow, text="Factorizacion Lu Parcial", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: factorizacionLuParcial())
    boton16 = Button(newWindow, text="Jacobi", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: jacobi())
    boton17 = Button(newWindow, text="Gauss-Seidel", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: gausEidel())

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
    
    Label(newWindow, text="Maximo de Iteraciones").grid(column=0,row=3)
    maxIteracion = Entry(newWindow)
    maxIteracion.grid(column=1,row=3)
    
    Label(newWindow, text="paso").grid(column=0,row=4)
    paso = Entry(newWindow)
    paso.grid(column=1,row=4)
    
    resultado = ""
    
    boton = Button(newWindow, text="Iniciar", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: resultado == busquedas(funcion.get(),float(puntoInicial.get()),float(paso.get()),int(maxIteracion.get())))
    boton.grid(column=0, row=6, columnspan=2)
    Label(newWindow, text='{}'.format(resultado)).grid(column=0,row=7, columnspan=2)
    
def biseccionn():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=7)
    
    Label(newWindow, text="Funcion").grid(column=0,row=1)
    funcion =Entry(newWindow)
    funcion.grid(column=1,row=1)
    
    Label(newWindow, text="Punto a").grid(column=0,row=2)
    puntoInicial = Entry(newWindow)
    puntoInicial.grid(column=1,row=2)
    
    Label(newWindow, text="Punto b").grid(column=0,row=3)
    puntoFinal = Entry(newWindow)
    puntoFinal.grid(column=1,row=3)
    
    Label(newWindow, text="Maximo de Iteraciones").grid(column=0,row=4)
    maxIteracion = Entry(newWindow)
    maxIteracion.grid(column=1,row=4)
    
    Label(newWindow, text="Tolerancia").grid(column=0,row=5)
    tolerancia = Entry(newWindow)
    tolerancia.grid(column=1,row=5)
    
    resultado = ""
    
    boton = Button(newWindow, text="Iniciar", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: resultado == biseccion(funcion.get(),float(puntoInicial.get()),float(puntoFinal.get()),int(maxIteracion.get()),float(tolerancia.get())))
    boton.grid(column=0, row=6, columnspan=2)
    Label(newWindow, text='{}'.format(resultado)).grid(column=0,row=7, columnspan=2)
    
def reglaFalsa():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=7)
    
    Label(newWindow, text="Funcion").grid(column=0,row=1)
    funcion =Entry(newWindow)
    funcion.grid(column=1,row=1)
    
    Label(newWindow, text="Punto a").grid(column=0,row=2)
    puntoInicial = Entry(newWindow)
    puntoInicial.grid(column=1,row=2)
    
    Label(newWindow, text="Punto b").grid(column=0,row=3)
    puntoFinal = Entry(newWindow)
    puntoFinal.grid(column=1,row=3)
    
    Label(newWindow, text="Maximo de Iteraciones").grid(column=0,row=4)
    maxIteracion = Entry(newWindow)
    maxIteracion.grid(column=1,row=4)
    
    Label(newWindow, text="Tolerancia").grid(column=0,row=5)
    tolerancia = Entry(newWindow)
    tolerancia.grid(column=1,row=5)
    
    resultado = ""
    
    boton = Button(newWindow, text="Iniciar", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: resultado == regla_falsa(funcion.get(),float(puntoInicial.get()),float(puntoFinal.get()),int(maxIteracion.get()),float(tolerancia.get())))
    boton.grid(column=0, row=6, columnspan=2)
    Label(newWindow, text='{}'.format(resultado)).grid(column=0,row=7, columnspan=2)
    
def puntoFijo():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=7)
    
    Label(newWindow, text="Funcion").grid(column=0,row=1)
    funcion =Entry(newWindow)
    funcion.grid(column=1,row=1)
    
    Label(newWindow, text="Punto Inicial").grid(column=0,row=2)
    puntoInicial = Entry(newWindow)
    puntoInicial.grid(column=1,row=2)
    
    Label(newWindow, text="Maximo de Iteraciones").grid(column=0,row=3)
    maxIteracion = Entry(newWindow)
    maxIteracion.grid(column=1,row=3)
    
    Label(newWindow, text="Tolerancia").grid(column=0,row=4)
    tolerancia = Entry(newWindow)
    tolerancia.grid(column=1,row=4)
    
    resultado = ""
    
    boton = Button(newWindow, text="Iniciar", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: resultado == puntofijo(funcion.get(),float(puntoInicial.get()),int(maxIteracion.get()),float(tolerancia.get())))
    boton.grid(column=0, row=6, columnspan=2)
    Label(newWindow, text='{}'.format(resultado)).grid(column=0,row=7, columnspan=2)
    
def newwton():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=7)
    
    Label(newWindow, text="Funcion").grid(column=0,row=1)
    funcion =Entry(newWindow)
    funcion.grid(column=1,row=1)
    
    Label(newWindow, text="Punto Inicial").grid(column=0,row=2)
    puntoInicial = Entry(newWindow)
    puntoInicial.grid(column=1,row=2)
    
    Label(newWindow, text="Maximo de Iteraciones").grid(column=0,row=3)
    maxIteracion = Entry(newWindow)
    maxIteracion.grid(column=1,row=3)
    
    Label(newWindow, text="tolerancia").grid(column=0,row=4)
    tolerancia = Entry(newWindow)
    tolerancia.grid(column=1,row=4)
    
    resultado = ""
    
    boton = Button(newWindow, text="Iniciar", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: resultado == newton(funcion.get(),float(puntoInicial.get()),int(maxIteracion.get()),float(tolerancia.get())))
    boton.grid(column=0, row=6, columnspan=2)
    Label(newWindow, text='{}'.format(resultado)).grid(column=0,row=7, columnspan=2)
    
def secantee():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=7)
    
    Label(newWindow, text="Funcion").grid(column=0,row=1)
    funcion =Entry(newWindow)
    funcion.grid(column=1,row=1)
    
    Label(newWindow, text="Punto a").grid(column=0,row=2)
    puntoa = Entry(newWindow)
    puntoa.grid(column=1,row=2)
    
    Label(newWindow, text="Punto b").grid(column=0,row=3)
    puntob = Entry(newWindow)
    puntob.grid(column=1,row=3)
    
    Label(newWindow, text="Maximo de Iteraciones").grid(column=0,row=4)
    maxIteracion = Entry(newWindow)
    maxIteracion.grid(column=1,row=4)
    
    Label(newWindow, text="tolerancia").grid(column=0,row=5)
    tolerancia = Entry(newWindow)
    tolerancia.grid(column=1,row=5)
    
    resultado = ""
    
    boton = Button(newWindow, text="Iniciar", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: resultado == secante(funcion.get(),float(puntoa.get()),float(puntob.get()),int(maxIteracion.get()),tolerancia.get))
    boton.grid(column=0, row=6, columnspan=2)
    Label(newWindow, text='{}'.format(resultado)).grid(column=0,row=7, columnspan=2)
    
def raicesMultiples():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=7)
    
    Label(newWindow, text="Funcion").grid(column=0,row=1)
    funcion =Entry(newWindow)
    funcion.grid(column=1,row=1)
    
    Label(newWindow, text="Punto a").grid(column=0,row=2)
    puntoa = Entry(newWindow)
    puntoa.grid(column=1,row=2)
    
    Label(newWindow, text="Maximo de Iteraciones").grid(column=0,row=3)
    maxIteracion = Entry(newWindow)
    maxIteracion.grid(column=1,row=3)
    
    Label(newWindow, text="tolerancia").grid(column=0,row=4)
    tolerancia = Entry(newWindow)
    tolerancia.grid(column=1,row=4)
    
    resultado = ""
    
    boton = Button(newWindow, text="Iniciar", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: resultado == raicesmlps(funcion.get(),float(puntoa.get()),int(maxIteracion.get()),tolerancia.get))
    boton.grid(column=0, row=6, columnspan=2)
    Label(newWindow, text='{}'.format(resultado)).grid(column=0,row=7, columnspan=2)
    
def gausSimple():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=5)
    
    Label(newWindow, text="Funcion").grid(column=0,row=1)
    funcion =Entry(newWindow)
    funcion.grid(column=1,row=1)
    
    Label(newWindow, text="Punto Inicial").grid(column=0,row=2)
    puntoInicial = Entry(newWindow)
    puntoInicial.grid(column=1,row=2)
    
    resultado = ""
    
    boton = Button(newWindow, text="Iniciar", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: resultado == gausspl(funcion.get(),float(puntoInicial.get())))
    boton.grid(column=0, row=6, columnspan=2)
    Label(newWindow, text='{}'.format(resultado)).grid(column=0,row=7, columnspan=2)
    
def gausPP():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=5)
    
    Label(newWindow, text="Funcion").grid(column=0,row=1)
    funcion =Entry(newWindow)
    funcion.grid(column=1,row=1)
    
    Label(newWindow, text="Punto Inicial").grid(column=0,row=2)
    puntoInicial = Entry(newWindow)
    puntoInicial.grid(column=1,row=2)
    
    resultado = ""
    
    boton = Button(newWindow, text="Iniciar", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: resultado == gausspar(funcion.get(),float(puntoInicial.get())))
    boton.grid(column=0, row=6, columnspan=2)
    Label(newWindow, text='{}'.format(resultado)).grid(column=0,row=7, columnspan=2)
    
def gausPT():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=5)
    
    Label(newWindow, text="Funcion").grid(column=0,row=1)
    funcion =Entry(newWindow)
    funcion.grid(column=1,row=1)
    
    Label(newWindow, text="Punto Inicial").grid(column=0,row=2)
    puntoInicial = Entry(newWindow)
    puntoInicial.grid(column=1,row=2)
    
    resultado = ""
    
    boton = Button(newWindow, text="Iniciar", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: resultado == gausstot(funcion.get(),float(puntoInicial.get())))
    boton.grid(column=0, row=6, columnspan=2)
    Label(newWindow, text='{}'.format(resultado)).grid(column=0,row=7, columnspan=2)
    
def factorizacionLuSimple():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=5)
    
    Label(newWindow, text="Funcion").grid(column=0,row=1)
    funcion =Entry(newWindow)
    funcion.grid(column=1,row=1)
    
    Label(newWindow, text="Punto Inicial").grid(column=0,row=2)
    puntoInicial = Entry(newWindow)
    puntoInicial.grid(column=1,row=2)
    
    resultado = ""
    
    boton = Button(newWindow, text="Iniciar", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: resultado == lusimpl(funcion.get(),float(puntoInicial.get())))
    boton.grid(column=0, row=6, columnspan=2)
    Label(newWindow, text='{}'.format(resultado)).grid(column=0,row=7, columnspan=2)
    
def factorizacionLuParcial():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=5)
    
    Label(newWindow, text="Funcion").grid(column=0,row=1)
    funcion =Entry(newWindow)
    funcion.grid(column=1,row=1)
    
    Label(newWindow, text="Punto Inicial").grid(column=0,row=2)
    puntoInicial = Entry(newWindow)
    puntoInicial.grid(column=1,row=2)
    
    resultado = ""
    
    boton = Button(newWindow, text="Iniciar", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: resultado == lupar(funcion.get(),float(puntoInicial.get())))
    boton.grid(column=0, row=6, columnspan=2)
    Label(newWindow, text='{}'.format(resultado)).grid(column=0,row=7, columnspan=2)
    
def jacobi():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=7)
    
    Label(newWindow, text="Funcion").grid(column=0,row=1)
    funcion =Entry(newWindow)
    funcion.grid(column=1,row=1)
    
    Label(newWindow, text="Punto Inicial").grid(column=0,row=2)
    puntoInicial = Entry(newWindow)
    puntoInicial.grid(column=1,row=2)
    
    Label(newWindow, text="Maximo de Iteraciones").grid(column=0,row=3)
    maxIteracion = Entry(newWindow)
    maxIteracion.grid(column=1,row=3)
    
    Label(newWindow, text="paso").grid(column=0,row=4)
    paso = Entry(newWindow)
    paso.grid(column=1,row=4)
    
    resultado = ""
    
    boton = Button(newWindow, text="Iniciar", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: resultado == jacobi(funcion.get(),float(puntoInicial.get()),float(paso.get()),int(maxIteracion.get())))
    boton.grid(column=0, row=6, columnspan=2)
    Label(newWindow, text='{}'.format(resultado)).grid(column=0,row=7, columnspan=2)
    
def gausEidel():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=7)
    
    Label(newWindow, text="Funcion").grid(column=0,row=1)
    funcion =Entry(newWindow)
    funcion.grid(column=1,row=1)
    
    Label(newWindow, text="Punto Inicial").grid(column=0,row=2)
    puntoInicial = Entry(newWindow)
    puntoInicial.grid(column=1,row=2)
    
    Label(newWindow, text="Maximo de Iteraciones").grid(column=0,row=3)
    maxIteracion = Entry(newWindow)
    maxIteracion.grid(column=1,row=3)
    
    resultado = ""
    
    boton = Button(newWindow, text="Iniciar", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: resultado == gauss_seidel(funcion.get(),float(puntoInicial.get()),int(maxIteracion.get())))
    boton.grid(column=0, row=6, columnspan=2)
    Label(newWindow, text='{}'.format(resultado)).grid(column=0,row=7, columnspan=2)
    
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