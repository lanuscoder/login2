from tkinter import *
from tkinter import messagebox
from turtle import title
from PIL import Image,ImageTk

win = Tk()
win.title('Đăng nhập')
win.geometry("500x750+300+50")
win.config(bg = "#141126")

def dangnhap():
    user = entry1.get()
    pw = entry2.get()
    if (user == 'lanuscoding') and (pw == '12345'):
        messagebox.showinfo('Thông báo','Đăng nhập thành công!')
    else:
        messagebox.showerror('Đăng nhập thất bại!',"Sai mật khẩu hoặc tên đăng nhập!")

image = Image.open("Screenshot_1.png")
img = image.resize((500,500))
mimg = ImageTk.PhotoImage(img)
lb1 = Label(win,image = mimg,bg = "#141126")
lb1.place(x = 0, y = -75)

but1 = Button(win,width=10,height=2,font=('Microsoft Yahei UI Light',16), text="Đăng nhập",
              border=0,fg="#fff",bg="orange",command=dangnhap)
but1.place(relx = 0.5,rely = 0.75,anchor=CENTER)

###
def enter(event):
    entry1.delete(0,'end')
def leave(event):
    ten = entry1.get()
    if ten == '':
        entry1.insert(0,'Tên đăng nhập')

entry1 = Entry(win, width=30, font = ('Microsoft Yahei UI Light',18),border=0,
               bg="#fff")
entry1.place(relx = 0.5, rely = 0.5,anchor=CENTER)
entry1.insert(0,'Tên đăng nhập')
entry1.bind('<FocusIn>',enter)
entry1.bind('<FocusOut>',leave)

###
def enter(event):
    entry2.delete(0,'end')
def leave(event):
    ten = entry2.get()
    if ten == '':
        entry2.insert(0,'Mật khẩu')
entry2 = Entry(win,width=30,font=('Microsoft Yahei UI Light',18),border=0,
               bg="#fff")
entry2.place(relx = 0.5, rely = 0.6,anchor=CENTER)
entry2.insert(0,'Mật khẩu')
entry2.bind('<FocusIn>',enter)
entry2.bind('<FocusOut>',leave)
win.mainloop()