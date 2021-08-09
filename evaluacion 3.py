from tkinter import *
from math import *

met=Tk()
met.title(' EVALUACIÓN ')
met.geometry('700x300')
met.config(bg='DarkSlateGray1')
input_text=StringVar()
operador=''
rts=StringVar()
c1=StringVar()
c2=StringVar()
ancho=8
ancho_label=4





#operaciones

def sumar():
    rts.set(float(c1.get())+float(c2.get()))
    borrar()
   

def menos():
    
    rts.set(float(c1.get())-float(c2.get()))
    borrar()

def multi():
    
    rts.set(float(c1.get())*float(c2.get()))
    borrar()

def dividir():
    
    rts.set(float(c1.get())/float(c2.get()))
    borrar()

def clear():
          rts.set('0')
          borrar()

def borrar():
    c1.set('  ')
    c2.set('  ')
       

#Calculo
    
def equal():
    global operador
    try:
        opera=str(eval(operador))
        input_text.set(opera)
    except:
        input_text.set('ERROR')
        operador=''






#recuadros
        
Entry(met,font=('Arial',18,'bold'),width=ancho,bd=2,bg='white',
      justify=CENTER,textvariable=c1,fg='red').place(x=50, y=50)

Entry(met,font=('Arial',18,'bold'),width=ancho,bd=1,bg='white',
      justify=CENTER,fg='red',textvariable=c2).place(x=200,y=50)

Entry(met,font=('Arial',18,'bold'),width=ancho,bd=1,bg='white',
      justify=CENTER,textvariable=rts,fg='red').place(x=450,y=50)

Label(met,font=('Arial',18,'bold'),width=ancho_label,text='=',
      bg='white',).place(x=360, y=60)


#Botones de operadores



Button(met, text='+',width=6,
       height=2,bg='goldenrod4',fg='White',command=sumar).place(x=50, y=150)

Button(met, text='-',width=6,
       height=2,bg='goldenrod4',fg='White',command=menos).place(x=120, y=150)

Button(met, text='*',width=6,
       height=2,bg='goldenrod4',fg='White',command=multi).place(x=200, y=150)

Button(met, text='/',width=6,
       height=2,bg='goldenrod4',fg='White',command=dividir).place(x=280, y=150)

Button(met, text='AC',width=6,
       height=2,bg='goldenrod4',fg='White',command=clear).place(x=454, y=150)       
















met.mainloop()
