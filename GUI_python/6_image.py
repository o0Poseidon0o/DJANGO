from tkinter import *
from PIL import ImageTk,Image #Phai cai Pillow. pip install pillow

root = Tk()
root.title("Test thoat chuong trinh")
root.iconbitmap('C:\Users\POSEIDON\Desktop\DJANGO\DJANGO\image\icon.png')

my_img = ImageTk.PhotoImage(Image.open('image\doreamon.png'))
my_label = Label(image=my_img)
my_label.pack()


button_quit= Button(root, text="Thoat chuong trinh", command=root.quit)
button_quit.pack()

root.mainloop()