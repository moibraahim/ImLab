from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import cv2
from tkinter import filedialog
from tkinter.filedialog import askopenfile



class GUI(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.LoadWelcomePage()
    def btn_clicked(self):
        self.LoadMainPage()

    def LoadWelcomePage(self):
        canvas = Canvas(window, bg="#0a0a0a", height=1024, width=1440, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"WelcomePage/background.png")
        background = canvas.create_image(716.0, 502.0, image=background_img)

        img0 = PhotoImage(file=f"WelcomePage/img0.png")
        b0 = Button(image=img0, borderwidth=0, highlightthickness=0, command=lambda : self.btn_clicked(), relief="flat")

        b0.place(x=594, y=738, width=251, height=38)
        window.mainloop()

    def MedianFilter(self):
        NoisyImage = cv2.imread("Images/MedianFilter.jpg",0)
        m, n = NoisyImage.shape[0], NoisyImage.shape[1]
        ResultImage = np.zeros([m, n])

        for i in range(1, m - 1):

            for j in range(1, n - 1):
                ## Getting Every Value in the 3x3 matrix
                temp = [NoisyImage[i - 1, j - 1], NoisyImage[i - 1, j], NoisyImage[i - 1, j + 1], NoisyImage[i, j - 1],
                        NoisyImage[i, j],
                        NoisyImage[i, j + 1],
                        NoisyImage[i + 1, j - 1],
                        NoisyImage[i + 1, j],
                        NoisyImage[i + 1, j + 1]]

                temp = sorted(temp)
                ## Update the value of the current pixel with the median in the 4th position
                ResultImage[i, j] = temp[4]

        ## Casting the array to 8 bit integer
        ResultImage = ResultImage.astype(np.uint8)
        ResultImage = cv2.resize(ResultImage, (960, 540))
        cv2.imshow('Result of median filter', ResultImage)


    def LoadMainPage(self):
        window.geometry("1593x1024")
        canvas = Canvas(
            window,
            bg="#385fc5",
            height=1024,
            width=1593,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"MainPage/background.png")
        background = canvas.create_image(
            863.5, 384.5,
            image=background_img)

        img0 = PhotoImage(file=f"MainPage/img0.png")
        b0 = Button(
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=self.MedianFilter,
            relief="flat")

        b0.place(
            x=73, y=178,
            width=153,
            height=34)

        img1 = PhotoImage(file=f"MainPage/img1.png")
        b1 = Button(
            image=img1,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            relief="flat")

        b1.place(
            x=73, y=220,
            width=153,
            height=34)

        img2 = PhotoImage(file=f"MainPage/img2.png")
        b2 = Button(
            image=img2,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            relief="flat")

        b2.place(
            x=73, y=263,
            width=153,
            height=34)

        img3 = PhotoImage(file=f"MainPage/img3.png")
        b3 = Button(
            image=img3,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            relief="flat")

        b3.place(
            x=66, y=616,
            width=153,
            height=34)

        img4 = PhotoImage(file=f"MainPage/img4.png")
        b4 = Button(
            image=img4,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            relief="flat")

        b4.place(
            x=66, y=658,
            width=153,
            height=34)

        img5 = PhotoImage(file=f"MainPage/img5.png")
        b5 = Button(
            image=img5,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            relief="flat")

        b5.place(
            x=66, y=701,
            width=153,
            height=34)

        img6 = PhotoImage(file=f"MainPage/img6.png")
        b6 = Button(
            image=img6,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            relief="flat")

        b6.place(
            x=73, y=306,
            width=153,
            height=34)

        img7 = PhotoImage(file=f"MainPage/img7.png")
        b7 = Button(
            image=img7,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            relief="flat")

        b7.place(
            x=1315, y=531,
            width=153,
            height=34)

        img8 = PhotoImage(file=f"MainPage/img8.png")
        b8 = Button(
            image=img8,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            relief="flat")

        b8.place(
            x=1317, y=581,
            width=153,
            height=34)

        img9 = PhotoImage(file=f"MainPage/img9.png")
        b9 = Button(
            image=img9,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            relief="flat")

        b9.place(
            x=1315, y=168,
            width=232,
            height=34)

        img10 = PhotoImage(file=f"MainPage/img10.png")
        b10 = Button(
            image=img10,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            relief="flat")

        b10.place(
            x=1315, y=212,
            width=232,
            height=34)

        img11 = PhotoImage(file=f"MainPage/img11.png")
        b11 = Button(
            image=img11,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            relief="flat")

        b11.place(
            x=1315, y=253,
            width=232,
            height=34)

        img12 = PhotoImage(file=f"MainPage/img12.png")
        b12 = Button(
            image=img12,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            relief="flat")

        b12.place(
            x=1314, y=299,
            width=233,
            height=34)

        img13 = PhotoImage(file=f"MainPage/img13.png")
        b13 = Button(
            image=img13,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            relief="flat")

        b13.place(
            x=1314, y=341,
            width=233,
            height=34)

        img14 = PhotoImage(file=f"MainPage/img14.png")
        b14 = Button(
            image=img14,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            relief="flat")

        b14.place(
            x=1315, y=391,
            width=233,
            height=34)

        img15 = PhotoImage(file=f"MainPage/img15.png")
        b15 = Button(
            image=img15,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            relief="flat")

        b15.place(
            x=76, y=399,
            width=173,
            height=34)

        img16 = PhotoImage(file=f"MainPage/img16.png")
        b16 = Button(
            image=img16,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            relief="flat")

        b16.place(
            x=76, y=441,
            width=171,
            height=34)

        img17 = PhotoImage(file=f"MainPage/img17.png")
        b17 = Button(
            image=img17,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            relief="flat")

        b17.place(
            x=76, y=483,
            width=210,
            height=34)

        img18 = PhotoImage(file=f"MainPage/img18.png")
        b18 = Button(
            image=img18,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            relief="flat")

        b18.place(
            x=76, y=527,
            width=153,
            height=34)

        img19 = PhotoImage(file=f"MainPage/img19.png")
        b19 = Button(
            image=img19,
            borderwidth=0,
            highlightthickness=0,
            command= lambda : self.choose(),
            relief="flat")

        b19.place(
            x=612, y=830,
            width=176,
            height=49)

        img20 = PhotoImage(file=f"MainPage/img20.png")
        b20 = Button(
            image=img20,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            relief="flat")

        b20.place(
            x=823, y=830,
            width=175,
            height=49)


        window.mainloop()

    def choose(self):
        global InputImage
        f_types = [('Jpg Files', '*.jpg')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        InputImage = Image.open(filename)
        img_resized =  InputImage.resize((900, 540))  # new width & height
        InputImage = ImageTk.PhotoImage(img_resized)
        b2 = Button(window, image= InputImage)  # using Button
        b2.grid(row=3, column=1)
        b2.place(x=345,y=155)



window = Tk()
window.geometry("1440x1024")
window.configure(bg = "#0a0a0a")
window.resizable(False, False)
gui = GUI(window)
gui.mainloop()
