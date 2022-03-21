from tkinter import *

root = Tk()
root.title("Kala:)")
root.geometry("800x600")

w = 600
h = 400
x = w/2
y = h/2

my_canvas = Canvas(root, width=2000, heigh=h, bg="white")
my_canvas.pack(pady=20)

img = PhotoImage(file="c:/Users/Karl-Markus/Pictures/Haug/Haug.png")
my_image = my_canvas.create_image(260,125, image=img)

def move(e):
    global img
    img = PhotoImage(file="c:/Users/Karl-Markus/Pictures/Haug/Haug.png")
    my_image = my_canvas.create_image(e.x,e.y, image=img)
    my_label.config(text="Coordinates x: " + str(e.x) + " y: " + str(e.y))
    
my_label = Label(root, text="")
my_label.pack(pady=20)

my_canvas.bind("<B1-Motion>", move)

root.mainloop()