from tkinter import *
from PIL import ImageTk, Image



def btn_clicked():
    print("Button Clicked")


window = Tk()


window.geometry("1440x1024")
window.configure(bg = "#0a0a0a")
canvas = Canvas(window, bg = "#0a0a0a", height = 1024, width = 1440, bd = 0,  highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(716.0, 502.0, image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0, command = btn_clicked, relief = "flat")

b0.place(x = 594, y = 738, width = 251, height = 38)






window.resizable(False, False)
window.mainloop()
