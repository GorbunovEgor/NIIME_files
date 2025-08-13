from tkinter import *
from tkinter import ttk
import easygui



Min = 1000
Max = 2000
cp = 15



root = Tk()
root.title("Обработчиик_данных")
root.geometry("400x500")
root.resizable(width=False , height=False)
root.iconbitmap('1489187695-billingdatayencurrency_81853.ico')
#root.config(bg="Black")
#root["bg"] = "#009999"
img = PhotoImage(file="gradient_400_500.png")
l_logo = Label(root, image=img)
l_logo.pack()
 




def click_0():
    global Min
    global Max
    global cp
    
    Min = Min + 10000
    Max = Max + 10000
    cp = cp + 10000
    
    
    print(Min)
    print(Max)
    print(cp)


def click():
    #print('Выполнено')
    win = Toplevel()
    win.title("Параметры_графика")
    win.geometry('270x150')
    win.grab_set()
    win.iconbitmap('1489187695-billingdatayencurrency_81853.ico')
    win.resizable(width=False , height=False)
    
    
    l = Label(win, text = ("min =") , font='Arial 13' , bg = "#940099" ).place(x=10 , y=10)
    l_1 = Label(win, text = ("max =") , font='Arial 13' , bg = "#940099" ).place(x=10 , y=40)
    l_2 = Label(win, text = ("counter_plot = ") , font='Arial 13' , bg = "#940099" ).place(x=10 , y=70)
    
    
    min = Entry(win)
    min.place(x=130 , y=10)
    min.insert(END,Min)
    
    max = Entry(win)
    max.place(x=130 , y=40)
    max.insert(END,Max)
    
    counter_plot = Entry(win)
    counter_plot.place(x=130 , y=70)
    counter_plot.insert(END,cp)
    
    
    btn_0 = Button(win, text = "Назначить" , command = click_0 , font='Arial 13' , bg = "#940099" , activebackground = "#FF0099")
    btn_0.place(x=100 , y=100)
    
    
    
    
    
    
    
def click_1():
    input_file = easygui.fileopenbox(filetypes=["*.docx"])
    #pre.insert(END,"hello")
    pre.insert(END,  input_file)
    
def click_2():
    input_file = easygui.fileopenbox(filetypes=["*.docx"])
    #pre.insert(END,"hello")
    post.insert(END,  input_file)
    
    
def click_3():
    input_file = easygui.fileopenbox(filetypes=["*.docx"])
    #pre.insert(END,"hello")
    file_r.insert(END,  input_file)







#btn_1 = Button(root, text = "Выбрать" , command = click_1 , font='Arial 10' , bg = "#660099" , activebackground = "#FF0099")
#btn_1.place(x=310 , y=50)
#btn.pack()

btn = Button(root, text = "Выполнить" , command = click , font='Arial 13' , bg = "#940099" , activebackground = "#FF0099")
btn.place(x=150 , y=450)


label_0 = Label(root, text = "Файл_PRE" , font='Arial 13' , bg = "#940099" )
#label.pack()
label_0.place(x=10 , y=50)

pre = Entry(root)
pre.place(x=180 , y=50)

btn_1 = Button(root, text = "Выбрать" , command = click_1 , font='Arial 10' , bg = "#940099" , activebackground = "#FF0099")
btn_1.place(x=310 , y=50)



label_1 = Label(root, text = "Файл_POST" , font='Arial 13' , bg = "#940099" )
label_1.place(x=10 , y=90)

post = Entry(root)
post.place(x=180 , y=90)

btn_2 = Button(root, text = "Выбрать" , command = click_2 , font='Arial 10' , bg = "#940099" , activebackground = "#FF0099")
btn_2.place(x=310 , y=90)



label_2 = Label(root, text = "Файл_RESULT" , font='Arial 13' , bg = "#940099" )
label_2.place(x=10 , y=130)

file_r = Entry(root)
file_r.place(x=180 , y=130)

btn_3 = Button(root, text = "Выбрать" , command = click_3 , font='Arial 10' , bg = "#940099" , activebackground = "#FF0099")
btn_3.place(x=310 , y=130)



label_3 = Label(root, text = "Название_листа" , font='Arial 13' , bg = "#940099")
label_3.place(x=10 , y=170)

name_l = Entry(root)
name_l.place(x=180 , y=170)



label_4 = Label(root, text = "Количество_точек" , font='Arial 13' , bg = "#940099" )
label_4.place(x=10 , y=210)

counter_t = Entry(root)
counter_t.place(x=180 , y=210)



print(Min)
print(Max)
print(cp)


root.mainloop()

#name = input("введите имя ")
#print(name)





