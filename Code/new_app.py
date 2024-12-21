from PIL import Image, ImageTk
import PIL.Image 
import time
import speech_recognition as sr
import pyttsx3
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from PIL import ImageGrab
from translate import Translator
import time
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib
import random
# print(random.randint(0,9))
from email.mime.multipart import MIMEMultipart
from tkinter import*
from tkinter import ttk
import tkinter
from imutils.video import VideoStream
import cv2
import time
import f_detector
import imutils
import numpy as np
# from dbtkint import Database
from tkinter import messagebox
# dbtkint=Database("employers.db")
admin=Tk()
admin.title(" SURVEILLANCE SYSTEM ")
admin.geometry("900x600+0+0")

# b = Button(admin,text = "Simple") 

n_name=tkinter.StringVar()
n_meet=tkinter.StringVar()
n_key=tkinter.StringVar()

# b.pack()  
# admin.config(bg="blue")
bg = PhotoImage(file = "cam.png")
  
# Show image using label
label1 = Label( admin, image = bg)
label1.place(x = 0, y = 0)
head_label = Label(admin,width= 30, text=" SURVEILLANCE SYSTEM ")
head_label.pack(pady=10)

# img1="Image1.png"
# load = PIL.Image.open(img1)
# render = ImageTk.PhotoImage(load)
# img = Label(admin, image=render)
# img.image = render
# # img.place(x=0, y=0)
# img.config(image=render,width="150",height="100")



engine=pyttsx3.init()
r = sr.Recognizer()

# def someFunction():
    # print("Hello world")
def auto_camera():
    nam=n_name.get()
    meet=n_meet.get()
    key=n_key.get()
    print('num',nam)
    print('num',meet)
    print('num',key)

    detector = cv2.CascadeClassifier("./data/haarcascade_frontalface_default.xml")
    vid = cv2.VideoCapture(0)
    while(True):
        ret, frame = vid.read()
        cv2.imshow('frame', frame)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # face=face_cascade.detectMultiScale(gray,1.1,4)
        # grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face = detector.detectMultiScale(image=gray, scaleFactor=1.1, minNeighbors=5)
        for (x,y,w,h) in face:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        key = cv2.waitKey(1)        
        img_name = "C:\\Users\\Vinay.Subramaniam\\Desktop\\project\\face_recognition\\ImagesAttendance\\{}.png".format(nam)
        # name.makedirs('{}'.format(img_name))
        cv2.imwrite(img_name, frame)           
        print("{} written!".format(nam))
            # num+=1
            # img_counter += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    try:         
        if n_meet.get() == "kishore" and n_key.get() == "nlvkruh":
            print("a success !")
            val=1
        elif n_meet.get()=="vishnu" and n_key.get() == "ylvkqx":
            print("b success !")
            val=1
        elif n_meet.get() =="vinay" and n_key.get() == "ylqdb":
            print("c success !")
            val=1
        elif n_meet.get()=="vishal" and n_key.get() == "ylvkdo":
            print("b success !")
            val=1
        elif n_meet.get() =="shiva" and n_key.get() == "vklyd":
            print("c success !")
            val=1
        elif n_meet.get()=="vinoth" and n_key.get() == "ylnudp":
            print("b success !")
            val=1
        elif n_meet.get() =="vishva" and n_key.get() == "ylvkyd":
            print("c success !")
            val=1
        elif n_meet.get()=="yogesh" and n_key.get() == "brjhvk":
            print("b success !")
            val=1
        elif n_meet.get() =="vikram" and n_key.get() == "ylnudp":
            print("c success !")
            val=1
        elif n_meet.get()=="muthu" and n_key.get() == "pxwkx":
            print("b success !")
            val=1
        elif n_meet.get() =="thyanesh" and n_key.get() == "wkbdqhvk":
            print("c success !")
            val=1
        else:
            # someFunction()
            # button_page()
            print("Unknown person !")
            # someFunction()
            val=0
            now = datetime.now()
            print(now)
            dtString = now.strftime('%H:%M:%S')
            # print("Unknown person !")
            msg = ("         INTRUDER ALERT \n ********* \n UNAUTHORIZED PERSON TRIED TO ENTER THE SERVELLANCE AREA AND THE PERSON DIDN'T PASS THE SECURITY CHECK @ {}".format(dtString))
            SMTP_USERNAME = 'vishnuprakash0112@gmail.com'
            SMTP_PASSWORD = 'tfqvqyhsnjqtiyvj'
            SMTP_PORT = 587
            SMTP_SERVER = 'smtp.gmail.com'
            server = smtplib.SMTP('smtp.gmail.com', 25)
            server.connect("smtp.gmail.com",587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            # text = msg.as_string()
            server.sendmail("vishnuprakash0112@gmail.com","shreekishore14@gmail.com", msg)
            print("successfully")
            server.quit()
    except:
        # button_page()
        print("failed ")
        # num+=1
        # time.sleep(2)
        # return None

    vid.release()
    cv2.destroyAllWindows()

def someFunction():
    def blink():
        from imutils.video import VideoStream
        import cv2
        import time
        import f_detector
        import imutils
        import numpy as np

        # instancio detector
        detector = f_detector.eye_blink_detector()
        # iniciar variables para el detector de parapadeo
        # COUNTER = 0
        # TOTAL = 0
        # i=0
        # ----------------------------- video -----------------------------
        #ingestar data
        vs = VideoStream(src=0).start()
        while True:
            star_time = time.time()
            im = vs.read()
            im = cv2.flip(im, 1)
            im = imutils.resize(im, width=720)
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            # detectar_rostro    
            rectangles = detector.detector_faces(gray, 0)
            boxes_face = f_detector.convert_rectangles2array(rectangles,im)
            if len(boxes_face)!=0:
                # seleccionar el rostro con mas area
                areas = f_detector.get_areas(boxes_face)
                index = np.argmax(areas)
                rectangles = rectangles[index]
                boxes_face = np.expand_dims(boxes_face[index],axis=0)
                # blinks_detector
                COUNTER,TOTAL = detector.eye_blink(gray,rectangles,COUNTER,TOTAL)
                # agregar bounding box
                img_post = f_detector.bounding_box(im,boxes_face,['blinks: {}'.format(TOTAL)])
            else:
                img_post = im 
            # visualizacion 
            end_time = time.time() - star_time    
            FPS = 1/end_time
            cv2.putText(img_post,f"FPS: {round(FPS,3)}",(10,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
            cv2.imshow('blink_detection',img_post)
            i=i+1
            if TOTAL==3:
                return True
            if i==50:
                if TOTAL==0:
                    return False

            if cv2.waitKey(1) &0xFF == ord('q'):
                break

    def SpeakText(command):     
        # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()

    path = 'C:\\Users\\Vinay.Subramaniam\\Desktop\\project\\face_recognition\\ImagesAttendance'
    images = []
    classNames = []
    myList = os.listdir(path)
    # print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    # print(classNames)

    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    def markAttendance(name):
        with open('Att.csv','r+') as f:
            myDataList = f.readlines()
            nameList = []
            print(nameList)
            # print("attendance",name)
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            # if name in nameList:
            if True:
                now = datetime.now()
                # print(now)
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString}')
    encodeListKnown = findEncodings(images)
    def button_page():
        entries_frame=Frame(bg="blue")
        entries_frame.pack(side=TOP,fill=X)
        title=Label(entries_frame,text="New user page", font=("Calibri",18,"bold"),bg="blue",fg="white")
        title.grid(row=0,columnspan=2, padx=10,pady=10)

        lblname=Label(entries_frame,text="Name", font=("Calibri",16),bg="green",fg='yellow')
        lblname.grid(row=1,column=0,padx=15,pady=10,sticky="w")
        txtname=Entry(entries_frame, textvariable=n_name,font=("Calibri",16),width=30)
        txtname.grid(row=1,column=1,padx=15,pady=10,sticky="w")

        # entries_frame=Frame(bg="blue")
        # entries_frame.pack(side=TOP,fill=X)
        # title=Label(entries_frame,text="who want to meet you ", font=("Calibri",18,"bold"),bg="blue",fg="white")
        # title.grid(row=0,columnspan=2, padx=10,pady=10)

        lblmeet=Label(entries_frame,text="Who want to meet you ", font=("Calibri",16),bg="green",fg='yellow')
        lblmeet.grid(row=3,column=0,padx=15,pady=10,sticky="w")
        txtmeet=Entry(entries_frame, textvariable=n_meet,font=("Calibri",16),width=30)
        txtmeet.grid(row=3,column=1,padx=15,pady=10,sticky="w")

        
        lblkey=Label(entries_frame,text="Secret Key ", font=("Calibri",16),bg="green",fg='yellow')
        lblkey.grid(row=6,column=0,padx=15,pady=10,sticky="w")
        txtkey=Entry(entries_frame, textvariable=n_key,font=("Calibri",16),width=30)
        txtkey.grid(row=6,column=1,padx=15,pady=10,sticky="w")
                # admin.config(bg="blue")

        btn_frame=Frame(entries_frame,bg="#535c68")
        btn_frame.grid(row=15,column=0,columnspan=4,padx=15,pady=15,sticky="w")
        btnAdd=Button(btn_frame,command=auto_camera,text="Submit",font=("Calibri",16),bg="green",fg="white",bd=0)
        btnAdd.grid(row=15,column=1,padx=5)
        # print(txtname.get())
        unknown_person_name=n_name.get()
        # if unknown_person_name==None:
        #     return unknown_person_name
        # else:
        #     return None
        admin.update()
    
    print('Encoding Complete- Press Q or q to CLOSE WEBCAM')

    # @app.route('/cam')
    # def cam():
    detector = f_detector.eye_blink_detector()
        # iniciar variables para el detector de parapadeo
        # COUNTER = 0
        # TOTAL = 0
        # i=0
        # ----------------------------- video -----------------------------
        #ingestar data
    cap = VideoStream(src=0).start()
    name="1"
    COUNTER = 0
    TOTAL = 0
    i=0
    while True:
        im = cap.read()
        if i<100:
            star_time = time.time()
            
            im = cv2.flip(im, 1)
            im = imutils.resize(im, width=720)
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            # detectar_rostro    
            rectangles = detector.detector_faces(gray, 0)
            boxes_face = f_detector.convert_rectangles2array(rectangles,im)
            if len(boxes_face)!=0:
                # seleccionar el rostro con mas area
                areas = f_detector.get_areas(boxes_face)
                index = np.argmax(areas)
                rectangles = rectangles[index]
                boxes_face = np.expand_dims(boxes_face[index],axis=0)
                # blinks_detector
                COUNTER,TOTAL = detector.eye_blink(gray,rectangles,COUNTER,TOTAL)
                # agregar bounding box
                img_post = f_detector.bounding_box(im,boxes_face,['blinks: {}'.format(TOTAL)])
            else:
                img_post = im 
            # visualizacion 
            end_time = time.time() - star_time    
            FPS = 1/end_time
            cv2.putText(img_post,f"FPS: {round(FPS,3)}",(10,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
            cv2.imshow('blink_detection',img_post)
            
            if TOTAL==3:
                val= True
            if i==50:
                if TOTAL==0:
                    val= False


        else:
            # success, img = cap.read()
            # img = captureScreen()
            imgS = cv2.resize(im,(0,0),None,0.25,0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
            if name=="Unknown Person":
                break
            for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
                #print(faceDis)
                matchIndex = np.argmin(faceDis)
                # print(matches[matchIndex])
                if matches[matchIndex]:
                    name = classNames[matchIndex].upper()
                    # print(name)
                    y1,x2,y2,x1 = faceLoc
                    y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                    cv2.rectangle(im,(x1,y1),(x2,y2),(0,255,0),2)
                    cv2.rectangle(im,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                    cv2.putText(im,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                    
                    #if val:
                    markAttendance(name)
                    # print("name",name)
                    # markAttendance(name)
                    # engine.say(name)
                    # engine.runAndWait()
                    # SpeakText(name)
                else:
                    name="Unknown Person"
                    # print(name)
                    y1,x2,y2,x1 = faceLoc
                    y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                    cv2.rectangle(im,(x1,y1),(x2,y2),(0,255,0),2)
                    cv2.rectangle(im,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                    cv2.putText(im,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                    # break
                    button_page()
            cv2.imshow('Webcam',im)    
        i=i+1
        b=cv2.waitKey(1)
        if b==31 or b==113:
            print("End Face Detection")
            break
            
def main():
    button = Button(admin,text=" Start Security Camera ", bg='cyan', height=4, width=25,command=someFunction)
    button.pack(padx=100,pady=20)
# button.pack

main()
# if val==1:
#     main()

admin.mainloop()
