from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import filedialog
import cv2
import time
import pickle
import cvzone
import numpy as np
import os
# import splash_screen_gui

#Local Start Video
def ipCam():
    w.iconify()
    cap = cv2.VideoCapture(0)
    video_file_count = 0
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    t = time.strftime("%m-%d-%Y %H-%M-%S")
    out = cv2.VideoWriter('C:/Users/hp/PycharmProjects/detection/parkdtec_video/parkdtec_video' + t + '.avi',
                          fourcc, 20.0, (frame_width, frame_height))

    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)

    # width, height = 120, 89
    width, height = 103, 43

    def checkParkingSpace(imgPro):
        spaceCounter = 0

        for pos in posList:
            x, y = pos

            imgCrop = imgPro[y:y + height, x:x + width]
            # cv2.imshow(str(x * y), imgCrop)
            count = cv2.countNonZero(imgCrop)

            if count < 900:
                color = (0, 255, 0)
                thickness = 5
                spaceCounter += 1
            else:
                color = (0, 0, 255)
                thickness = 2

            cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
            cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1,
                               thickness=3, offset=0, colorR=color)

        cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (100, 50), scale=3,
                           thickness=5, offset=20, colorR=(0, 200, 0))

    while (cap.isOpened):
        if cap.isOpened():
            print("Successfully accessed the IP Address!")
        else:
            messagebox.showwarning("", "Failed to access!")
            break

        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        success, img = cap.read()
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
        imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv2.THRESH_BINARY_INV, 25, 16)
        imgMedian = cv2.medianBlur(imgThreshold, 5)
        kernel = np.ones((3, 3), np.uint8)
        imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

        checkParkingSpace(imgDilate)
        # img1 = cv2.resize(img,(1280,720),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
        out.write(img)
        print("Recording video", t)

        video_file_count += 1
        cv2.imshow("Detecting Parking Area", img)

        k = cv2.waitKey(30) & 0xFF
        if k == 27 or cv2.getWindowProperty("Detecting Parking Area", cv2.WND_PROP_VISIBLE) < 1:
            response = messagebox.askquestion("", "Are you sure, do you want to stop the video?")
            if response == 'no':
                continue
            else:
                messagebox.showinfo("","The video successfully saved!")
                break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

#Local Start Video End

#Wireless Start Video
def wirelessCam():
    w.iconify()
    cap = cv2.VideoCapture('http://192.168.1.2:8080/video')
    video_file_count = 0
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    t = time.strftime("%m-%d-%Y %H-%M-%S")
    out = cv2.VideoWriter('C:/Users/hp/PycharmProjects/detection/parkdtec_video/parkdtec_video' + t + '.avi',
                          fourcc, 20.0, (frame_width, frame_height))

    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)

    # width, height = 120, 89
    width, height = 103, 43

    def checkParkingSpace(imgPro):
        spaceCounter = 0

        for pos in posList:
            x, y = pos

            imgCrop = imgPro[y:y + height, x:x + width]
            # cv2.imshow(str(x * y), imgCrop)
            count = cv2.countNonZero(imgCrop)

            if count < 900:
                color = (0, 255, 0)
                thickness = 5
                spaceCounter += 1
            else:
                color = (0, 0, 255)
                thickness = 2

            cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
            cvzone.putTextRect(img, str(count), (x, y + height - 2), scale=1,
                               thickness=2, offset=0, colorR=color)

        cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (100, 50), scale=3,
                           thickness=5, offset=20, colorR=(0, 200, 0))

    while (cap.isOpened):
        if cap.isOpened():
            print("Successfully accessed the IP Address!")
        else:
            messagebox.showinfo("", "Invalid input!")
            break

        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        success, img = cap.read()
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
        imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv2.THRESH_BINARY_INV, 25, 16)
        imgMedian = cv2.medianBlur(imgThreshold, 5)
        kernel = np.ones((3, 3), np.uint8)
        imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

        checkParkingSpace(imgDilate)
        # img1 = cv2.resize(img,(1280,720),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
        out.write(img)
        print("Recording video", t)

        video_file_count += 1
        cv2.imshow("Detecting Parking Area", img)

        k = cv2.waitKey(30) & 0xFF
        if k == 27 or cv2.getWindowProperty("Detecting Parking Area", cv2.WND_PROP_VISIBLE) < 1:
            response = messagebox.askquestion("", "Are you sure, do you want to stop the video?")
            if response == 'no':
                continue
            else:
                messagebox.showinfo("","The video successfully saved!")
                break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
#Wireless Start Video End

# Start Capture Background
def captureLocal():
    # def defaultImg():
    #     # global ip_g
    #     # cam = cv2.VideoCapture('http://192.168.1.2:8080/video')
    #     # cam = cv2.VideoCapture('http://192.168.18.27:8080/video')
    #     # ip = int(ip_g.get())
    cam = cv2.VideoCapture(0)
    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            messagebox.showwarning("","Failed to access!")
            break

        cv2.imshow("Capturing the background", frame)


        k = cv2.waitKey(30) & 0xFF
        if k == 27 or cv2.getWindowProperty("Capturing the background", cv2.WND_PROP_VISIBLE) < 1:
            break

        elif k % 256 == 32:
            img_name = "images\parking_image{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            response = messagebox.askquestion("", "Do you want to save this image?")
            if response == 'no':
                messagebox.showwarning("","No capture image!")
            else:
                messagebox.showinfo("","The image is successfully saved.")
                break


    cam.release()

    # cam.destroyAllWindows()

#Capture Wireless Start
def captureWireless():
    # def defaultImg():
    #     # global ip_g
    #     # cam = cv2.VideoCapture('http://192.168.1.2:8080/video')
    #     # cam = cv2.VideoCapture('http://192.168.18.27:8080/video')
    #     # ip = int(ip_g.get())

    cam = cv2.VideoCapture('http://192.168.1.2:8080/video')
    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            messagebox.showwarning("", "Failed to access!")
            break

        cv2.imshow("Capturing the background", frame)
        cv2.startWindowThread()


        k = cv2.waitKey(30) & 0xFF
        if k == 27 or cv2.getWindowProperty("Capturing the background", cv2.WND_PROP_VISIBLE) < 1:
            break

        elif k % 256 == 32:
            img_name = "images\parking_image{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            response = messagebox.askquestion("", "Do you want to save this image?")
            if response == 'no':
                messagebox.showwarning("","No capture image!")
            else:
                messagebox.showinfo("","The image is successfully saved.")
                break


    cam.release()
    # cam.destroyAllWindows()
#Capture Wireless Start

#Start Adjust Size
def adjust():

    def adjustPickerSize():
        width = int(e1.get())
        height = int(e2.get())

        import cv2 as cv

        Dirpath = 'C:/Users/hp/PycharmProjects/detection/images'
        Files = os.listdir(Dirpath)
        for File in Files:
            imgPath = os.path.join(Dirpath, File)
            print(imgPath)

            image = cv2.imread(imgPath, cv.IMREAD_GRAYSCALE)
            # cv.imshow('image', image)
            cv.waitKey(1)

            try:
                with open('CarParkPos', 'rb') as f:
                    posList = pickle.load(f)

            except:
                posList = []

            def mouseClick(events, x, y, flags, params):
                if events == cv2.EVENT_LBUTTONDOWN:
                    posList.append((x, y))
                if events == cv2.EVENT_RBUTTONDOWN:
                    for i, pos in enumerate(posList):
                        x1, y1 = pos
                        if x1 < x < x1 + width and y1 < y < y1 + height:
                            posList.pop(i)

                with open('CarParkPos', 'wb') as f:
                    pickle.dump(posList, f)

            while True:

                img = cv2.imread(imgPath)
                for pos in posList:
                    cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (300, 3, 300), 3)

                cv2.imshow("Image", img)
                cv2.setMouseCallback("Image", mouseClick)
                # if cv2.waitKey(2) & 0xFF == ord('q'):
                #     break

                k = cv2.waitKey(1) & 0xFF
                if k == 27 or cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE) < 1:
                    break
                if k % 256 == 32:
                    posList.clear()
        cv2.destroyAllWindows()



    def reset():
      for widget in w.winfo_children():
          if isinstance(widget,Entry):
              widget.delete(0,'end')

    r = Tk()
    r.title("SET MEASUREMENT")
    r.geometry("300x150")
    r.iconbitmap('C:/Users/hp/PycharmProjects/detection/fav1.ico')
    r.resizable(0, 0)
    frame = Frame(r,bg='#252726', width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    global e1
    global e2

    font_style = ("Helvetica", 10, "bold")
    Label(r,font=font_style, bg="darkorange",fg="#252726",text="Width : " ).place(x=10, y=10)
    Label(r,font=font_style,  bg="darkorange",fg="#252726",text="Height : ").place(x=10, y=40)

    e1 = Entry(r)
    e1.place(x=140, y=10)

    e2 = Entry(r)
    e2.place(x=140, y=40)

    Button(r,border=0,font=font_style,bg="darkorange",fg="#252726", text="Save", command=adjustPickerSize, height=1, width=10).place(x=10, y=100)
    Button(r,border=0,font=font_style,bg="darkorange",fg="#252726", text="Reset", command=reset, height=1, width=10).place(x=190, y=100)

    r.mainloop()

#Start Adjust Size End

#Start Quit
def quit():
    w.destroy()
#Start Quit End

#Start Open Recording Video
def openfileVideo():
    filetype=('All files','*.*'),('text files','*.txt')
    filepath= filedialog.askopenfilename(filetypes=filetype,initialdir=r'C:\Users\hp\PycharmProjects\detection\parkdtec_video')
    print(filepath)

    cap = cv2.VideoCapture(str(filepath))

    # Check if camera opened successfully
    if (cap.isOpened() == False):
        print("Error opening video stream or file")

    # Read until video is completed
    while (cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:

            # Display the resulting frame
            cv2.imshow('Video Frame', frame)

            # Press Q on keyboard to  exit
            k = cv2.waitKey(30) & 0xFF
            if k == 27 or cv2.getWindowProperty("Video Frame", cv2.WND_PROP_VISIBLE) <1:
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

#End Open Recording Video

w = Tk()
w.title("PARkDTEC")
w.geometry("900x500")
w.iconbitmap('C:/Users/hp/PycharmProjects/detection/fav1.ico')
w.resizable(0, 0)


bg_image1=ImageTk.PhotoImage(Image.open('C:/Users/hp/PycharmProjects/detection/background/bg1.jpg'))
bg_image2=ImageTk.PhotoImage(Image.open('C:/Users/hp/PycharmProjects/detection/background/bg2.jpg'))
bg_image3=ImageTk.PhotoImage(Image.open('C:/Users/hp/PycharmProjects/detection/background/bg3.jpg'))
bg_image4=ImageTk.PhotoImage(Image.open('C:/Users/hp/PycharmProjects/detection/background/bg4.jpg'))

lb=Label(w)
lb.pack()

#Local Port Start
def toggle_win1():
    global f1

    f1 = Frame(w, width=300, height=500, bg='#252726')
    f1.place(x=0, y=0)

    f_style = ("Helvetica", 8, "bold")
    def bttn(x, y, text, bcolor, fcolor, cmd):
        def on_entera(e):
            myButton1['background'] = bcolor  # ffcc66
            myButton1['foreground'] = 'white'  # 000d33


        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground'] = 'darkorange'

        myButton1 = Button(f1, text=text,
                           font=f_style,
                           width=42,
                           height=2,
                           fg='#FE6101',
                           border=0,
                           bg=fcolor,
                           activeforeground='white',
                           activebackground=bcolor,
                           command=cmd)

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)

    bttn(0, 20, 'L O C A L   C A M E R A', '#252726', '#252726', DISABLED)
    bttn(0, 80, 'S T A R T', 'darkorange', '#252726', ipCam)
    bttn(0, 117, 'C A P T U R E  B A C K G R O U N D', 'darkorange', '#252726', captureLocal)
    bttn(0, 154, 'S E T   M E A S U R E M E N T', 'darkorange', '#252726', adjust)
    bttn(0, 191, 'R E C O R D E D  V I D E O', 'darkorange', '#252726', openfileVideo)
    bttn(0, 228, 'E X I T', 'darkorange', '#252726',  f1.destroy)
    # bttn(0, 265, 'Q U I T', '#0f9d9a', '#12c4c0', quit)
#Local Port Start End

#Wireless Port Start
def toggle_win2():
    global f1

    f1 = Frame(w, width=300, height=600, bg='#252726')
    f1.place(x=0, y=0)

    f_style = ("Helvetica", 8, "bold")
    def bttn(x, y, text, bcolor, fcolor, cmd):
        def on_entera(e):
            myButton1['background'] = bcolor  # ffcc66
            myButton1['foreground'] = 'white'  # 000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground'] = 'darkorange'

        myButton1 = Button(f1, text=text,
                           font=f_style,
                           width=42,
                           height=2,
                           fg='#FE6101',
                           border=0,
                           bg=fcolor,
                           activeforeground='white',
                           activebackground=bcolor,
                           command=cmd)

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)


        myButton1.place(x=x, y=y)

    bttn(0, 20, 'W I R E L E S S   C A M E R A','#252726', '#252726', DISABLED)
    bttn(0, 80, 'S T A R T', 'darkorange', '#252726', wirelessCam)
    bttn(0, 117, 'C A P T U R E  B A C K G R O U N D', 'darkorange', '#252726', captureWireless)
    bttn(0, 154, 'S E T   M E A S U R E M E N T', 'darkorange', '#252726', adjust)
    bttn(0, 191, 'R E C O R D E D  V I D E O', 'darkorange', '#252726', openfileVideo)
    bttn(0, 228, 'E X I T', 'darkorange', '#252726',  f1.destroy)

    # bttn(0, 265, 'Q U I T', '#0f9d9a', '#12c4c0', quit)
#Wireless Port Start End

x=1
def move():
    global x
    if x==5:
        x=1;
    if x==1:
        lb.config(image=bg_image1)
    elif x==2:
        lb.config(image=bg_image2)
    elif x==3:
        lb.config(image=bg_image3)
    elif x==4:
        lb.config(image=bg_image4)

    w.after(4500,move)
    x+=1

font_style = ("Helvetica",8, "bold")

photo1 = ImageTk.PhotoImage(file=r"C:\Users\hp\PycharmProjects\detection\button_images\favicon (8).ico")
btn1 = Button(w, text="   LOCAL", image=photo1,compound=LEFT,font=font_style,bg="#FE6101",activebackground="darkorange",border=0,
              borderwidth=0,fg="black",command=toggle_win1,height=50, width=120).place(relx=0.5,rely=0.5,anchor=CENTER)


photo2 = ImageTk.PhotoImage(file=r"C:\Users\hp\PycharmProjects\detection\button_images\favicon (6).ico")
btn2 = Button(w,text="   WIRELESS",image=photo2,compound=LEFT,font=font_style,border=0,bg="#FE6101",activebackground="darkorange",
       borderwidth=0,fg="black",command=toggle_win2,height=50, width=120).place(x=388, y=290)

move()
w.mainloop()






