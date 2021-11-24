import tkinter as tk
import numpy as np
from tkinter import *
from tkinter import filedialog, messagebox, ttk

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
from gausstot import gausstot
from lusimpl import lusimpl
from lupar import lupar
from jacobi import entrada as jacobi
from gseidel import gauss_seidel
from lagrange import lagrange
from vandermonde import vandermonde

def inicio():
    #intrucciones
    boton1 = Button(ventana_principal, text="Numerical solution of nonlinear equations", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: createNewWindow1())    
    boton2 = Button(ventana_principal, text="Solution of systems of linear equations", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: createNewWindow2())
    boton3 = Button(ventana_principal, text="Interpolation", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: createNewWindow3())

    boton1.grid(column=0, row=1, columnspan=2)
    boton2.grid(column=0,row=3, columnspan=2)
    boton3.grid(column=0,row=5, columnspan=2)

def createNewWindow1():
    ventana_principal.iconify()
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=14)
    boton4 = Button(newWindow, text="Incremental searches", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: busquedass())
    boton5 = Button(newWindow, text="Bisection", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: biseccionn())
    boton6 = Button(newWindow, text="False rule", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: reglaFalsa())
    boton7 = Button(newWindow, text="Fixed point", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: puntoFijo())
    boton8 = Button(newWindow, text="Newton", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: newwton())
    boton9 = Button(newWindow, text="Secante", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: secantee())
    boton10 = Button(newWindow, text="Multiple roots", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: raicesMultiples())

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
    ventana_principal.iconify()
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=14)
    boton11 = Button(newWindow, text="Gauss Simple", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: gausSimple())
    boton12 = Button(newWindow, text="Gauss partial pivot", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: gausPP())
    boton13 = Button(newWindow, text="Gauss total pivot", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: gausPT())
    boton14 = Button(newWindow, text="LU factorization", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: factorizacionLuSimple())
    boton15 = Button(newWindow, text="LU factorization (Partial pivot)", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: factorizacionLuParcial())
    boton16 = Button(newWindow, text="Jacobi", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: jacobi())
    boton17 = Button(newWindow, text="Gauss Seidel", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: gausEidel())

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
    ventana_principal.iconify()
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=250)
    canvas.grid(columnspan=2, rowspan=3)
    boton18 = Button(newWindow,text="Vandermonde", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: vandermonde_v())
    #boton19 = Button(newWindow,text="Diferencias Divididas", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: diferenciasDiv())
    boton20 = Button(newWindow,text="Lagrange", bg="SkyBlue", fg="black", width=35, height=2, command = lambda: lagrange_v())

    boton18.grid(column=0, row=0, columnspan=2)
    #boton19.grid(column=0,row=2, columnspan=2)
    boton20.grid(column=0,row=1, columnspan=2)

def busquedass():
    try:
        newWindow = tk.Toplevel(ventana_principal)
        canvas = tk.Canvas(newWindow, width=400, height=450)
        canvas.grid(columnspan=2, rowspan=8)
        
        Label(newWindow, text="Function").grid(column=0,row=1)
        funcion =Entry(newWindow)
        funcion.grid(column=1,row=1)
        
        Label(newWindow, text="Initial Point").grid(column=0,row=2)
        puntoInicial = Entry(newWindow)
        puntoInicial.grid(column=1,row=2)
        
        Label(newWindow, text="Max iterations").grid(column=0,row=3)
        maxIteracion = Entry(newWindow)
        maxIteracion.grid(column=1,row=3)
        
        Label(newWindow, text="Step").grid(column=0,row=4)
        paso = Entry(newWindow)
        paso.grid(column=1,row=4)
        
        def obValores ():
            
            i = busquedas(funcion.get(),float(puntoInicial.get()),float(paso.get()),int(maxIteracion.get()))
            Label(newWindow, text='Result = {}'.format(i)).grid(column=0,row=6, columnspan=2)
        
        boton = Button(newWindow, text="Start", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: obValores())
        boton.grid(column=0, row=7, columnspan=2)
        Label(newWindow, text='').grid(column=0,row=8, columnspan=2)
    except:
        messagebox.showinfo(message="some entrys are empty", title="Error")
        
def biseccionn():
    try:
        newWindow = tk.Toplevel(ventana_principal)
        canvas = tk.Canvas(newWindow, width=400, height=450)
        canvas.grid(columnspan=2, rowspan=8)
        
        Label(newWindow, text="Function").grid(column=0,row=1)
        funcion =Entry(newWindow)
        funcion.grid(column=1,row=1)
        
        Label(newWindow, text="Point a").grid(column=0,row=2)
        puntoInicial = Entry(newWindow)
        puntoInicial.grid(column=1,row=2)
        
        Label(newWindow, text="Point b").grid(column=0,row=3)
        puntoFinal = Entry(newWindow)
        puntoFinal.grid(column=1,row=3)
        
        Label(newWindow, text="Max iterations").grid(column=0,row=4)
        maxIteracion = Entry(newWindow)
        maxIteracion.grid(column=1,row=4)
        
        Label(newWindow, text="Tolerance").grid(column=0,row=5)
        tolerancia = Entry(newWindow)
        tolerancia.grid(column=1,row=5)
        
        def obValores ():
            
            i = biseccion(funcion.get(),float(puntoInicial.get()),float(puntoFinal.get()),int(maxIteracion.get()),float(tolerancia.get()))
            Label(newWindow, text='Result = {}'.format(i)).grid(column=0,row=6, columnspan=2)
        
        boton = Button(newWindow, text="Start", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: obValores())
        boton.grid(column=0, row=7, columnspan=2)
        
        Label(newWindow, text='').grid(column=0,row=8, columnspan=2)
    except:
        messagebox.showinfo(message="some entrys are empty", title="Error")
    
def reglaFalsa():
    try:
        newWindow = tk.Toplevel(ventana_principal)
        canvas = tk.Canvas(newWindow, width=400, height=450)
        canvas.grid(columnspan=2, rowspan=8)
        
        Label(newWindow, text="Function").grid(column=0,row=1)
        funcion =Entry(newWindow)
        funcion.grid(column=1,row=1)
        
        Label(newWindow, text="Point a").grid(column=0,row=2)
        puntoInicial = Entry(newWindow)
        puntoInicial.grid(column=1,row=2)
        
        Label(newWindow, text="Point b").grid(column=0,row=3)
        puntoFinal = Entry(newWindow)
        puntoFinal.grid(column=1,row=3)
        
        Label(newWindow, text="Max iterations").grid(column=0,row=4)
        maxIteracion = Entry(newWindow)
        maxIteracion.grid(column=1,row=4)
        
        Label(newWindow, text="Tolerance").grid(column=0,row=5)
        tolerancia = Entry(newWindow)
        tolerancia.grid(column=1,row=5)
        
        def obValores ():
            
            i = regla_falsa(funcion.get(),float(puntoInicial.get()),float(puntoFinal.get()),int(maxIteracion.get()),float(tolerancia.get()))
            Label(newWindow, text='Result = {}'.format(i)).grid(column=0,row=6, columnspan=2)
        
        boton = Button(newWindow, text="Start", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: obValores())
        boton.grid(column=0, row=7, columnspan=2)
        
        Label(newWindow, text='').grid(column=0,row=8, columnspan=2)
    except:
        messagebox.showinfo(message="some entrys are empty", title="Error")
    
def puntoFijo():
    try:
        newWindow = tk.Toplevel(ventana_principal)
        canvas = tk.Canvas(newWindow, width=400, height=450)
        canvas.grid(columnspan=2, rowspan=8)
        
        Label(newWindow, text="Function").grid(column=0,row=1)
        funcion =Entry(newWindow)
        funcion.grid(column=1,row=1)
        
        Label(newWindow, text="Initial point").grid(column=0,row=2)
        puntoInicial = Entry(newWindow)
        puntoInicial.grid(column=1,row=2)
        
        Label(newWindow, text="Max iterations").grid(column=0,row=3)
        maxIteracion = Entry(newWindow)
        maxIteracion.grid(column=1,row=3)
        
        Label(newWindow, text="Tolerance").grid(column=0,row=4)
        tolerancia = Entry(newWindow)
        tolerancia.grid(column=1,row=4)
        
        def obValores ():
            
            i = puntofijo(funcion.get(),float(puntoInicial.get()),int(maxIteracion.get()),float(tolerancia.get()))
            Label(newWindow, text='Result = {}'.format(i)).grid(column=0,row=6, columnspan=2)
        
        boton = Button(newWindow, text="Start", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: obValores())
        boton.grid(column=0, row=7, columnspan=2)
        
        Label(newWindow, text='').grid(column=0,row=8, columnspan=2)
    except:
        messagebox.showinfo(message="some entrys are empty", title="Error")
    
def newwton():
    try:
        newWindow = tk.Toplevel(ventana_principal)
        canvas = tk.Canvas(newWindow, width=400, height=450)
        canvas.grid(columnspan=2, rowspan=8)
        
        Label(newWindow, text="Function").grid(column=0,row=1)
        funcion =Entry(newWindow)
        funcion.grid(column=1,row=1)
        
        Label(newWindow, text="Initial point").grid(column=0,row=2)
        puntoInicial = Entry(newWindow)
        puntoInicial.grid(column=1,row=2)
        
        Label(newWindow, text="Max iterations").grid(column=0,row=3)
        maxIteracion = Entry(newWindow)
        maxIteracion.grid(column=1,row=3)
        
        Label(newWindow, text="Tolerance").grid(column=0,row=4)
        tolerancia = Entry(newWindow)
        tolerancia.grid(column=1,row=4)
        
        def obValores ():
            
            i = newton(funcion.get(),float(puntoInicial.get()),int(maxIteracion.get()),float(tolerancia.get()))
            Label(newWindow, text='Result = {}'.format(i)).grid(column=0,row=6, columnspan=2)
        
        boton = Button(newWindow, text="Start", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: obValores())
        boton.grid(column=0, row=7, columnspan=2)
        
        Label(newWindow, text='{}').grid(column=0,row=8, columnspan=2)
    except:
        messagebox.showinfo(message="some entrys are empty", title="Error")
    
def secantee():
    try:
        newWindow = tk.Toplevel(ventana_principal)
        canvas = tk.Canvas(newWindow, width=400, height=450)
        canvas.grid(columnspan=2, rowspan=7)
        
        Label(newWindow, text="Function").grid(column=0,row=1)
        funcion =Entry(newWindow)
        funcion.grid(column=1,row=1)
        
        Label(newWindow, text="Point a").grid(column=0,row=2)
        puntoa = Entry(newWindow)
        puntoa.grid(column=1,row=2)
        
        Label(newWindow, text="Point b").grid(column=0,row=3)
        puntob = Entry(newWindow)
        puntob.grid(column=1,row=3)
        
        Label(newWindow, text="Max iterations").grid(column=0,row=4)
        maxIteracion = Entry(newWindow)
        maxIteracion.grid(column=1,row=4)
        
        Label(newWindow, text="Tolerance").grid(column=0,row=5)
        tolerancia = Entry(newWindow)
        tolerancia.grid(column=1,row=5)
        
        def obValores ():
            
            i = secante(funcion.get(),float(puntoa.get()),float(puntob.get()),int(maxIteracion.get()),float(tolerancia.get))
            Label(newWindow, text='Result = {}'.format(i)).grid(column=0,row=6, columnspan=2)
        
        boton = Button(newWindow, text="Start", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: obValores())
        boton.grid(column=0, row=7, columnspan=2)
        
        Label(newWindow, text='{}').grid(column=0,row=8, columnspan=2)
    except:
        messagebox.showinfo(message="some entrys are empty", title="Error")
    
def raicesMultiples():
    try:
        newWindow = tk.Toplevel(ventana_principal)
        canvas = tk.Canvas(newWindow, width=400, height=450)
        canvas.grid(columnspan=2, rowspan=7)
        
        Label(newWindow, text="Function").grid(column=0,row=1)
        funcion =Entry(newWindow)
        funcion.grid(column=1,row=1)
        
        Label(newWindow, text="Point a").grid(column=0,row=2)
        puntoa = Entry(newWindow)
        puntoa.grid(column=1,row=2)
        
        Label(newWindow, text="Max iterations").grid(column=0,row=3)
        maxIteracion = Entry(newWindow)
        maxIteracion.grid(column=1,row=3)
        
        Label(newWindow, text="Tolerance").grid(column=0,row=4)
        tolerancia = Entry(newWindow)
        tolerancia.grid(column=1,row=4)
        
        def obValores ():
            
            i = raicesmlps(funcion.get(),float(puntoa.get()),int(maxIteracion.get()),float(tolerancia.get))
            Label(newWindow, text='Result = {}'.format(i)).grid(column=0,row=6, columnspan=2)
        
        boton = Button(newWindow, text="Start", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: obValores())
        boton.grid(column=0, row=7, columnspan=2)
        
        Label(newWindow, text='{}').grid(column=0,row=8, columnspan=2)
    except:
        messagebox.showinfo(message="some entrys are empty", title="Error")
    
def gausSimple():
    try:
        newWindow = tk.Toplevel(ventana_principal)
        canvas = tk.Canvas(newWindow, width=400, height=450)
        canvas.grid(columnspan=10, rowspan=11)
        
        Label(newWindow, text="Unknowns").grid(column=0,row=1)
        incognita = Entry(newWindow)
        incognita.grid(column=1,row=1)
        matriz = []
        vector = []
        def genMatriz (x):
            matriz.clear()
            vector.clear()
            for i in range(x):
                Label(newWindow, text="=").grid(column=x,row=i+3, sticky="w")
                a = [0]*x
                for j in range(x):
                    casilla = Entry(newWindow, width=10)
                    casilla.grid(column=j, row=i+3)
                    a[j] = casilla
                matriz.append(a)
                vectorr = Entry(newWindow, width=7)
                vector.append(vectorr)
                vectorr.grid(column=x+1, row=i+3, sticky="e")
                
            array = np.array(matriz)
            
        generar = Button(newWindow, text="Generate", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: genMatriz(int(incognita.get())))
        generar.grid(column=0, row=2, columnspan=10)
        
        def obValores (m):
            c = np.zeros((m,m))
            d = np.zeros(m)
            for i in range(m):
                for j in range(m):
                    a = float(matriz[i][j].get())
                    c[i,j] = a
                b = float(vector[i].get())
                d[i] = b
            i = gausspl(c,d)
            matriz.clear()
            vector.clear()
            Label(newWindow, text='Result = {}'.format(i)).grid(column=0,row=10, columnspan=10)
        
        boton = Button(newWindow, text="Start", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: obValores(int(incognita.get())))
        boton.grid(column=0, row=11, columnspan=10)
        Label(newWindow, text='').grid(column=0,row=12, columnspan=10)
    except:
        messagebox.showinfo(message="some entrys are empty", title="Error")
    
def gausPP():
    try:
        newWindow = tk.Toplevel(ventana_principal)
        canvas = tk.Canvas(newWindow, width=400, height=450)
        canvas.grid(columnspan=10, rowspan=11)
        
        Label(newWindow, text="Unknowns").grid(column=0,row=1)
        incognita = Entry(newWindow)
        incognita.grid(column=1,row=1)
        matriz = []
        vector = []
        def genMatriz (x):
            matriz.clear()
            vector.clear()
            for i in range(x):
                Label(newWindow, text="=").grid(column=x,row=i+3, sticky="w")
                a = [0]*x
                for j in range(x):
                    casilla = Entry(newWindow, width=10)
                    casilla.grid(column=j, row=i+3)
                    a[j] = casilla
                matriz.append(a)
                vectorr = Entry(newWindow, width=7)
                vector.append(vectorr)
                vectorr.grid(column=x+1, row=i+3, sticky="e")
                
            array = np.array(matriz)
            
        generar = Button(newWindow, text="Generate", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: genMatriz(int(incognita.get())))
        generar.grid(column=0, row=2, columnspan=10)
        
        def obValores (m):
            c = np.zeros((m,m))
            d = np.zeros(m)
            for i in range(m):
                for j in range(m):
                    a = float(matriz[i][j].get())
                    c[i,j] = a
                b = float(vector[i].get())
                d[i] = b
            i = gausspar(c,d)
            matriz.clear()
            vector.clear()
            Label(newWindow, text='Result = {}'.format(i)).grid(column=0,row=10, columnspan=10)
        
        boton = Button(newWindow, text="Start", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: obValores(int(incognita.get())))
        boton.grid(column=0, row=10, columnspan=10)
        Label(newWindow, text='').grid(column=0,row=11, columnspan=2)
    except:
        messagebox.showinfo(message="some entrys are empty", title="Error")
    
def gausPT():
    try:
        newWindow = tk.Toplevel(ventana_principal)
        canvas = tk.Canvas(newWindow, width=400, height=450)
        canvas.grid(columnspan=10, rowspan=11)
        
        Label(newWindow, text="Unknowns").grid(column=0,row=1)
        incognita = Entry(newWindow)
        incognita.grid(column=1,row=1)
        matriz = []
        vector = []
        def genMatriz (x):
            matriz.clear()
            vector.clear()
            for i in range(x):
                Label(newWindow, text="=").grid(column=x,row=i+3, sticky="w")
                a = [0]*x
                for j in range(x):
                    casilla = Entry(newWindow, width=10)
                    casilla.grid(column=j, row=i+3)
                    a[j] = casilla
                matriz.append(a)
                vectorr = Entry(newWindow, width=7)
                vector.append(vectorr)
                vectorr.grid(column=x+1, row=i+3, sticky="e")
                
            array = np.array(matriz)
            
        generar = Button(newWindow, text="Generate", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: genMatriz(int(incognita.get())))
        generar.grid(column=0, row=2, columnspan=10)
        
        def obValores (m):
            c = np.zeros((m,m))
            d = np.zeros(m)
            for i in range(m):
                for j in range(m):
                    a = float(matriz[i][j].get())
                    c[i,j] = a
                b = float(vector[i].get())
                d[i] = b
            i = gausstot(c,d)
            matriz.clear()
            vector.clear()
            Label(newWindow, text='Result = {}'.format(i)).grid(column=0,row=10, columnspan=10)
        
        boton = Button(newWindow, text="Start", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: obValores(int(incognita.get())))
        boton.grid(column=0, row=10, columnspan=10)
        Label(newWindow, text='').grid(column=0,row=11, columnspan=2)
    except:
        messagebox.showinfo(message="some entrys are empty", title="Error")
    
def factorizacionLuSimple():
    try:
        newWindow = tk.Toplevel(ventana_principal)
        canvas = tk.Canvas(newWindow, width=400, height=450)
        canvas.grid(columnspan=10, rowspan=11)
        
        Label(newWindow, text="Unknowns").grid(column=0,row=1)
        incognita = Entry(newWindow)
        incognita.grid(column=1,row=1)
        matriz = []
        vector = []
        def genMatriz (x):
            matriz.clear()
            vector.clear()
            for i in range(x):
                Label(newWindow, text="=").grid(column=x,row=i+3, sticky="w")
                a = [0]*x
                for j in range(x):
                    casilla = Entry(newWindow, width=10)
                    casilla.grid(column=j, row=i+3)
                    a[j] = casilla
                matriz.append(a)
                vectorr = Entry(newWindow, width=7)
                vector.append(vectorr)
                vectorr.grid(column=x+1, row=i+3, sticky="e")
                
            array = np.array(matriz)
            
        generar = Button(newWindow, text="Generate", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: genMatriz(int(incognita.get())))
        generar.grid(column=0, row=2, columnspan=10)
        
        def obValores (m):
            c = np.zeros((m,m))
            d = np.zeros(m)
            for i in range(m):
                for j in range(m):
                    a = float(matriz[i][j].get())
                    c[i,j] = a
                b = float(vector[i].get())
                d[i] = b
            i = lusimpl(c,d)
            matriz.clear()
            vector.clear()
            Label(newWindow, text='Result = {}'.format(i)).grid(column=0,row=10, columnspan=10)
        
        boton = Button(newWindow, text="Start", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: obValores(int(incognita.get())))
        boton.grid(column=0, row=10, columnspan=10)
        Label(newWindow, text='').grid(column=0,row=11, columnspan=2)
    except:
        messagebox.showinfo(message="some entrys are empty", title="Error")
    
def factorizacionLuParcial():
    try:
        newWindow = tk.Toplevel(ventana_principal)
        canvas = tk.Canvas(newWindow, width=400, height=450)
        canvas.grid(columnspan=10, rowspan=11)
        
        Label(newWindow, text="Unknowns").grid(column=0,row=1)
        incognita = Entry(newWindow)
        incognita.grid(column=1,row=1)
        matriz = []
        vector = []
        def genMatriz (x):
            matriz.clear()
            vector.clear()
            for i in range(x):
                Label(newWindow, text="=").grid(column=x,row=i+3, sticky="w")
                a = [0]*x
                for j in range(x):
                    casilla = Entry(newWindow, width=10)
                    casilla.grid(column=j, row=i+3)
                    a[j] = casilla
                matriz.append(a)
                vectorr = Entry(newWindow, width=7)
                vector.append(vectorr)
                vectorr.grid(column=x+1, row=i+3, sticky="e")
                
            array = np.array(matriz)
            
        generar = Button(newWindow, text="Generate", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: genMatriz(int(incognita.get())))
        generar.grid(column=0, row=2, columnspan=10)
        
        def obValores (m):
            c = np.zeros((m,m))
            d = np.zeros(m)
            for i in range(m):
                for j in range(m):
                    a = float(matriz[i][j].get())
                    c[i,j] = a
                b = float(vector[i].get())
                d[i] = b
            i = lupar(c,d)
            matriz.clear()
            vector.clear()
            Label(newWindow, text='Result = {}'.format(i)).grid(column=0,row=10, columnspan=10)
        
        boton = Button(newWindow, text="Start", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: obValores(int(incognita.get())))
        boton.grid(column=0, row=10, columnspan=10)
        Label(newWindow, text='').grid(column=0,row=11, columnspan=2)
    except:
        messagebox.showinfo(message="some entrys are empty", title="Error")
    
def jacobi():
    try:
        newWindow = tk.Toplevel(ventana_principal)
        canvas = tk.Canvas(newWindow, width=400, height=450)
        canvas.grid(columnspan=10, rowspan=11)
        
        Label(newWindow, text="Unknowns").grid(column=0,row=1)
        incognita = Entry(newWindow)
        incognita.grid(column=1,row=1)
        
        Label(newWindow, text="Tolerance").grid(column=0,row=2)
        tolerancia = Entry(newWindow)
        tolerancia.grid(column=1,row=2)
        
        Label(newWindow, text="Max iterations").grid(column=0,row=3)
        maxIteracion = Entry(newWindow)
        maxIteracion.grid(column=1,row=3)
        
        matriz = []
        vector = []
        def genMatriz (x):
            matriz.clear()
            vector.clear()
            for i in range(x):
                Label(newWindow, text="=").grid(column=x,row=i+5, sticky="w")
                a = [0]*x
                for j in range(x):
                    casilla = Entry(newWindow, width=10)
                    casilla.grid(column=j, row=i+5)
                    a[j] = casilla
                matriz.append(a)
                vectorr = Entry(newWindow, width=7)
                vector.append(vectorr)
                vectorr.grid(column=x+1, row=i+5, sticky="e")
                
            array = np.array(matriz)
            
        generar = Button(newWindow, text="Generate", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: genMatriz(int(incognita.get())))
        generar.grid(column=0, row=4, columnspan=10)
        
        def obValores (m):
            c = np.zeros((m,m))
            d = np.zeros(m)
            for i in range(m):
                for j in range(m):
                    a = float(matriz[i][j].get())
                    c[i,j] = a
                b = float(vector[i].get())
                d[i] = b
            i = jacobi(c,d,int(maxIteracion.get()),float(tolerancia.get))
            matriz.clear()
            vector.clear()
            Label(newWindow, text='Result = {}'.format(i)).grid(column=0,row=10, columnspan=10)
        
        boton = Button(newWindow, text="Start", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: obValores(int(incognita.get())))
        boton.grid(column=0, row=11, columnspan=10)
        Label(newWindow, text='').grid(column=0,row=12, columnspan=10)
    except:
        messagebox.showinfo(message="some entrys are empty", title="Error")
    
def gausEidel():
    try:
        newWindow = tk.Toplevel(ventana_principal)
        canvas = tk.Canvas(newWindow, width=400, height=450)
        canvas.grid(columnspan=10, rowspan=11)
        
        Label(newWindow, text="Unknowns").grid(column=0,row=1)
        incognita = Entry(newWindow)
        incognita.grid(column=1,row=1)
        
        Label(newWindow, text="Max iterations").grid(column=0,row=2)
        maxIteracion = Entry(newWindow)
        maxIteracion.grid(column=1,row=2)
        
        matriz = []
        vector = []
        def genMatriz (x):
            matriz.clear()
            vector.clear()
            for i in range(x):
                Label(newWindow, text="=").grid(column=x,row=i+4, sticky="w")
                a = [0]*x
                for j in range(x):
                    casilla = Entry(newWindow, width=10)
                    casilla.grid(column=j, row=i+4)
                    a[j] = casilla
                matriz.append(a)
                vectorr = Entry(newWindow, width=7)
                vector.append(vectorr)
                vectorr.grid(column=x+1, row=i+4, sticky="e")
                
            array = np.array(matriz)
            
        generar = Button(newWindow, text="Generate", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: genMatriz(int(incognita.get())))
        generar.grid(column=0, row=3, columnspan=10)
        
        def obValores (m):
            c = np.zeros((m,m))
            d = np.zeros(m)
            for i in range(m):
                for j in range(m):
                    a = float(matriz[i][j].get())
                    c[i,j] = a
                b = float(vector[i].get())
                d[i] = b
            i = gauss_seidel(c,d,int(maxIteracion.get))
            matriz.clear()
            vector.clear()
            Label(newWindow, text='Result = {}'.format(i)).grid(column=0,row=10, columnspan=10)
        
        boton = Button(newWindow, text="Start", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: obValores(int(incognita.get())))
        boton.grid(column=0, row=11, columnspan=10)
        Label(newWindow, text='').grid(column=0,row=12, columnspan=10)
    except:
        messagebox.showinfo(message="some entrys are empty", title="Error")
    
def vandermonde_v():
    try:
        newWindow = tk.Toplevel(ventana_principal)
        canvas = tk.Canvas(newWindow, width=400, height=450)
        canvas.grid(columnspan=10, rowspan=12)
        
        Label(newWindow, text="Points").grid(column=0,row=1)
        incognita = Entry(newWindow)
        incognita.grid(column=1,row=1)
        vectorx = []
        vectory = []
        def genMatriz (x):
            vectorx.clear()
            vectory.clear()
            for i in range(x):
                Label(newWindow, text="X").grid(column=0,row=3)
                Label(newWindow, text="Y").grid(column=1,row=3)
                vectora = Entry(newWindow, width=12)
                vectorb = Entry(newWindow, width=12)
                vectorx.append(vectora)
                vectory.append(vectorb)
                vectora.grid(column=0, row=i+4, sticky="e")
                vectorb.grid(column=1, row=i+4, sticky="e")
            
        generar = Button(newWindow, text="Generate", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: genMatriz(int(incognita.get())))
        generar.grid(column=0, row=2, columnspan=10)
        
        def obValores (m):
            x = np.zeros(m)
            y = np.zeros(m)
            for i in range(m):
                x[i] = float(vectorx[i].get())
                y[i] = float(vectory[i].get())
            i = vandermonde(x,y)
            vectorx.clear()
            vectory.clear()
            Label(newWindow, text='Result = {}'.format(i)).grid(column=0,row=10, columnspan=10)
        
        boton = Button(newWindow, text="Start", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: obValores(int(incognita.get())))
        boton.grid(column=0, row=11, columnspan=10)
        Label(newWindow, text='').grid(column=0,row=12, columnspan=10)
    except:
        messagebox.showinfo(message="some entrys are empty", title="Error")
    
'''def diferenciasDiv():
    newWindow = tk.Toplevel(ventana_principal)
    canvas = tk.Canvas(newWindow, width=400, height=450)
    canvas.grid(columnspan=2, rowspan=5)'''
    
def lagrange_v():
    try:
        newWindow = tk.Toplevel(ventana_principal)
        canvas = tk.Canvas(newWindow, width=400, height=450)
        canvas.grid(columnspan=10, rowspan=11)
        
        Label(newWindow, text="Point").grid(column=0,row=1)
        incognita = Entry(newWindow)
        incognita.grid(column=1,row=1)
        vectorx = []
        vectory = []
        def genMatriz (x):
            vectorx.clear()
            vectory.clear()
            for i in range(x):
                Label(newWindow, text="X").grid(column=0,row=3)
                Label(newWindow, text="Y").grid(column=1,row=3)
                vectora = Entry(newWindow, width=12)
                vectorb = Entry(newWindow, width=12)
                vectorx.append(vectora)
                vectory.append(vectorb)
                vectora.grid(column=0, row=i+4, sticky="e")
                vectorb.grid(column=1, row=i+4, sticky="e")
            
        generar = Button(newWindow, text="Generate", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: genMatriz(int(incognita.get())))
        generar.grid(column=0, row=2, columnspan=10)
        
        def obValores (m):
            
            x = np.zeros(m)
            y = np.zeros(m)
            for i in range(m):
                x[i] = float(vectorx[i].get())
                y[i] = float(vectory[i].get())
            i = lagrange(x,y)
            vectorx.clear()
            vectory.clear()
            Label(newWindow, text='Result = {}'.format(i)).grid(column=0,row=10, columnspan=10)
        
        boton = Button(newWindow, text="Start", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: obValores(int(incognita.get())))
        boton.grid(column=0, row=11, columnspan=10)
        Label(newWindow, text='').grid(column=0,row=12, columnspan=2)
    except:
        messagebox.showinfo(message="some entrys are empty", title="Error")
    
    
str = ''
pestas_color="DarkGrey"
ventana_principal = tk.Tk()
canvas = tk.Canvas(ventana_principal, width=400, height=450)
canvas.grid(columnspan=2, rowspan=14)
ventana_principal.title("Numerical Analysis")#TITULO DE LA VENTANA
label1= Label(ventana_principal, text="Welcome to numerical analysis project", bg="SkyBlue", font=("Calibri", 13))
label1.grid(column=0,row=0, columnspan=5)
boton = Button(ventana_principal, text="Start", bg="SkyBlue", fg="black", width=35, height=2, command= lambda: inicio())
boton.grid(column=0, row=1, columnspan=2)

label5 = Label(ventana_principal, text="")

ventana_principal.mainloop()