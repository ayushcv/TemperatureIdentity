#By Ayush Singh
#Libraries are imported to help use methods which allow the use of various methods
import sys
import os
#imports the Computer Vision Libraries
import cv2
import numpy as np
#Barcode detection with the computer vision
from pyzbar.pyzbar import decode
import time
#Servo GPIO readings
import RPi.GPIO as GPIO
#Google Client Reading with GOOGLE Drive APIS
from googleapiclient.http import MediaFileUpload
from Google import Create_Service
#Creating a smbus for the infrared temperature sensor. 5A
from smbus import SMBus
from mlx90614 import MLX90614

#google client variables. Importing the JSON Files for verification purposes.
CLIENT_SECRET_FILE = '/home/pi/Downloads/client_secret_368174336898-oaaah3llb1u44eulqe7cco9jg34ta2an.apps.googleusercontent.com.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
#Destination for the database file when uploaded. ID used in correlation to the JSON files
folder_id = '1VbcH3MZYEj6WNeryD2b282J3I2oQehSm'
file_names= ['database.txt']
mime_types= ['text/plain']
file_id = '1_DX6Lumm3mFob0W6hQL4xhK1WE-Wfdlg'

#Servo X axis
#The GPIO pins are now set to output signals
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
pwm= GPIO.PWM(13, 50)

#Servo Y Axis
GPIO.setup(11, GPIO.OUT)
pwmy= GPIO.PWM(11, 50)

# Classifying the video capture function to enable the computer vision. Creates the frame for the live video.
obj = False
faceCascade = cv2.CascadeClassifier("/home/pi/Resources12/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(4, 480)  # height
cap.set(10, 100)  # brightness
need = 0

#barcode reading : The data sheet is stored in the same folder. It only gives access to Ayush. Restricts access to Stewart
#img = cv2.imread('/home/pi/Resources12/frame (1).png')
with open('/home/pi/Resources12/myDataFile.text') as f:
    myDataList = f.read().splitlines()
count = 0

#Restart Program Function. This allows a seamless behavior for the program to repeat.
def restart_program():
    python = sys.executable
    os.execv(python, ['python'] + sys.argv)

#This is the main loop which allows the Computer vision to get activated,contributes to servo movements,&Google Services.
while True:
    #Starts the capture the video
    success, img = cap.read()
    #The barcode computer vision library scans through the database to verify users.
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
        #The if statement will check if the the QR code is authorized. If it works, face will get detected.
        if myData in myDataList:
            myOutput = 'Authorized'
            myColor = (0, 255, 0)
            cv2.destroyWindow("LIVE")
            #The face is detected as it gets converted into grayscale and faceoutlines are detected.
            while count<=20:
                success, img = cap.read()
                imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
                #This for loop allows a rectangular box to be created around the face and forehead.
                #These x and y values are used to create the location of texts and they are used for the servos.
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    cv2.putText(img, myData + ' User Detected', (x - 50,y + h +50 ), cv2.FONT_HERSHEY_COMPLEX, 1,(0, 0, 0), 2)
                    cv2.rectangle(img, (x + 20 , y + 20), (x + 100, y + 10 ), (0, 0, 255), 2)

                    #Algor for x axis with ranges. These ranges are evenly dived to cover the whole range of movements.
                    #The ranges are calculated with averages and the degrees which are evenly divided.
                    if x == 0:
                        pwm.start(12)
                    elif x in range(1,55):
                        pwm.start(11.5)
                    elif x in range(56,110):
                        pwm.start(11)
                    elif x in range(111,165):
                        pwm.start(10.5)
                    elif x in range(166,220):
                        pwm.start(10)
                    elif x in range(221,330):
                        pwm.start(9.5)
                    elif x in range(331,385):
                        pwm.start(9)
                    elif x in range(386,440):
                        pwm.start(8.5)
                    elif x in range(441,495):
                        pwm.start(8)
                    elif x in range(496,549):
                        pwm.start(7.5)
                    elif x == 550:
                        pwm.start(7)

                    #Y Axis Algorithm. These ranges are evenly dived to cover the whole range of movements.
                    #The ranges are calculated with averages and the degrees which are evenly divided.
                    if y == 0:
                        pwmy.start(2)
                    elif y in range(1,35):
                        pwmy.start(2.8)
                    elif y in range(36,70):
                        pwmy.start(3.6)
                    elif y in range(71,105):
                        pwmy.start(4.4)
                    elif y in range(106,139):
                        pwmy.start(5.2)
                    elif y in range(140,210):
                        pwmy.start(6)
                    elif y in range(210,245):
                        pwmy.start(7.2)
                    elif y in range(246,280):
                        pwmy.start(8.4)
                    elif y in range(281,315):
                        pwmy.start(9.6)
                    elif y in range(315,349):
                        pwmy.start(10.8)
                    elif y == 350:
                        pwmy.start(12)

                #This creates the SMBUS to allow temperature readings.
                while need <1:
                    bus = SMBus(1)
                    sensor = MLX90614(bus,address=0x5A)
                    #print ("Amb temp", sensor.get_ambient()) Adjusment factor is added to the temperature to consider for distance.
                    ter = ((sensor.get_object_1())//1 + 8)
                    bus.close()

                    #This opens the database in the raspberry folder.
                    r = open("/home/pi/Resources12/database.txt", "a")
                    #If temperature is below 35 Degrees C, the name/time/temp.
                    if ter <=35.0:
                        r.write("\n" + myData + " | " + str(ter) + " | " + time.ctime())
                        r.close()
                    #Name/temp/time is saved. If temperature is above 35 Degrees C, the name/time/temp is saved to database Alongside Warning.
                    else:
                        r.write("\n" + myData + " | " + str(ter) + " | " + time.ctime() + " PRECAUTION! (DANGER) ")
                        cv2.putText(img, myData + 'DO NOT ENTER', (x - 50,y + h +50 ), cv2.FONT_HERSHEY_COMPLEX, 1,(0, 0, 0), 2)
                        r.close()
                    need = need + 1

                    #Break Here. The loop is broken. TASK ARE COMPLETED Final
                    obj = True
                count = count + 1
                cv2.imshow("Video", img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        # IF barcode is not authorized, error message is shown.
        else:
            myOutput = 'Un-Authorized'
            myColor = (0, 0, 255)
        #Creates rectangle around the barcode to help indentify the code.
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, myColor, 5)
        pts2 = barcode.rect
        cv2.putText(img, myOutput, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, myColor, 2)

    cv2.imshow('LIVE', img)
    cv2.waitKey(1)

    #The google drive is called to finally update the database.
    if count>=20:
        #Finds the type of file. In this case, Text File.
        for file_name, mime_types in zip(file_names, mime_types):
            file_metadata={
                'name' : file_name,
                #'parents' : [folder_id]
            }
            #Media is saved the variable to send as package.
            media = MediaFileUpload('/home/pi/Resources12/{0}'.format(file_name), mimetype=mime_types)

            #The services is now updated with the API Call and is pushed.
            #The variables belowed are given values in the top of the code.
            service.files().update(
                fileId=file_id,
                body= file_metadata,
                media_body=media,
                fields='id'
            ).execute()

#The Program now restared for the next student.
#Restart function is stated before the while.
restart_program()