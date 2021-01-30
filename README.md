# TemperatureIdentity
Infrared Temperature Sensor using Computer Vision with cloud capacities 
Temperature Identity Code Documentation 
By Ayush Singh 

For explanation purposes, I will include a step-by-step explanation of the code. 

Step 1: Accessing the Python Code 
To view the code, please visit https://github.com/ayushcv/TemperatureIdentity 

Once arrived, please click on the folder “Code(Temp Identity)” 

Please ignore “_pycache_” (This is an automated file) 

The final code is called “Final_code.py” 

If interested, all extra codes and test cases are present in “Extra Code for testing cases” 

Step 2: Opening the Python Code 

You should now be looking at “Final_code.py” Click on it, and the code will be present. There should be a total of 203 lines. 

Step 3: Understanding the Python Code 

Libraries (Lines 1- 18) 
Sys and os libraries help set system-specific parameters and allow the use of the operating system. 
Cv2 and NumPy are OpenCV libraries that allow the use of computer vision in the code. 
Pyzbar.pyzbar is used for understanding the sequences of the bar code. 
Time is used to import the current time using the device’s location. 
RPI.GPIO is used to get the servo readings 
Googleapiclient.HTTP and Google are used to create the google drive service. 
SMBus and mlx90414 are used to get the infrared temperature sensor readings. This library allows certain methods and functions to be used. SMBUS allows the signal to be readable. 

SetVariables (Lines 20-50) 
Google Client Services, JSON files, and API Version are all provided to allow the use of the Google Drive API. The JSON File acts as the encryption code for the access of the Google servers. 
Service = The google drive services are created with the information above. Then the designation of the database file is provided with IDs. 
GPIO.setmode = tells the Raspberry Pi to enable the output pins, and provides the location of the servos. (pin 11,13) 
Objects, facecascade, and cap are set to enable the functionality of the computer vision. This creates the frame for the live video. 
Barcode Database (Lines 52-56) 
The barcode database file is opened from the directory, and the data is stored in the myDataList variable.
Restart Function (Lines 59-61) 
restart_program() is used to restart the program once the while loop of each user ends. This allows a seamless behavior from a user flow perspective. 
Main While Loop (Lines 64 - 199) 
Video capture is stored and displayed on the screen. 
For Loop (barcode) 
Data is read from the database, and stored into myData. 
If Statement checks if the barcode is authorized.
IF TRUE
 If the barcode is authorized...OpenCV will run and convert the video stream into grayscale to create the face outlines. 
As the face is detected, a For Loop will create a rectangular box around the face and the forehead. These x and y values will also be used to create text on the screen. 
An Algorithm for x-axis and y-axis with ranges is created. These ranges are evenly divided to cover the whole range of movements. The ranges are calculated with averages and the degrees which are evenly divided.
As the person moves from one range to the other, the servo movement occurs accordingly. The servo successfully follows the person’s forehead.
An SMBus is opened to allow the temperature readings to come at the exact moment. The bus is open with binary digit 1 and the temperature is stored into ter. Then the bus is closed. 
The database document is open with the var r. 
If Statement creates a threshold for the temperature readings. 
If True, the Name/temp/time is stored in the database. 
If False, the Name/temp/time and a WARNING is stored into the database as the student’s temperature may be harmful. A DANGER TEXT is displayed on the screen. 
The obj becomes True and the loop is broken. The stream is broken and the students are good to go/ may be rejected as the DANGER sign is displayed if the temp is greater than the threshold. 
ELSE: 
A message is displayed that the user is un-authorized to enter the system. The error message is displayed on the screen using the cv2.putText. 
The live video continues until the correct barcode is presented. 
If statement checks whether the above loop has been completed. 
IF TRUE: 
The type of file is detected from the directory. 
Media = the media type file being uploaded into the cloud.
A service is created and the files are updated using the google drive service API.
Then the database is updated. 
Restart_program() Line (203) 
The program restarts to create seamless behavior for the next user. 






Step 4: Accessing the Website Code 
To view the code, please visit https://github.com/ayushcv/ayushcv.github.io/tree/master/TEJ4MO 

The final code is called “index.html” 

If interested, all assets and images are present in “Assets, Images” The cascading style sheets are also present in these folders. 

Step 5: Opening the Website Code 

You should now be looking at “index.html” Click on it, and the code will be present. There should be a total of 189 lines. 

Step 6: Understanding the Website Code 

Head (lines 4 -11) 
This allows for the title of the web page to be saved and the CSS and JS files are imported for use.
Body (lInes 12-187) 
The first header of the website is present. The text is classified into columns and rows.
A Button is added to enable a scroll down functionality.
A container is used to set the placement of the text and features. This section includes the databases and the name of the classroom. It is set in a container provided by the CSS.
AN IFRAME IS CREATED TO MAKE A PORTAL BETWEEN THE DATABASE and the website. Updated at every input.
A Scroll Button to go down the page is added again. 
Section 3. This includes a couple of pictures and buttons which take you to the desired web pages for more information. The styling of the buttons is done in the CSS files and they are called with styles and set with HREF links for redirection to the various webpages. 
THIS IS ANOTHER SCROLL BUTTON TO GO TO THE CONTACT ME SECTION. 
The footer includes social media, and the links are there to go to the contact information. 
The class of the icons is brought from the CSS and the links are provided with the HREF. 
My Javascript files are called to use their functionalities to allow browser and scrolling capabilities. 

**Optional** 
Step 7: Javascript Code Overview 

Please Access “main.js”
The Javascript file is used to create the breakpoints, and add the animations on the page load. The scrollable button is used to navigate through the webpage.

Step 8: CSS Code Overview 

Please Access “main.css” 

The CSS is made to set the methods, class, container, and boxes. Alongside that, the button styling all occurs here. 
The file is very long as you have to configure each dimension, color-code, animation, and text. 
There is a bird animation trails code in there, it is extra and is not used in the finalized HTML files as it is not necessary. 


Thank you for your time. This is the end of the documentation. 

