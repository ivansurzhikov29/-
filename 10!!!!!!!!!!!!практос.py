from tkinter import* 

from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from tkinter.ttk import Radiobutton

def cleck():
    if combo.get()=="+":label1.configure(text=int(spin.get())+int(spin1.get()))
    elif combo.get()=="-":label1.configure(text=int(spin.get())-int(spin1.get()))
    elif combo.get()=="*":label1.configure(text=int(spin.get())*int(spin1.get()))
    elif combo.get()=="/" and spin1.get()=="0":label1.configure(text="00")
    else :label1.configure(text=int(spin.get())/int(spin1.get()))
                                                                                          #"ПОДПРОГРАММЫ"
def cleck1():
   if selected.get()==0: messagebox.showinfo("Вы выбрали","1 вкл")
   if selected.get()==1: messagebox.showinfo("Вы выбрали","2 вкл")
   if selected.get()==2: messagebox.showinfo("Вы выбрали","3 вкл ")

def cleck2():
    with open('text.txt','r') as file:
        text.delete(1.0, END)
        texttext.insert(1.0, file.read())
    filefile.close()

def cleck3():
    with open('text.txt','w') as file1:
         file1.write(text.get(1.0, END))
    file1.close()

window = Tk()
window.title("Суржиков Иван Сергеевич")

window.geometry("1000x750")                                                             # ПАРАМЕТРЫ ОКНА 
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1,text="вкладка 1")
tab_control.add(tab2,text=" вкаладка 2")
tab_control.add(tab3,text="вкладка 3 ")
tab_control.pack(expand=1,fill='both')

var =IntVar()
var.set(0)
spin=Spinbox(tab1,from_=-100000,to=100000,width=10,justify="center",textvariable=var)
spin.grid(column=0,row=0)
combo=Combobox(tab1,justify="center",width=5)
combo["values"]=("+","-","*","/")
combo.current(0)
combo.grid(column=1,row=0)
var1 =IntVar()
var1.set(0)
spin1=Spinbox(tab1,from_=-100000,to=100000,width=10,justify="center",textvariable=var1)
spin1.grid(column=2,row=0)
btn = Button(tab1,text="нажми", bg = "black", fg = "red", command=cleck1)
btn.grid(column=3,row=0)
label1 = ttk.Label(tab1,text="1")
label1.grid(column=4,row=0)

selected=IntVar()
selected.set(0)
rad1=Radiobutton(tab2,text="кнопка 1",value=0,variable=selected)
rad2=Radiobutton(tab2,text="кнопка 2",value=1,variable=selected)
rad3=Radiobutton(tab2,text="кнопка 3",value=2,variable=selected)
rad1.grid(column=0,row=0)
rad2.grid(column=1,row=0)
rad3.grid(column=2,row=0)
btn1= Button(tab2,text="жмякай",command=cleck1)
btn1.grid(column=0,row=1)

text=scrolledtext.ScrolledText(tab3,width=50,height=10,bg="black",fg="white")
text.grid(row=0, column=0, columnspan=2,padx=35)
btn2= Button(tab3,text="Загузить",command=cleck2)
btn2.grid(row=1, column=0, pady=10)
btn3= Button(tab3,text="Сохранить",command=cleck3)
btn3.grid(row=1, column=1)

window.mainloop()
