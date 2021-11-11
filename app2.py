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

from PIL import ImageTk,Image  
import pandas as pd  # generar archivos excel

import numpy as np # libreria de matrices 

import xlsxwriter  # escribir excels



import math #libreria para uso de funciones matematicas



import os  #permite acceder a las fucciones principales de la pc - navegar por archivos de pc
from shutil import copyfile #permite copiar y mover archivos en la pc

##############################################################
#----------------------Variables globales---------------------
##############################################################

##############################################################
#----------------------Funciones------------------------------
##############################################################

# La funcion guardar nos permite generar un excel donde se mostraran los resultados con las formulas

def guardar():
#----------------------variables globales------------------------------
    global a
    file_excel=asksaveasfile(defaultextension=".xlsx", initialfile="Resultados.xlsx", title="Guardar",)
  
    dic={}
    lista=[]

    for i in range(20):
        lista.append(i)
    diametro_2=round(pulgadas,0)
    angulo=float(a.get())
    l0=["","","","","","","","","","","","","","",""]
    l1=["","","Parte I:","","","","","","","","","","","",""]
    l2=["","","DIÁMETRO DE TUBO","","DIAMETRO DE TUBO","","Area=","Diámetro=","","LONG. DE TRANSICION","","T1=","T2=","Lt1=","Lt2="]
    l3=["","","Y LONG. DE  ","","","",f"{area} m2",f"{diametro} m","","","",T1,T2,LT,LT2]
    l4=["","","TRANSICIÓN","","","","",f"» {pulgadas} plg ≈ {diametro_2} plg","","","","» b+(2yz)","Diametro (m)","Ang°","4*Diametro"]

    l5=["------------------------------------","","Parte II:","","","","","","","",""]
    l6=["------------------------------------","","COTAS","","NIVEL DE AGUA","","Cota de fondo 1=","Nivel Agua 1=","","COTA DE FONDO 2",""]
    l7=["------------------------------------","","","","","",f" {cota_fondo_1} m.s.n.m",f" {nivel_agua_1} m.s.n.m","","", ""]
    l8=["------------------------------------","","","","","","» Cota inicial-(Long e*Escala)","» Cota1 + y","","",""]


    l9=["","","","","","","",""]
    l10=["v1=","vt=","hte=","1.5Hv(1)=","1.5Hv(2)=","1.5Hv=","Hv=","Cota de fondo 2="]
    l11=[v1,vt,hte,hv1,hv2,hv15,hv,f" {cota_fondo_2} m.s.n.m"]
    l12=["» Q/((T2^2)*Pi/4)","» (y*z+b)*y/2","» T2/cos(Angº)","» (v1^2)/(2*g)","» (vt^2)/(2*g)","» 1.5Hv(1) - 1.5Hv(2)","» 1.5Hv * 1.5","» Nivel Agua 1 -(Hte + Hv)"]

    l13=["","","","","","","","","","","","","","","",""]
    l14=["","COTA DE FONDO 3","","h=","Cota de fondo 3=","","COTA DE FONDO 4","","h4=","Cota de fondo 4=","","COTA DE FONDO 5","","h=","Cota de fondo 5=",""]
    l15=["","","",h,f" {cota_fondo_3} m.s.n.m","","","",h4,f" {cota_fondo_4} m.s.n.m","","","",h5, f" {cota_fondo_5} m.s.n.m",""]
    l16=["","","","» Angº *5","» Cota2 - h","","","","» Lth* Escala","» Cota3 - h4","","","","» Angº *4","» Cota4 + h",""]

    l17=["------------------------------------","","Parte III:","","","","","","","","","","","","",""]
    l18=["------------------------------------","","VALOR P,","","VALOR P","","P de entrada=","P de salida=","Valor P=","","INCLINACION DE LOS","","Entrada x=","Entrada y=","Inclinacion=","","Salida x="]
    l19=["------------------------------------","","CARGA HIDRÁULICA","","","",p_entrada,p_salida,p,"","TUBOS DOBLADOS","",x_entrada,y_entrada,inclinacion_entrada,"",x_salida]
    l20=["------------------------------------","","Y PERDIDAS DE CARGA","","","","» 3/4 T2","» 1/2 T2","» Cota Final - Cota5","","","","» h(cota3)/Tang(Angº)","» h(cota3)","» Entrada x/Entrada Y","","» h(cota5)/Tang(Angº)"]


    l21=["","","","","","","","","","","","","","","","","",""]
    l22=["Salida y=","Inclinacion=","","CARGA HIDRÁULICA","","Cota 1 + tirante=","Cota 6 + tirante=","Carga disponible=","","CALCULO DE","","Entrada=","Salida=","Friccion=","Codos=","PERDIDA TOTAL=","10% Seguridad="]
    l23=[y_salida,inclinacion_salida,"","DISPONIBLE","",f" {c1_t} m.s.n.m",f" {c6_t} m.s.n.m",f" {carga} m","","LAS PERDIDAS","",entrada,salida,friccion,codos,perdida,porcentaje]
    l24=["» h(cota5)","» Salida x/Salida Y","","","","» Cota1 +y","» Cota Final +y (2)","» (1)-(2)","","DE CARGA","","» P entrada *0.0938","» P Salida *0.0938","» 0.025*(longitud/Diametro)*1.5Hv(1)","» 2*(0.25*(Angº^(1/2))/(90º *1.5Hv(1))","»Entrada+Salida+Friccion+Codo","» Perdida*(1+10%)"]

    l25=["","","","","","",""]
    l26=["","∆ Cota 1 y Cota 2=","Altura de sumergencia=","","LONGITUD DE","","Lp="]
    l27=["",cotas,altura,"","PROTECCION CON","",longitud]
    l28=["","» Cota1-Cota2","»y+(∆c1 y c2)-hte","","ENRROCADO","","»3*T2"]
  
    dic['']=l1 + l5 +l9 +l13+l17+l21+l25
    dic['Diseño ']=l2+l6+l10+l14+l18+l22+l26

    dic['hidráulico ']=l3+l7+l11+l15+l19+l23+l27
    dic['del sifón']=l4+l8+l12+l16+l20+l24+l28
    df1=pd.DataFrame(dic)

    columnas=len(df1.columns)
    # aqui se genera el excel con el formato q le damos
    writer = pd.ExcelWriter(file_excel.name, engine='xlsxwriter')
    df1.to_excel(writer, sheet_name="Diseño de Sifon", index=False)

    workbook = writer.book

    worksheet = writer.sheets['Diseño de Sifon']

    header_format = workbook.add_format()
    a_format = workbook.add_format()
    b_format = workbook.add_format()
    a_format.set_align('center')
    a_format.set_align('vcenter')
    a_format.set_bg_color('#ffffff')

    header_format.set_bold()

    header_format.set_font_size(12)
    header_format.set_italic()
    header_format.set_align('center')
    header_format.set_align('vcenter')
    header_format.set_pattern(1)  
    header_format.set_bg_color('#ffffff')

    for i in range(columnas+1):
        worksheet.set_column(1, i, 25,a_format)
    for col_num, value in enumerate(df1.columns.values):

        worksheet.write(0, col_num, value, header_format)
    writer.close()
    pass



#----------------------Procesar------------------------------
#Esta funcion permite procesar los datos y dar resultados
def procesar():

    #variables globales-------------------------------
    try:
        global z
        global q
        global s
        global b
        global n
        global y
        global v
        global a

        global lht
        global ci
        global cf
        global le
        global ang
        global g
        
        #variables globales de salida-------------------------------
        global Frame2_2
        global area
        global diametro
        global T1
        global T2
        global LT
        global LT2

        global cota_fondo_1
        global nivel_agua_1
        global v1
        global vt
        global hte
        global hv1
        global hv2
        global hv15
        global hv
        global cota_fondo_2
        global h
        global h5
        global h4
        global cota_fondo_3
        global cota_fondo_4
        global cota_fondo_5

        global pulgadas
        global p_entrada
        global p_salida
        global p
        global x_salida
        global x_entrada
        global y_salida
        global y_entrada
        global entrada 
        global salida
        global friccion
        global codos
        global c1_t
        global c6_t
        global inclinacion_entrada
        global inclinacion_salida
        global carga
        global perdida
        global porcentaje
        global cotas
        global altura
        global longitud


        ang=float(ang.get())
        area=round(float(q.get())/float(v.get()),2)
        #print("Area:",area)
        diametro=round(math.sqrt(area*4/math.pi),2)
        #print("Daimetro:",diametro)
        pulgadas=round(diametro/0.0254,2)
        #print("pulgadas:",pulgadas)
        T1=round(float(b.get())+(float(y.get())*float(z.get())*2),1)
        #print("T1:",T1)
        T2=round(round(pulgadas,0)*0.0254,4)
        #print("T2:",T2)
        LT=round((T1-T2)/(2*math.tan(math.radians(float(a.get())))),2)
        #print("LT:",LT)
        LT2=round(4*T2,1)
        #print("LT2:",LT2)
        cota_fondo_1=round(float(ci.get())-(0.001*float(le.get())),3)
        #print("cota_fondo_1:",cota_fondo_1)
        nivel_agua_1=round(cota_fondo_1+float(y.get()),3)
        #print("nivel_agua_1:",nivel_agua_1)
        v1=float(q.get())/((T2**2)*math.pi/4)
        #print("v1:",v1)
        vt=round((float(y.get()) *float(z.get())+float(b.get()))*float(y.get())/2,4)
        #print("vt:",vt)
        hte=(round(pulgadas,0)*0.0254)/math.cos(math.radians(ang))
        #print("hte:",hte)
        hv1=(v1**2)/(2*float(g.get()) )
        #print("hv1:",hv1)
        hv2=(vt**2)/(2*float(g.get()) )
        #print("hv2:",hv2)
        hv15=hv1-hv2
        #print("1.5hv:",hv)
        hv=hv15*1.5
        #print("hv:",hv)
        cota_fondo_2=round(nivel_agua_1-(hte+hv),3)
        #print("cota_fondo_2:",cota_fondo_2)
        h=math.radians(ang)*5
        cota_fondo_3=round(cota_fondo_2-math.radians(ang)*5,3)
        #print("cota_fondo_3:",cota_fondo_3)
        h4=0.05
        # h4=float(lht.get())*5/1000
        #print(h4)
        cota_fondo_4=round(cota_fondo_3-h4,3)
        #print("cota_fondo_4:",cota_fondo_4)
        h5=math.radians(ang)*4
        cota_fondo_5=round((math.radians(ang)*4)+cota_fondo_4,3)
        #print("cota_fondo_5:",cota_fondo_5)
        p_entrada=round((3/4)*(round(pulgadas,0)*0.0254),4)
        #print("p_entrada:",p_entrada)
        p_salida=round((1/2)*(round(pulgadas,0)*0.0254),4)
        #print("p_salida:",p_salida)
        p=round(float(cf.get())-cota_fondo_5,3)
        #print("p:",p)
        x_entrada=round((math.radians(ang)*5)/(math.tan(math.radians(float(ang)))),3)
        #print("x_entrada:",x_entrada)
        y_entrada=round(math.radians(ang)*5,3)
        #print("y_entrada:",y_entrada)
        inclinacion_entrada=round(x_entrada/y_entrada,3)
        #print("inclinacion_entrada:",inclinacion_entrada)
        x_salida=round((math.radians(ang)*4)/(math.tan(math.radians(float(ang)))),3)
        #print("x_salida:",x_salida)
        y_salida=round(math.radians(ang)*4,3)
        #print("y_salida:",y_salida)
        inclinacion_salida =round(x_salida/y_salida,3) 
        #print("inclinacion_salida:",inclinacion_salida)
        c1_t=round(cota_fondo_1+float(y.get()),3)
        #print("cota1+tirante:",c1_t)
        c6_t=round(float(cf.get())+float(y.get()),3)
        #print("cota6+tirante:",c6_t)
        carga=round(c1_t-c6_t,3)
        #print("carga dispoible:",carga)
        entrada=round(p_salida*0.0938,4)
        #print("entrada:",entrada)
        salida=round(p_entrada*0.0938,4)
        #print("salida:",salida)
        # dato=(float(y.get())**2)/(2*float(g.get()))
        friccion=(19/diametro)*hv1*0.025
        #print(friccion)
        codos=2*(0.25*math.sqrt(math.radians(float(ang))/math.radians(90))*(hv1))
        #print(codos)
        perdida=round(entrada+salida+codos+friccion,2)
        #print("perdida total:",perdida)
        porcentaje=round(perdida*(1+0.1),2)
        #print("porcentaje:",porcentaje)
        cotas=round(cota_fondo_1- cota_fondo_2,3)
        #print("∆ Cota 1 y Cota 2:",cotas)
        altura=round(float(y.get())+cotas- hte,3)
        #print("alturas de sumergencia:",altura)
        longitud=round(3*(pulgadas*0.0254),1)
        #print(" Longitud de proteccion :",longitud)


        #muestra la data generando nuevos recuadros de vistas

        Frame2_2=Frame(Frame2,width=370, height=180 )
        
        Frame2_2.config(bd=4,relief="groove")
        Frame2_2.place(x="160",y="210")
        label_area=Label(Frame2_2,text="DIAMETRO DE TUBO Y LONG. DE TRANSICION",font="Verdana 9 bold",justify="left")
        label_area.place(x="20",y="0")

        label_info=Label(Frame2_2,text=f"Area= {area} m2",font="Verdana 9 bold",justify="left")
        label_info.place(x="10",y="50")
        label_info=Label(Frame2_2,text=f"Diametro= {diametro} plg",font="Verdana 9 bold",justify="left")
        label_info.place(x="10",y="75")
        label_info=Label(Frame2_2,text=f"T1= {T1} ",font="Verdana 9 bold",justify="left")
        label_info.place(x="200",y="50")
        label_info=Label(Frame2_2,text=f"T2= {T2} ",font="Verdana 9 bold",justify="left")
        label_info.place(x="200",y="75")
        label_info=Label(Frame2_2,text=f"Lt1= {LT} ",font="Verdana 9 bold",justify="left")
        label_info.place(x="200",y="100")
        label_info=Label(Frame2_2,text=f"Lt2= {LT2} ",font="Verdana 9 bold",justify="left")
        label_info.place(x="200",y="125")
    except:
        messagebox.showerror(message="Error Campos vacios o con texto, porfavor llene los campos correctamente", title="Error al Procesar")
        global Frame2_1
        try:
       
            Frame2_2.destroy()
        except:
            pass
        Frame2_1.destroy()
        Frame2_1=Frame(Frame2,width=520, height=130)
        # Frame2.pack()
        Frame2_1.config(bd=4,relief="groove")
        Frame2_1.place(x="10",y="30")



        zt=Label(Frame2_1,text="Z=",font="Verdana 9 bold",justify="left")
        zt.place(x="10",y="10")
        z=tk.Entry(Frame2_1, width="5",)
        z.place(x="50",y="10")

        qt=Label(Frame2_1,text="Q=",font="Verdana 9 bold",justify="left")
        qt.place(x="10",y="35")
        q=tk.Entry(Frame2_1, width="5",)
        q.place(x="50",y="35")

        st=Label(Frame2_1,text="S=",font="Verdana 9 bold",justify="left")
        st.place(x="10",y="60")
        s=tk.Entry(Frame2_1, width="5",)
        s.place(x="50",y="60")

        angt=Label(Frame2_1,text="Angº=",font="Verdana 9 bold",justify="left")
        angt.place(x="0",y="85")
        ang=tk.Entry(Frame2_1, width="5",)
        ang.place(x="50",y="85")




        bt=Label(Frame2_1,text="b=",font="Verdana 9 bold",justify="left")
        bt.place(x="110",y="10")
        b=tk.Entry(Frame2_1, width="5",)
        b.place(x="160",y="10")

        nt=Label(Frame2_1,text="n=",font="Verdana 9 bold",justify="left")
        nt.place(x="110",y="35")
        n=tk.Entry(Frame2_1, width="5",)
        n.place(x="160",y="35")

        yt=Label(Frame2_1,text="y=",font="Verdana 9 bold",justify="left")
        yt.place(x="110",y="60")
        y=tk.Entry(Frame2_1, width="5",)
        y.place(x="160",y="60")

        gt=Label(Frame2_1,text="g=",font="Verdana 9 bold",justify="left")
        gt.place(x="110",y="85")
        g=tk.Entry(Frame2_1, width="5",)
        g.place(x="160",y="85")




        vt=Label(Frame2_1,text="v=",font="Verdana 9 bold",justify="left")
        vt.place(x="210",y="10")
        v=tk.Entry(Frame2_1, width="5",)
        v.place(x="270",y="10")

        at=Label(Frame2_1,text="α/2=",font="Verdana 9 bold",justify="left")
        at.place(x="210",y="35")
        a=tk.Entry(Frame2_1, width="5",)
        a.place(x="270",y="35")

        let=Label(Frame2_1,text="Long e=",font="Verdana 9 bold",justify="left")
        let.place(x="210",y="85")
        le=tk.Entry(Frame2_1, width="5",)
        le.place(x="270",y="85")




        lhtt=Label(Frame2_1,text="Lth=",font="Verdana 9 bold",justify="left")
        lhtt.place(x="350",y="10")
        lht=tk.Entry(Frame2_1, width="5",)
        lht.place(x="470",y="10")

        cit=Label(Frame2_1,text="Cota Inicial=",font="Verdana 9 bold",justify="left")
        cit.place(x="350",y="35")
        ci=tk.Entry(Frame2_1, width="5",)
        ci.place(x="470",y="35")

        cft=Label(Frame2_1,text="Cota Final=",font="Verdana 9 bold",justify="left")
        cft.place(x="350",y="60")
        cf=tk.Entry(Frame2_1, width="5",)
        cf.place(x="470",y="60")
        btn5=Button(Frame2_1,text="Leyendo", width="14",height="1", cursor="hand2", command=leyenda) 
        btn5.place(x="380", y="90")

    pass


#----------------------Teoria------------------------------
#Esta funcion permite descargar la teoria

def teoria():
    try:
        file_pdf=asksaveasfile(defaultextension=".pdf", initialfile="teoria.pdf", title="Guardar",)
        # #print(file_pdf.name)
        archivo=str(os.getcwd())+"\\"+"teoria.pdf"

        # #print(os.getcwd()+"\\"+"teoria.pdf")
        copyfile(archivo, file_pdf.name)
        pass
    except:
        pass

    



#----------------------Acerca------------------------------
#Esta funcion permite mirar la informacion del creador

def acerca():
  

    acerca =tk.Tk()

    acerca.title("Acerca de ...") # titulo
    acerca.geometry("460x400") # geometria inicial
    acerca.resizable(0, 0) # no e sposible  agrandar
    acerca.iconbitmap("icon.ico")

    texto=Label(acerca,text="GRUPO CAELUM",font="Verdana 14 bold")
    texto.place(x="20", y="25")
    texto=Label(acerca,text="Integrantes:",font="Verdana 10 bold")
    texto.place(x="20", y="100")

    pass


#----------------------Salir------------------------------
#Esta funcion permite cerrar la app

def salir():
    app.destroy()
    pass

#----------------------Limpiar------------------------------
#Esta funcion limpia todo lo realizado

def limpiar():
    global Frame2_1

    #variables globales --------------------------------------
    try:
        global Frame2_2
        Frame2_2.destroy()

    except:
        pass
    Frame2_1.destroy()  
    Frame2_1=Frame(Frame2,width=520, height=130)
    # Frame2.pack()
    Frame2_1.config(bd=4,relief="groove")
    Frame2_1.place(x="10",y="30")



    zt=Label(Frame2_1,text="Z=",font="Verdana 9 bold",justify="left")
    zt.place(x="10",y="10")
    z=tk.Entry(Frame2_1, width="5",)
    z.place(x="50",y="10")

    qt=Label(Frame2_1,text="Q=",font="Verdana 9 bold",justify="left")
    qt.place(x="10",y="35")
    q=tk.Entry(Frame2_1, width="5",)
    q.place(x="50",y="35")

    st=Label(Frame2_1,text="S=",font="Verdana 9 bold",justify="left")
    st.place(x="10",y="60")
    s=tk.Entry(Frame2_1, width="5",)
    s.place(x="50",y="60")

    angt=Label(Frame2_1,text="Angº=",font="Verdana 9 bold",justify="left")
    angt.place(x="0",y="85")
    ang=tk.Entry(Frame2_1, width="5",)
    ang.place(x="50",y="85")




    bt=Label(Frame2_1,text="b=",font="Verdana 9 bold",justify="left")
    bt.place(x="110",y="10")
    b=tk.Entry(Frame2_1, width="5",)
    b.place(x="160",y="10")

    nt=Label(Frame2_1,text="n=",font="Verdana 9 bold",justify="left")
    nt.place(x="110",y="35")
    n=tk.Entry(Frame2_1, width="5",)
    n.place(x="160",y="35")

    yt=Label(Frame2_1,text="y=",font="Verdana 9 bold",justify="left")
    yt.place(x="110",y="60")
    y=tk.Entry(Frame2_1, width="5",)
    y.place(x="160",y="60")

    gt=Label(Frame2_1,text="g=",font="Verdana 9 bold",justify="left")
    gt.place(x="110",y="85")
    g=tk.Entry(Frame2_1, width="5",)
    g.place(x="160",y="85")




    vt=Label(Frame2_1,text="v=",font="Verdana 9 bold",justify="left")
    vt.place(x="210",y="10")
    v=tk.Entry(Frame2_1, width="5",)
    v.place(x="270",y="10")

    at=Label(Frame2_1,text="α/2=",font="Verdana 9 bold",justify="left")
    at.place(x="210",y="35")
    a=tk.Entry(Frame2_1, width="5",)
    a.place(x="270",y="35")


    let=Label(Frame2_1,text="Long e=",font="Verdana 9 bold",justify="left")
    let.place(x="210",y="85")
    le=tk.Entry(Frame2_1, width="5",)
    le.place(x="270",y="85")




    lhtt=Label(Frame2_1,text="Lth=",font="Verdana 9 bold",justify="left")
    lhtt.place(x="350",y="10")
    lht=tk.Entry(Frame2_1, width="5",)
    lht.place(x="470",y="10")

    cit=Label(Frame2_1,text="Cota Inicial=",font="Verdana 9 bold",justify="left")
    cit.place(x="350",y="35")
    ci=tk.Entry(Frame2_1, width="5",)
    ci.place(x="470",y="35")

    cft=Label(Frame2_1,text="Cota Final=",font="Verdana 9 bold",justify="left")
    cft.place(x="350",y="60")
    cf=tk.Entry(Frame2_1, width="5",)
    cf.place(x="470",y="60")
    btn5=Button(Frame2_1,text="Leyendo", width="14",height="1", cursor="hand2", command=leyenda) 
    btn5.place(x="380", y="90")
    pass


#esta funcion nos permite ver la informacion de los datos q estamos ingresando
def leyenda():

    #variables globales --------------------------------------
    global logo
    leyenda = Tk()

    leyenda.title("Leyenda") # titulo
    leyenda.geometry("290x400") # geometria inicial
    leyenda.resizable(0, 0) # no e sposible  agrandar
    leyenda.iconbitmap("icon.ico")

    texto=Label(leyenda,text="Leyenda",font="Verdana 14 bold")
    texto.place(x="100", y="15")

    texto=Label(leyenda,text="Z=talud",font="Verdana 10 bold").place(x="20", y="50")
    texto=Label(leyenda,text="Q=caudal",font="Verdana 10 bold").place(x="20", y="75")
    texto=Label(leyenda,text="S=pendiente",font="Verdana 10 bold").place(x="20", y="100")
    texto=Label(leyenda,text="b=base",font="Verdana 10 bold").place(x="20", y="125")
    texto=Label(leyenda,text="n=numero de froude",font="Verdana 10 bold").place(x="20", y="150")
    texto=Label(leyenda,text="Y=tirante",font="Verdana 10 bold").place(x="20", y="175")
    texto=Label(leyenda,text="V=velocidad",font="Verdana 10 bold").place(x="20", y="200")
    texto=Label(leyenda,text="α/2=angulo lt",font="Verdana 10 bold").place(x="20", y="225")
    texto=Label(leyenda,text="T=espejo de agua",font="Verdana 10 bold").place(x="20", y="250")
    texto=Label(leyenda,text="Lth=Longitud de tubo horizontal",font="Verdana 10 bold").place(x="20", y="275")
    texto=Label(leyenda,text="Ang=Angulo",font="Verdana 10 bold").place(x="20", y="300")
    texto=Label(leyenda,text="g=gravedad",font="Verdana 10 bold").place(x="20", y="325")

    
    
    pass
#Esta funcion nos permite cambiar la vista de los resultados

def parte1():
    try:
    #variables globales --------------------------------------
        global Frame2_2 
        global Frame2

        Frame2_2.destroy()
        Frame2_2=Frame(Frame2,width=370, height=180 )
        # Frame2.pack()
        Frame2_2.config(bd=4,relief="groove")
        Frame2_2.place(x="160",y="210")
        label_area=Label(Frame2_2,text="DIAMETRO DE TUBO Y LONG. DE TRANSICION",font="Verdana 9 bold",justify="left")
        label_area.place(x="20",y="0")

        label_info=Label(Frame2_2,text=f"Area= {area} m2",font="Verdana 9 bold",justify="left")
        label_info.place(x="10",y="50")
        label_info=Label(Frame2_2,text=f"Diametro= {diametro} plg",font="Verdana 9 bold",justify="left")
        label_info.place(x="10",y="75")
        label_info=Label(Frame2_2,text=f"T1= {T1} ",font="Verdana 9 bold",justify="left")
        label_info.place(x="200",y="50")
        label_info=Label(Frame2_2,text=f"T2= {T2} ",font="Verdana 9 bold",justify="left")
        label_info.place(x="200",y="75")
        label_info=Label(Frame2_2,text=f"Lt1= {LT} ",font="Verdana 9 bold",justify="left")
        label_info.place(x="200",y="100")
        label_info=Label(Frame2_2,text=f"Lt2= {LT2} ",font="Verdana 9 bold",justify="left")
        label_info.place(x="200",y="125")
        pass   
    except:   
        pass
#Esta funcion nos permite cambiar la vista de los resultados

def parte2():
    try:
    #variables globales --------------------------------------
        global Frame2_2 
        global Frame2 
        Frame2_2.destroy()
        Frame2_2=Frame(Frame2,width=370, height=180 )
    
        Frame2_2.config(bd=4,relief="groove")
        Frame2_2.place(x="160",y="210")
        label_area=Label(Frame2_2,text="COTAS",font="Verdana 9 bold",justify="left")
        label_area.place(x="150",y="0")

        label_info=Label(Frame2_2,text=f"Nivel Agua= {nivel_agua_1} m.s.n.m",font="Verdana 9 bold",justify="left")
        label_info.place(x="10",y="25")
        label_info=Label(Frame2_2,text=f"Cota de fondo 1= {cota_fondo_1} m.s.n.m",font="Verdana 9 bold",justify="left")
        label_info.place(x="10",y="50")
        label_info=Label(Frame2_2,text=f"Cota de fondo 2= {cota_fondo_2} m.s.n.m",font="Verdana 9 bold",justify="left")
        label_info.place(x="10",y="75")
        label_info=Label(Frame2_2,text=f"Cota de fondo 3= {cota_fondo_3} m.s.n.m",font="Verdana 9 bold",justify="left")
        label_info.place(x="10",y="100")
        label_info=Label(Frame2_2,text=f"Cota de fondo 4= {cota_fondo_4} m.s.n.m",font="Verdana 9 bold",justify="left")
        label_info.place(x="10",y="125")
        label_info=Label(Frame2_2,text=f"Cota de fondo 5= {cota_fondo_5} m.s.n.m",font="Verdana 9 bold",justify="left")
        label_info.place(x="10",y="150")
        pass   
    except:   
        pass
#Esta funcion nos permite cambiar la vista de los resultados

def parte3():
    try:
    #variables globales --------------------------------------
        global Frame2_2 
        global Frame2
        Frame2_2.destroy()
        Frame2_2=Frame(Frame2,width=370, height=180 )

        Frame2_2.config(bd=4,relief="groove")
        Frame2_2.place(x="160",y="210")
        label_area=Label(Frame2_2,text="VALOR P, CARGA HIDRAULICA Y PERDIDAS DE CARGA",font="Verdana 8 bold",justify="left")
        label_area.place(x="5",y="0")

        label_info=Label(Frame2_2,text=f"P de entrada= {p_entrada}",font="Verdana 7 bold",justify="left")
        label_info.place(x="10",y="25")
        label_info=Label(Frame2_2,text=f"P de salida= {p_salida}",font="Verdana 7 bold",justify="left")
        label_info.place(x="10",y="50")
        label_info=Label(Frame2_2,text=f"P= {p}",font="Verdana 7 bold",justify="left")
        label_info.place(x="10",y="75")
        label_info=Label(Frame2_2,text=f"Inclinacion entrada= {inclinacion_entrada}",font="Verdana 7 bold",justify="left")
        label_info.place(x="10",y="100")
        label_info=Label(Frame2_2,text=f"Inclinacion salida= {inclinacion_salida}",font="Verdana 7 bold",justify="left")
        label_info.place(x="10",y="125")
        label_info=Label(Frame2_2,text=f"carga= {carga} m.",font="Verdana 7 bold",justify="left")
        label_info.place(x="10",y="150")

        label_info=Label(Frame2_2,text=f"Perdida= {perdida}",font="Verdana 7 bold",justify="left")
        label_info.place(x="200",y="25")
        label_info=Label(Frame2_2,text=f"% Seguridad= {porcentaje}",font="Verdana 7 bold",justify="left")
        label_info.place(x="200",y="50")
        label_info=Label(Frame2_2,text=f"∆ C.1 y C.2= {cotas}",font="Verdana 7 bold",justify="left")
        label_info.place(x="200",y="75")
        label_info=Label(Frame2_2,text=f"Alt.sumergencia= {altura}",font="Verdana 7 bold",justify="left")
        label_info.place(x="200",y="125")
        label_info=Label(Frame2_2,text=f"Lng.proteccion= {longitud}",font="Verdana 7 bold",justify="left")
        label_info.place(x="200",y="150")

        pass   
    except:   
        pass
#Esta funcion nos Permite tener la vista principal para ingresar los datos

def aplicacion():
    global z
    global q
    global s
    global b
    global n
    global y
    global v
    global a

    global lht
    global g
    global ci
    global cf
    global le
    global ang
    global Frame2
    global logo
    global Frame2_1
    global app

    root.destroy()
    app = Tk() # Creamos la App
    app.title("App") # titulo
    app.geometry("570x500") # geometria inicial
    app.resizable(0, 0) # no e sposible  agrandar
    app.iconbitmap("icon.ico")

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



    # # ------------------------------------------------------------------------------
    # #   Descripcion - Titulo
    # # ------------------------------------------------------------------------------

    texto=Label(app,text="Diseño Hidráulico De Sifón Invertido",font="Verdana 15 bold")
    texto.place(x="20", y="15")



    # # ------------------------------------------------------------------------------
    # #  Frame 2
    # # ------------------------------------------------------------------------------

    Frame2=Frame(width=550, height=410)

    Frame2.config(bd=4,relief="groove")
    Frame2.place(x="10",y="60")

    text2=Label(Frame2,text="Ingresar Datos ",font="Verdana 10 bold")
    text2.place(x="15",y="0")

    # # ------------------------------------------------------------------------------
    # #  Frame 2_1
    # # ------------------------------------------------------------------------------

    Frame2_1=Frame(Frame2,width=520, height=130)
    # Frame2.pack()
    Frame2_1.config(bd=4,relief="groove")
    Frame2_1.place(x="10",y="30")



    zt=Label(Frame2_1,text="Z=",font="Verdana 9 bold",justify="left")
    zt.place(x="10",y="10")
    z=tk.Entry(Frame2_1, width="5",)
    z.place(x="50",y="10")

    qt=Label(Frame2_1,text="Q=",font="Verdana 9 bold",justify="left")
    qt.place(x="10",y="35")
    q=tk.Entry(Frame2_1, width="5",)
    q.place(x="50",y="35")

    st=Label(Frame2_1,text="S=",font="Verdana 9 bold",justify="left")
    st.place(x="10",y="60")
    s=tk.Entry(Frame2_1, width="5",)
    s.place(x="50",y="60")

    angt=Label(Frame2_1,text="Angº=",font="Verdana 9 bold",justify="left")
    angt.place(x="0",y="85")
    ang=tk.Entry(Frame2_1, width="5",)
    ang.place(x="50",y="85")




    bt=Label(Frame2_1,text="b=",font="Verdana 9 bold",justify="left")
    bt.place(x="110",y="10")
    b=tk.Entry(Frame2_1, width="5",)
    b.place(x="160",y="10")

    nt=Label(Frame2_1,text="n=",font="Verdana 9 bold",justify="left")
    nt.place(x="110",y="35")
    n=tk.Entry(Frame2_1, width="5",)
    n.place(x="160",y="35")

    yt=Label(Frame2_1,text="y=",font="Verdana 9 bold",justify="left")
    yt.place(x="110",y="60")
    y=tk.Entry(Frame2_1, width="5",)
    y.place(x="160",y="60")

    gt=Label(Frame2_1,text="g=",font="Verdana 9 bold",justify="left")
    gt.place(x="110",y="85")
    g=tk.Entry(Frame2_1, width="5",)
    g.place(x="160",y="85")




    vt=Label(Frame2_1,text="v=",font="Verdana 9 bold",justify="left")
    vt.place(x="210",y="10")
    v=tk.Entry(Frame2_1, width="5",)
    v.place(x="270",y="10")

    at=Label(Frame2_1,text="α/2=",font="Verdana 9 bold",justify="left")
    at.place(x="210",y="35")
    a=tk.Entry(Frame2_1, width="5",)
    a.place(x="270",y="35")


    let=Label(Frame2_1,text="Long e=",font="Verdana 9 bold",justify="left")
    let.place(x="210",y="85")
    le=tk.Entry(Frame2_1, width="5",)
    le.place(x="270",y="85")




    lhtt=Label(Frame2_1,text="Lth=",font="Verdana 9 bold",justify="left")
    lhtt.place(x="350",y="10")
    lht=tk.Entry(Frame2_1, width="5",)
    lht.place(x="470",y="10")

    cit=Label(Frame2_1,text="Cota Inicial=",font="Verdana 9 bold",justify="left")
    cit.place(x="350",y="35")
    ci=tk.Entry(Frame2_1, width="5",)
    ci.place(x="470",y="35")

    cft=Label(Frame2_1,text="Cota Final=",font="Verdana 9 bold",justify="left")
    cft.place(x="350",y="60")
    cf=tk.Entry(Frame2_1, width="5",)
    cf.place(x="470",y="60")

    btn5=Button(Frame2_1,text="Leyendo", width="14",height="1", cursor="hand2", command=leyenda) 
    btn5.place(x="380", y="90")

    # # ------------------------------------------------------------------------------
    # #  Frame 2_2
    # # ------------------------------------------------------------------------------



    text=Label(app,text="Resultados:",font="Verdana 9 bold")
    text.place(x="190",y="240")
    btn5=Button(app,text="Parte 1", width="10",height="1", cursor="hand2", command=parte1) 
    btn5.place(x="280", y="240")
    btn6=Button(app,text="Parte 2", width="10",height="1", cursor="hand2", command=parte2) 
    btn6.place(x="370", y="240")
    btn7=Button(app,text="Parte 3", width="10",height="1", cursor="hand2", command=parte3) 
    btn7.place(x="460", y="240")



    btn5=Button(Frame2,text="Procesar", width="15",height="2", cursor="hand2", command=procesar) 
    btn5.place(x="25", y="170")

    btn6=Button(Frame2,text="Guardar", width="15",height="2", cursor="hand2", command=guardar) 
    btn6.place(x="25", y="230")

    btn6=Button(Frame2,text="Limpiar", width="15",height="2", cursor="hand2", command=limpiar) 
    btn6.place(x="25", y="290")

    btn6=Button(Frame2,text="Ver Teoria", width="15",height="2", cursor="hand2", command=teoria) 
    btn6.place(x="25", y="350")
    pass



##############################################################
#----------------------INICIO de la APP-----------------------
##############################################################


# declaramos propiedades de la pagina principal
root = Tk() # Creamos la App
root.title("App Sifon") # titulo
root.geometry("700x500") # geometria inicial
root.resizable(0, 0) # no es sposible  agrandar
root.iconbitmap("icon.ico") #icono de la app

# ---------------------------------------------------------------
#                   Carga de Imagenes
# ---------------------------------------------------------------

img_pag1 = tk.PhotoImage(file="img_1.png") 
# img_pag1= img_pag1.zoom(2, 2)  
# logo = ImageTk.PhotoImage(Image.open("logo.png")) 

# ---------------------------------------------------------------
#                   vista1
# ---------------------------------------------------------------
text2=Label(root,text="SIFÓN INVERTIDO",font="Verdana 24 bold")
text2.place(x="180",y="20")



imagen_central = tk.Label(root, image=img_pag1).place(x="150",y="100")

btn=Button(root,text="Teoria",font="Verdana 14 bold", width="15",height="2", cursor="hand2", command=teoria) 
btn.place(x="50", y="400")

btn2=Button(root,text="Diseña tu Sifón",font="Verdana 14 bold", width="15",height="2", cursor="hand2", command=aplicacion) 
btn2.place(x="450", y="400")
# ------------------------------------------------------------------------------
#   Fin de App
# ------------------------------------------------------------------------------
root.mainloop()
