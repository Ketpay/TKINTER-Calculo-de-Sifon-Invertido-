##############################################################
#----------------------Libraries------------------------------
##############################################################

#Las librerias tkinter sirven para generar las vistas
#La libreria pandas permite generar archivos excel

from tkinter import*  # importar interfaz

from tkinter import messagebox  # pop ups mensajes

from tkinter import filedialog # guardar archivos

from tkinter.filedialog import asksaveasfile, askdirectory  #descargar archivos

import tkinter as tk  # iniciar interfaz

# import pandas as pd  # generar archivos excel

# import numpy as np # libreria de matrices 

# import xlsxwriter  # escribir excels

# from statistics import variance #libreria para haver varianza

import math #libreria para uso de funciones matematicas

# import matplotlib.pyplot as plt # permite generar graficos

# import os  #permite acceder a las fucciones principales de la pc - navegar por archivos de pc


##############################################################
#----------------------Variables globales---------------------
##############################################################
#variables que pasaran de funcion a funcion

# global text_sifon
##############################################################
#----------------------Funciones------------------------------
##############################################################

def sifon_1():
    
    
    #variables globales --------------------------------------
    global text_sifon
    #--------------------------------------
    text_sifon.destroy()
    text_sifon=Label(Frame2,text="Ramas Oblicuas",font="Verdana 10 bold", fg="white", bg="#282923")
    text_sifon.place(x="120",y="20")
    pass

def sifon_2():
    
    
    #variables globales --------------------------------------
    global text_sifon
    #--------------------------------------
    text_sifon.destroy()
    text_sifon=Label(Frame2,text="Pozo Vertical",font="Verdana 10 bold", fg="white", bg="#282923")
    text_sifon.place(x="120",y="20")
    pass

def sifon_3():
    
    
    #variables globales --------------------------------------
    global text_sifon
    #--------------------------------------
    text_sifon.destroy()
    text_sifon=Label(Frame2,text="Ramas Verticales",font="Verdana 10 bold", fg="white", bg="#282923")
    text_sifon.place(x="120",y="20")
    pass
def sifon_4():
    
    
    #variables globales --------------------------------------
    global text_sifon
    #--------------------------------------
    text_sifon.destroy()
    text_sifon=Label(Frame2,text="Con Cámara De Limpieza",font="Verdana 10 bold", fg="white", bg="#282923")
    text_sifon.place(x="120",y="20")
    pass


def limpiar():

    #variables globales --------------------------------------
    
    pass



#----------------------Descargar------------------------------
#Esta funcion permite descargar el formulario en excel basandose en los ajustes que se le da.

def descargar():
#----------------------variables globales------------------------------
  
    pass


#----------------------Abrir------------------------------
#Esta funcion permite abrir el archivo a procesar.

def abrir():

    #variables globales-------------------------------
   
   
    pass

#----------------------Procesar------------------------------
#Esta funcion permite procesar los datos y dar resultados
def procesar():

    #variables globales-------------------------------

    global z
    global q
    global s
    global b
    global n
    global y
    global v
    global a
    global t
    global lht
    global ci
    global cf
    global le
    global ang
    ang=float(ang.get())
    area=round(float(q.get())/float(v.get()),2)
    print("Area:",area)
    diametro=round(math.sqrt(area*4/math.pi),2)
    print("Daimetro:",diametro)
    pulgadas=round(diametro/0.0254,2)
    print("pulgadas:",pulgadas)
    T1=round(float(b.get())+(float(y.get())*float(z.get())*2),2)
    print("T1:",T1)
    T2=round(pulgadas,0)*0.0254
    print("T2:",T2)
    LT=round((T1-T2)/(2*math.tan(math.radians(float(a.get())))),2)
    print("LT:",LT)
    LT2=round(4*T2,1)
    print("LT2:",LT2)
    cota_fondo_1=round(float(ci.get())-(0.001*float(le.get())),2)
    print("cota_fondo_1:",cota_fondo_1)
    nivel_agua_1=round(cota_fondo_1+float(y.get()),2)
    print("nivel_agua_1:",nivel_agua_1)
    v1=round(float(q.get())/((T2**2)*math.pi/4),2)
    print("v1:",v1)
    vt=round((float(y.get()) *float(z.get())+float(b.get()))*float(y.get())/2,2)
    print("vt:",vt)
    hte=(round(pulgadas,0)*0.0254)/math.cos(math.radians(ang))
    print("hte:",hte)
    hv1=(v1**2)/(2*9.81)
    print("hv1:",hv1)
    hv2=(vt**2)/(2*9.81)
    print("hv2:",hv2)
    hv=hv1-hv2
    print("1.5hv:",hv)
    hv=hv*1.5
    print("hv:",hv)
    cota_fondo_2=round(nivel_agua_1-(hte+hv),2)
    print("cota_fondo_2:",cota_fondo_2)
    cota_fondo_3=round(cota_fondo_2-math.radians(ang)*5,2)
    print("cota_fondo_3:",cota_fondo_3)
    h4=float(lht.get())*5/1000

    cota_fondo_4=round(cota_fondo_3-h4,2)
    print("cota_fondo_4:",cota_fondo_4)
    cota_fondo_5=round((math.radians(ang)*4)+cota_fondo_4,2)
    print("cota_fondo_5:",cota_fondo_5)
    p_entrada=(3/4)*(round(pulgadas,0)*0.0254)
    print("p_entrada:",p_entrada)
    p_salida=(1/2)*(round(pulgadas,0)*0.0254)
    print("p_salida:",p_salida)
    p=round(float(cf.get())-cota_fondo_5,3)
    print("p:",p)
    x_entrada=round((math.radians(ang)*5)/(math.tan(math.radians(float(ang)))),2)
    print("x_entrada:",x_entrada)
    y_entrada=round(math.radians(ang)*5,2)
    print("y_entrada:",y_entrada)
    inclinacion_entrada=round(x_entrada/y_entrada,2)
    print("inclinacion_entrada:",inclinacion_entrada)
    x_salida=round((math.radians(ang)*4)/(math.tan(math.radians(float(ang)))),2)
    print("x_salida:",x_salida)
    y_salida=round(math.radians(ang)*4,2)
    print("y_salida:",y_salida)
    inclinacion_salida =round(x_salida-y_salida,2) 
    print("inclinacion_salida:",inclinacion_salida)
    c1_t=round(cota_fondo_1,2)
    print("cota1+tirante:",c1_t)
    c6_t=round(float(cf.get()),2)
    print("cota6+tirante:",c6_t)
    carga=round(float(y.get())*(c1_t-c6_t),2)
    print("carga dispoible:",carga)
    entrada=round(p_salida*0.0938,2)
    print("entrada:",entrada)
    salida=round(p_entrada*0.0938,2)
    print("salida:",salida)
    perdida=round(entrada+salida+0.061+0.022,2)
    print("perdida total:",perdida)
    porcentaje=round(perdida*(1+0.1),2)
    print("porcentaje:",porcentaje)
    cotas=round(cota_fondo_1- cota_fondo_2,3)
    print("∆ Cota 1 y Cota 2:",cotas)
    altura=round(float(y.get())+cotas- hte,3)
    print("alturas de sumergencia:",altura)
    longitud=round(3*(pulgadas*0.0254),1)
    print(" Longitud de proteccion :",longitud)


    pass
#----------------------Graficos------------------------------
#Esta funcion permite ver los graficos de lo procesado

# def graficos():
#     #----------------------genera graficos------------------------------
  

#     pass


# #----------------------Abrir carpeta------------------------------
# #Esta funcion permite abrir la carpeta de ubicacion del archivo

# def abrir_carpeta():
#     #----------------------permite abrir la carpeta donde procesaste el archivo------------------------------
 
#     pass


#----------------------Teoria------------------------------
#Esta funcion permite abrir una ventana y ver la teoria 

def teoria():

    #----------------------abre una nueva vista q nos muestra la teoria------------------------------
    # global imagen_bg
    teoria = tk.Toplevel(app)

    teoria.title("Ver Teoria") # titulo
    teoria.geometry("550x300") # geometria inicial
    teoria.resizable(0, 0) # no e sposible  agrandar
    teoria.iconbitmap("icon.ico")
    # fondo=Label(teoria,image=imagen_bg).place(x=0,y=0)
    teoria.config(bg="#FFFFFF") #  background color

    texto=Label(teoria,text="TEORIA DEL ANÁLISIS DE DOBLE MASA",font="Verdana 14 bold", fg="black", bg="#ffffff")
    texto.place(x="20", y="15")
    texto=Label(teoria,text="El método de doble masa considera que, en una zona meteorológica",font="Verdana 10 bold", fg="black", bg="#ffffff")
    texto.place(x="20", y="100")
    texto=Label(teoria,text="homogénea, los valores de precipitación que ocurren en diferentes ",font="Verdana 10 bold", fg="black", bg="#ffffff")
    texto.place(x="20", y="120")
    texto=Label(teoria,text="puntos de esa zona en períodos anuales o estacionales guardan una ",font="Verdana 10 bold", fg="black", bg="#ffffff")
    texto.place(x="20", y="140")
    texto=Label(teoria,text="relación de proporcionalidad que puede representarse gráficamente.",font="Verdana 10 bold", fg="black", bg="#ffffff")
    texto.place(x="20", y="160")




    pass



#----------------------Acerca------------------------------
#Esta funcion permite mirar la informacion del creador

def acerca():
    global logo

    acerca = tk.Toplevel(app)

    acerca.title("Acerca de ...") # titulo
    acerca.geometry("460x400") # geometria inicial
    acerca.resizable(0, 0) # no e sposible  agrandar
    acerca.iconbitmap("icon.ico")
    acerca.config(bg="#282923") #  background color
    fondo=Label(acerca,image=logo).place(x=0,y=0)
    texto=Label(acerca,text="GRUPO ...",font="Verdana 14 bold", fg="white", bg="#282923")
    texto.place(x="20", y="100")
    texto=Label(acerca,text="Integrantes:",font="Verdana 10 bold", fg="white", bg="#282923")
    texto.place(x="20", y="130")
    texto=Label(acerca,text="- Roman Saldaña, Sebastian Andre",font="Verdana 10 bold", fg="white", bg="#282923")
    texto.place(x="20", y="160")
    # texto=Label(acerca,text="- Sandoval Peña, Carlos Anderson",font="Verdana 10 bold", fg="white", bg="#282923")
    # texto.place(x="20", y="190")
    # texto=Label(acerca,text="- Rodríguez Ñañaque, Melvin Jair",font="Verdana 10 bold", fg="white", bg="#282923")
    # texto.place(x="20", y="220")
    # texto=Label(acerca,text="- Reluz Muro, Oscar José ",font="Verdana 10 bold", fg="white", bg="#282923")
    # texto.place(x="20", y="250")
    # texto=Label(acerca,text="- Sacaca Mamani, Alcides Franco",font="Verdana 10 bold", fg="white", bg="#282923")
    # texto.place(x="20", y="280")
    # texto=Label(acerca,text="- Roman Saldaña, Sebastian Andre",font="Verdana 10 bold", fg="white", bg="#282923")
    # texto.place(x="20", y="310")
    # texto=Label(acerca,text="- Roncal Snchez, Luis Gianfranco",font="Verdana 10 bold", fg="white", bg="#282923")
    # texto.place(x="20", y="340")
    pass


#----------------------Salir------------------------------
#Esta funcion permite cerrar la app

def salir():
    app.destroy()
    pass

#----------------------Limpiar------------------------------
#Esta funcion limpia todo lo realizado

def limpiar():

    #variables globales --------------------------------------
    
    pass



def leyenda():

    #variables globales --------------------------------------
    
    pass


def aplicacion():

    pass
##############################################################
#----------------------INICIO de la APP-----------------------
##############################################################


# declaramos propiedades de la pagina principal
app = Tk() # Creamos la App
app.title("App") # titulo
app.geometry("570x500") # geometria inicial
app.resizable(0, 0) # no e sposible  agrandar
app.iconbitmap("icon.ico")
# imagen_bg=PhotoImage(file="bg2.png")
# fondo=Label(app,image=imagen_bg).place(x=0,y=0)
app.config(bg="#282923") #  background color

# ---------------------------------------------------------------
#                   Menu
# ---------------------------------------------------------------


barraMenu = Menu(app)
mnuOpciones = Menu(barraMenu)
mnuInicio = Menu(barraMenu)
mnuAYUDA = Menu(barraMenu)
submenu = Menu(mnuOpciones, tearoff=0)

#Menu inicio----------------------------------
mnuInicio=Menu(barraMenu,tearoff=0)
# mnuInicio.add_command(label = "Abrir",command=abrir)


mnuInicio.add_separator()
mnuInicio.add_command(label = "Salir",command=salir)

#Menu opciones------------------------------------

mnuOpciones=Menu(barraMenu,tearoff=0)
mnuOpciones.add_command(label = "Limpiar",command=limpiar)


#Menu ayuda--------------------------------------

mnuAYUDA=Menu(barraMenu,tearoff=0)

mnuAYUDA.add_command(label = "Ver Teoria",command=teoria)

mnuAYUDA.add_separator()
mnuAYUDA.add_command(label = "Acerca de ...",command=acerca)

#inicio de los menus-----------------------------
barraMenu.add_cascade(label = "Inicio", menu = mnuInicio)
barraMenu.add_cascade(label = "Opciones", menu = mnuOpciones)
barraMenu.add_cascade(label = "Ayuda", menu = mnuAYUDA)

app.config(menu = barraMenu)


# ---------------------------------------------------------------
#                   Carga de Imagenes
# ---------------------------------------------------------------

# logo = PhotoImage(file="logo.png") 
# logo = logo.subsample(2, 2)
# sifon1 = PhotoImage(file="1.png") 
# sifon1 = sifon1.subsample(3, 3)
# sifon2 = PhotoImage(file="2.png") 
# sifon2 = sifon2.subsample(3, 3)
# sifon3 = PhotoImage(file="3.png") 
# sifon3 = sifon3.subsample(3, 3)
# sifon4 = PhotoImage(file="4.png") 
# sifon4 = sifon1.subsample(1, 1)
# imagen_bg=PhotoImage(file="img2.png")

# # ------------------------------------------------------------------------------
# #   Descripcion - Titulo
# # ------------------------------------------------------------------------------

texto=Label(app,text="Calculo de Sifones",font="Verdana 12 bold", fg="white", bg="#282923")
texto.place(x="20", y="15")

# # ------------------------------------------------------------------------------
# #   Boton DE ABRIR ARCHIVO y nombre del archivo
# # ------------------------------------------------------------------------------



# # ------------------------------------------------------------------------------
# #  Frame 1
# # ------------------------------------------------------------------------------



# # ------------------------------------------------------------------------------
# #  Frame 2
# # ------------------------------------------------------------------------------

Frame2=Frame(width=550, height=410)
# Frame2.pack()
Frame2.config(bd=4,relief="groove", bg="#282923")
Frame2.place(x="10",y="60")

text2=Label(Frame2,text="-Ingresar Datos-",font="Verdana 10 bold", fg="white", bg="#282923")
text2.place(x="0",y="0")
text=Label(Frame2,text="Tipo de sifon:",font="Verdana 10 bold", fg="white", bg="#282923")
text.place(x="10",y="20")
text_sifon=Label(Frame2,text="...",font="Verdana 10 bold", fg="white", bg="#282923")
text_sifon.place(x="120",y="20")
# # ------------------------------------------------------------------------------
# #  Frame 2_1
# # ------------------------------------------------------------------------------

Frame2_1=Frame(Frame2,width=520, height=130)
# Frame2.pack()
Frame2_1.config(bd=4,relief="groove", bg="#282923")
Frame2_1.place(x="10",y="50")



zt=Label(Frame2_1,text="Z=",font="Verdana 9 bold", fg="white", bg="#282923",justify="left")
zt.place(x="10",y="5")
z=tk.Entry(Frame2_1, width="5",)
z.place(x="40",y="5")

qt=Label(Frame2_1,text="Q=",font="Verdana 9 bold", fg="white", bg="#282923",justify="left")
qt.place(x="10",y="30")
q=tk.Entry(Frame2_1, width="5",)
q.place(x="40",y="30")

st=Label(Frame2_1,text="S=",font="Verdana 9 bold", fg="white", bg="#282923",justify="left")
st.place(x="10",y="55")
s=tk.Entry(Frame2_1, width="5",)
s.place(x="40",y="55")

angt=Label(Frame2_1,text="Ang=",font="Verdana 9 bold", fg="white", bg="#282923",justify="left")
angt.place(x="0",y="80")
ang=tk.Entry(Frame2_1, width="5",)
ang.place(x="40",y="80")


bt=Label(Frame2_1,text="b=",font="Verdana 9 bold", fg="white", bg="#282923",justify="left")
bt.place(x="80",y="5")
b=tk.Entry(Frame2_1, width="5",)
b.place(x="110",y="5")

nt=Label(Frame2_1,text="n=",font="Verdana 9 bold", fg="white", bg="#282923",justify="left")
nt.place(x="80",y="30")
n=tk.Entry(Frame2_1, width="5",)
n.place(x="110",y="30")

yt=Label(Frame2_1,text="y=",font="Verdana 9 bold", fg="white", bg="#282923",justify="left")
yt.place(x="80",y="55")
y=tk.Entry(Frame2_1, width="5",)
y.place(x="110",y="55")

gt=Label(Frame2_1,text="g=",font="Verdana 9 bold", fg="white", bg="#282923",justify="left")
gt.place(x="80",y="80")
g=tk.Entry(Frame2_1, width="5",)
g.place(x="110",y="80")

vt=Label(Frame2_1,text="v=",font="Verdana 9 bold", fg="white", bg="#282923",justify="left")
vt.place(x="155",y="5")
v=tk.Entry(Frame2_1, width="5",)
v.place(x="195",y="5")

at=Label(Frame2_1,text="α/2=",font="Verdana 9 bold", fg="white", bg="#282923",justify="left")
at.place(x="155",y="30")
a=tk.Entry(Frame2_1, width="5",)
a.place(x="195",y="30")

tt=Label(Frame2_1,text="T=",font="Verdana 9 bold", fg="white", bg="#282923",justify="left")
tt.place(x="155",y="55")
t=tk.Entry(Frame2_1, width="5",)
t.place(x="195",y="55")

let=Label(Frame2_1,text="L e=",font="Verdana 9 bold", fg="white", bg="#282923",justify="left")
let.place(x="155",y="80")
le=tk.Entry(Frame2_1, width="5",)
le.place(x="195",y="80")


lhtt=Label(Frame2_1,text="Lth=",font="Verdana 9 bold", fg="white", bg="#282923",justify="left")
lhtt.place(x="240",y="5")
lht=tk.Entry(Frame2_1, width="5",)
lht.place(x="350",y="5")

cit=Label(Frame2_1,text="Cota Inicial=",font="Verdana 9 bold", fg="white", bg="#282923",justify="left")
cit.place(x="240",y="30")
ci=tk.Entry(Frame2_1, width="5",)
ci.place(x="350",y="30")

cft=Label(Frame2_1,text="Cota Final=",font="Verdana 9 bold", fg="white", bg="#282923",justify="left")
cft.place(x="240",y="55")
cf=tk.Entry(Frame2_1, width="5",)
cf.place(x="350",y="55")

btn5=Button(Frame2_1,text="Leyendo", width="14",height="2", cursor="hand2",fg="white",bg="#282923", command=leyenda) 
btn5.place(x="400", y="25")

# # ------------------------------------------------------------------------------
# #  Frame 2_2
# # ------------------------------------------------------------------------------

Frame2_2=Frame(Frame2,width=370, height=180 )
# Frame2.pack()
Frame2_2.config(bd=4,relief="groove", bg="#282923")
Frame2_2.place(x="160",y="200")

text=Label(Frame2_2,text="Resultados:",font="Verdana 9 bold", fg="white", bg="#282923")
text.place(x="10",y="10")


zt=Label(Frame2_2,text="Z=",font="Verdana 9 bold", fg="white", bg="#282923",justify="left")
zt.place(x="10",y="30")

btn5=Button(Frame2,text="Procesar", width="15",height="2", cursor="hand2",fg="white",bg="#282923", command=procesar) 
btn5.place(x="25", y="200")

btn6=Button(Frame2,text="Guardar", width="15",height="2", cursor="hand2",fg="white",bg="#282923", command=abrir) 
btn6.place(x="25", y="250")

btn6=Button(Frame2,text="Limpiar", width="15",height="2", cursor="hand2",fg="white",bg="#282923", command=limpiar) 
btn6.place(x="25", y="300")

btn6=Button(Frame2,text="Ver Teoria", width="15",height="2", cursor="hand2",fg="white",bg="#282923", command=teoria) 
btn6.place(x="25", y="350")
# ------------------------------------------------------------------------------
#   Fin de App
# ------------------------------------------------------------------------------
app.mainloop()
