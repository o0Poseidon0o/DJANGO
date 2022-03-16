from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Test thoat chuong trinh")
root.iconbitmap('D:\django\DJANGO_KHTN\DJANGO\GUI_python\icon.png')

my_img = ImageTk.PhotoImage(Image.open("gai.jpg"))
my_label = Label(image=my_img)
my_label.pack()


button_quit= Button(root, text="Thoat chuong trinh", command=root.quit)
button_quit.pack()

root.mainloop()