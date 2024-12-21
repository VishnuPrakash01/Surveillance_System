import time
import speech_recognition as sr
import pyttsx3
# import cv2
# import numpy as np
import face_recognition
# import os
from datetime import datetime
from PIL import ImageGrab
from translate import Translator
import os
import cv2
from PIL import Image
import numpy as np
from flask import Flask,render_template, request,url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("login.html")

# global name
@app.route('/res', methods = ['POST','GET'])
def login():
    if request.method=="GET":
        global name
        name = request.args.get('name')
        # name = os.makedirs(name)
        house_no = request.args.get('house_no')
        # return redirect(url_for('login'))
    return render_template("camera.html")

@app.route('/img')
def image():
    # face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
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
        # img_counter = 0
        # print(login(name))
        # num=0
        if key == 32:
            # storage = './{}/'.format(name)
            img_name = "C:\\Users\\User\\Desktop\\Babin_Projects\\New folder\\face_recognition\\ImagesAttendance\\{}.png".format(name)
            # name.makedirs('{}'.format(img_name))
            cv2.imwrite(img_name, frame)
            print("{} written!".format(name))
            # num+=1
            # img_counter += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # num+=1
    vid.release()
    cv2.destroyAllWindows()
    # return render_template("camera.html",image = img_name)
    success = "User Details Added Successfully"
    return render_template("register.html",names = success)


# import time

engine=pyttsx3.init()
r = sr.Recognizer()

def auto_camera(nam):
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
        # img_counter = 0
        # print(login(name))
        # num=0
        
        # storage = './{}/'.format(name)
        img_name = "C:\\Users\\User\\Desktop\\Babin_Projects\\New folder\\face_recognition\\ImagesAttendance\\{}.png".format(nam)
        # name.makedirs('{}'.format(img_name))
        cv2.imwrite(img_name, frame)           
        print("{} written!".format(nam))
            # num+=1
            # img_counter += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # num+=1
        time.sleep(2)
        return None

    vid.release()
    cv2.destroyAllWindows()

def SpeakText(command):     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

path = 'C:\\Users\\User\\Desktop\\Babin_Projects\\New folder\\face_recognition\\ImagesAttendance'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)
 
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
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')
  
encodeListKnown = findEncodings(images)
print('Encoding Complete- Press Q or q to CLOSE WEBCAM')
 
cap = cv2.VideoCapture(0)
@app.route('/cameras')
def cameras():
    while True:
        success, img = cap.read()
        # img = captureScreen()
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
    
        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
            #print(faceDis)
            matchIndex = np.argmin(faceDis)
            print(matches[matchIndex])
            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                print(name)
                y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                markAttendance(name)
                # engine.say(name)
                # engine.runAndWait()
                SpeakText(name)
                try:         
                    # use the microphone as source for input.
                    with sr.Microphone() as source2:
                        try:
                            audio2 = r.listen(source2)
                            MyText = r.recognize_google(audio2)
                            MyText = MyText.lower()
                            print("Did you say ",MyText)

                            # SpeakText(MyText)
                            # auto_camera(MyText)
                        except:
                            print("speech not recognized speech again..")

                except sr.RequestError as e:
                    print("Could not request results; {0}".format(e))

            else:
                name="Unknown Person"
                print(name)
                y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                markAttendance(name)
                speak = "who are you, what is your name "
                # time.sleep(1)
                SpeakText(speak)
                

                try:         
                    # use the microphone as source for input.
                    with sr.Microphone() as source2:
                        try:
                            audio2 = r.listen(source2)
                            MyText = r.recognize_google(audio2)
                            MyText = MyText.lower()
                            print("Did you say ",MyText)

                            # SpeakText(MyText)
                            auto_camera(MyText)
                        except:
                            print("speech not recognized speech again..")


                    # with sr.Microphone() as source2:
                    #     audio2 = r.listen(source2)
                    #     MyText = r.recognize_google(audio2)
                    #     MyText = MyText.lower()
                    #     print("Did you say ",MyText)

                # get_name=input("Enter the name :")
                # auto_camera(get_name)

                    
                except sr.RequestError as e:
                    print("Could not request results; {0}".format(e))
        cv2.imshow('Webcam',img)
        b=cv2.waitKey(1)
        if b==31 or b==113:
            print("End Face Detection")
            break
    return redirect(url_for('home'))
        
if __name__=="__main__":
    app.run(debug=True)