from tkinter import*
import parser
import math
import tkinter.messagebox

root=Tk()
root.title("SCIENTIFIC CALCULATOR")
root.configure(background='powder blue')
root.resizable(width=False,height=False)
root.geometry("480x568+0+0")

Calc=Frame(root)
Calc.grid()


'''numberpad='789456123'
i=0
btn=[]
for j in range(2,5):
    for k in range(3):
        btn.append(Button(Calc,width=6,height=2,font('arial',20,'bold'),bd=4,text=numberpad[i]))
        btn[i].grid(row=j,column=k,pady=1)

        i+=1'''
#=============================MENU====================================

def iExit():
    iExit=tkinter.messagebox.askyesno("SCIENTIFIC CALCULATOR","Confirm if you want to exit")
    if iExit>0:
        root.destroy()
        return
def Standard():
    root.resizable(width=False,height=False)
    root.geometry("480x568+0+0")
def Scientific():
    root.resizable(width=False,height=False)
    root.geometry("987x568+0+0")
    
    




menubar=Menu(Calc)

filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Standard',command=Standard)
filemenu.add_command(label='Scientific',command=Scientific)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=iExit)

editmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='Cut')
editmenu.add_command(label='Copy')
editmenu.add_separator()
editmenu.add_command(label='Paste')

helpmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='View Help')
def btnclick(num):
    global operator
    operator=operator+str(num)
    text_Input.set(operator)

def btnclear():
    global operator
    operator=""
    text_Input.set("")

def equalsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""
def pi():
    global operator
    operator=math.pi
    text_Input.set(operator)
def tau():
    global operator
    operator=math.tau
    text_Input.set(operator)


def sin():
    global operator
    operator=math.sin
    text_Input.set(operator)
def cos():
    global operator
    operator=math.cos
    text_Input.set(operator)    
def tan():
    global operator
    operator=math.tan
    text_Input.set(operator)
def cot():
    global operator
    operator=math.cot
    text_Input.set(operator)    


    
    
operator=''
text_Input=StringVar()
text_display=Entry(Calc,font=('arial',20,'bold'),textvariable=text_Input,bd=30,width=28,bg='powder blue',justify='right').grid(row=0,column=0,columnspan=4,pady=1)
#text_display.insert(0,"0")
btn7=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="7",command=lambda:btnclick(7)).grid(row=1,column=0,pady=1)
btn8=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="8",command=lambda:btnclick(8)).grid(row=1,column=1,pady=1)
btn9=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="9",command=lambda:btnclick(9)).grid(row=1,column=2,pady=1)
add=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="+",command=lambda:btnclick("+")).grid(row=1,column=3,pady=1)
btn4=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="4",command=lambda:btnclick(4)).grid(row=2,column=0,pady=1)
btn5=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="5",command=lambda:btnclick(5)).grid(row=2,column=1,pady=1)
btn6=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="6",command=lambda:btnclick(6)).grid(row=2,column=2,pady=1)
sub=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="-",command=lambda:btnclick("-")).grid(row=2,column=3,pady=1)
btn1=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="1",command=lambda:btnclick(1)).grid(row=3,column=0,pady=1)
btn2=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="2",command=lambda:btnclick(2)).grid(row=3,column=1,pady=1)
btn3=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="3",command=lambda:btnclick(3)).grid(row=3,column=2,pady=1)
decimal=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text=".",command=lambda:btnclick(".")).grid(row=3,column=3,pady=1)
btn0=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="0",command=lambda:btnclick(0)).grid(row=4,column=0,pady=1)
mul=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="*",command=lambda:btnclick("*")).grid(row=4,column=1,pady=1)
devide=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="/",command=lambda:btnclick("/")).grid(row=4,column=2,pady=1)
btnEquals=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="=",command=equalsInput).grid(row=4,column=3,pady=1)
clear=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="C",command=btnclear).grid(row=5,column=0,pady=1)
btndot=Button(Calc,width=6,height=2,text='√',bd=4,fg="black",font=('arial',20,'bold'),command=btnclear).grid(row=5,column=1,pady=1)
btnPM=Button(Calc,width=6,height=2,text=chr(177),bd=4,fg="black",font=('arial',20,'bold'),command=btnclear).grid(row=5,column=2,pady=1)
btnlog10=Button(Calc,width=6,height=2,text='log10',bd=4,fg="black",font=('arial',20,'bold'),command=btnclear).grid(row=5,column=3,pady=1)
#btnsq=Button(Calc,text='√',padx=16,bd=8,fg="black",font=('arial',20,'bold'),command=btnclear).grid(row=5,column=1,pady=1)

#===========================================SCIENTIFIC CALCULATOR===========================================================================================================
btnPi=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text= "π",command=pi).grid(row=1,column=4,pady=1)
btncos=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="cos",command=cos).grid(row=1,column=5,pady=1)
btntan=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="tan",command=tan).grid(row=1,column=6,pady=1)
btnsin=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="sin",command=sin).grid(row=2,column=4,pady=1)

btn2Pi=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="2π",command=tau).grid(row=2,column=5,pady=1)
btncosh=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="cosh",command=lambda:btnclick()).grid(row=2,column=6,pady=1)
btntanh=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="tanh",command=lambda:btnclick(9)).grid(row=3,column=4,pady=1)
btnsinh=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="sinh",command=lambda:btnclick(4)).grid(row=3,column=5,pady=1)

btncot=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="cot",command=cot).grid(row=3,column=6,pady=1)
btnsec=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="sec",command=lambda:btnclick(6)).grid(row=4,column=4,pady=1)
btncosec=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="cosec",command=lambda:btnclick(1)).grid(row=4,column=5,pady=1)

btnlog=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text= "log",command=lambda:btnclick(pi)).grid(row=4,column=6,pady=1)
btnExp=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="Exp",command=lambda:btnclick()).grid(row=5,column=4,pady=1)
btnMod=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="Mod",command=lambda:btnclick(9)).grid(row=5,column=5,pady=1)
btnE=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="e",command=lambda:btnclick(4)).grid(row=5,column=6,pady=1)

btncosec=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="cosec",command=lambda:btnclick(1)).grid(row=1,column=7,pady=1)

btnexpm1=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text= "expm1",command=lambda:btnclick(pi)).grid(row=2,column=7,pady=1)
btnlgamma=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="lgamma",command=lambda:btnclick()).grid(row=3,column=7,pady=1)
btnacosh=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="acosh",command=lambda:btnclick(9)).grid(row=4,column=7,pady=1)
btnasinh=Button(Calc,width=6,height=2,bd=4,fg="black",font=('arial',20,'bold'),text="asinh",command=lambda:btnclick(4)).grid(row=5,column=7,pady=1)


lbldisplay=Label(Calc,text='SCIENTIFIC CALCULATOR',font=('arial',30,'bold'),justify=CENTER)
lbldisplay.grid(row=0,column=4,columnspan=24,pady=1)


'''btn2=Button(Calc,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text="2",command=lambda:btnclick(2)).grid(row=3,column=1)
btn3=Button(Calc,padx=16,bd=8,fg="black",font'''

root.configure(menu=menubar)
root.mainloop()

