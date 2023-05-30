# face_recognition_attendance_system
Face Recognition is a biometric method of identifying an individual by comparing live capture or digital image data with the store record for that person. Face Recognition Attendance System is marking of attendance on this technology.

1.1 Project Objective
Attendance is prime important for both the teacher and student of an educational organization. So it is very important to keep record of the attendance. The problem arises when we think about the traditional process of taking attendance in class room. 
Calling name or roll number of the student for attendance is not only a problem of time consumption but also it needs energy. So an automatic attendance system can solve all above problems. 
There are some automatic attendances making system which are currently used by much institution. One of such system is biometric technique and RFID system. Although it is automatic and a step ahead of traditional method it fails to meet the time constraint. The student has to wait in queue for giving attendance, which is time taking. 
This project introduces an involuntary attendance marking system, devoid of any kind of interference with the normal teaching procedure. The system can be also implemented during exam sessions or in other teaching activities where attendance is highly essential. This system eliminates classical student identification such as calling name of the student, or checking respective identification cards of the student, which can not only interfere with the ongoing teaching process, but also can be stressful for students during examination sessions. In addition, the students have to register in the database to be recognized. The enrolment can be done on the spot through the user friendly interface.


1.2 Problem Statement
Traditional student attendance marking technique is often facing a lot of trouble. The face recognition student attendance system emphasizes its simplicity by eliminating classical student attendance marking technique such as 5 calling student names or checking respective identification cards. There are not only disturbing the teaching process but also causes distraction for students during exam sessions. Apart from calling names, attendance sheet is passed around the classroom during the lecture sessions. The lecture class especially the class with a large number of students might find it difficult to have the attendance sheet being passed around the class. Thus, face recognition attendance system is proposed in order to replace the manual signing of the presence of students which are burdensome and causes students get distracted in order to sign for their attendance. Furthermore, the face recognition based automated student attendance system able to overcome the problem of fraudulent approach and lecturers does not have to count the number of students several times to ensure the presence of the students. 
The paper proposed by Zhao, W et al. (2003) has listed the difficulties of facial identification. One of the difficulties of facial identification is the identification between known and unknown images. In addition, paper proposed by Pooja G.R et al. (2010) found out that the training process for face recognition student attendance system is slow and time-consuming. In addition, the paper proposed by Priyanka Wagh et al. (2015) mentioned that different lighting and head poses are often the problems that could degrade the performance of face recognition based student attendance system. 

Hence, there is a need to develop a real time operating student attendance system which means the identification process must be done within defined time constraints to prevent omission. The extracted features from facial images which represent the identity of the students have to be consistent towards a change in background, illumination, pose and expression. High accuracy and fast computation time will be 6 the evaluation points of the performance

1.3 Aims and Objectives
 The objective of this project is to develop face recognition attendance system. Expected achievements in order to fulfill the objectives are:
 ● To detect the face segment from the video frame.
 ● To extract the useful features from the face detected.
 ● To classify the features in order to recognize the face detected.
To store data in Mysql DataBase
 ● To record the attendance of the identified student
1.4 Scope of the project
We are setting up to design a system comprising of two modules. The first module (face detector) is a mobile component, which is basically a camera application that captures student faces and stores them in a file using computer vision face detection algorithms and face extraction techniques. The second module is a desktop application that does face recognition of the captured images (faces) in the file, marks the students register and then stores the results in a database for future analysis.

2.1 Student Attendance System
Arun Katara et al. (2017) mentioned disadvantages of RFID (Radio Frequency Identification) card system, fingerprint system and iris recognition system. RFID card system is implemented due to its simplicity. However, the user tends to help their friends to check in as long as they have their friend’s ID card. The fingerprint system is indeed effective but not efficient because it takes time for the verification process so the user has to line up and perform the verification one by one. However for face recognition, the human face is always exposed and contain less information compared to iris. Iris recognition system which contains more detail might invade the privacy of the user. Voice recognition is available, but it is less accurate compared to other methods. Hence, face recognition system is suggested to be implemented in the student attendance system.

2.2 Digital Image Processing
Digital Image Processing is the processing of images which are digital in nature by a digital computer. Digital image processing techniques are motivated by three major applications mainly:
 ● Improvement of pictorial information for human perception.
● Image processing for autonomous machine application 
● Efficient storage and transmission.

2.3 Image Representation in a Digital Computer
An image is a 2-Dimensional light intensity function 
𝐟 (𝐱,𝐲) = 𝐫 (𝐱,𝐲) × 𝐢 (𝐱,𝐲) -(2.0) 
Where, r (x, y) is the reflectivity of the surface of the corresponding image point. i (x,y) Represents the intensity of the incident light. A digital image f(x, y) is discretized both in spatial co-ordinates by grids and in brightness by quantization. Effectively, the image can be represented as a matrix whose row, column indices specify a point in the image and the element value identifies gray level value at that point. These elements are referred to as pixels or pels. 
Typically following image processing applications, the image size which is used is𝟐𝟓𝟔 × 𝟐𝟓𝟔, elements, 𝟔𝟒𝟎 × 𝟒𝟖𝟎 pels or 𝟏𝟎𝟐𝟒 × 𝟏𝟎𝟐𝟒 pixels. Quantization of these matrix pixels is done at 8 bits for black and white images and 24 bits for colored images (because of the three color planes Red, Green and Blue each at 8 bits).
2.4 Steps in Digital Image Processing
 Digital image processing involves the following basic tasks:
 ● Image Acquisition - An imaging sensor and the capability to digitize the signal produced by the sensor.
● Preprocessing – Enhances the image quality, filtering, contrast enhancement etc. 
● Segmentation – Partitions an input image into constituent parts of objects. 12 
● Description/feature Selection – extracts the description of image objects suitable for further computer processing.
 ● Recognition and Interpretation – Assigning a label to the object based on the information provided by its descriptor. Interpretation assigns meaning to a set of labelled objects. 
● Knowledge Base – This helps for efficient processing as well as inter module cooperation.
2.5 Face Detection
 Face detection is the process of identifying and locating all the present faces in a single image or video regardless of their position, scale, orientation, age and expression. Furthermore, the detection should be irrespective of extraneous illumination conditions and the image and video content[5 ].
2.6 Face Recognition
Face Recognition is a visual pattern recognition problem, where the face, represented as a three dimensional object that is subject to varying illumination, pose and other factors, needs to be identified based on acquired images[6 ]. 
Face Recognition is therefore simply the task of identifying an already detected face as a known or unknown face and in more advanced cases telling exactly whose face it is[7 ]. 
2.7 Local Binary Pattern Histogram
Local Binary Pattern (LBP) is a simple yet very efficient texture operator which labels the pixels of an image by thresholding the neighborhood of each pixel and considers the result as a binary number.
 It was first described in 1994 (LBP) and has since been found to be a powerful feature for texture classification. It has further been determined that when LBP is combined with histograms of oriented gradients (HOG) descriptor, it improves the detection performance considerably on some datasets. Using the LBP combined with histograms we can represent the face images with a simple data vector.
2.8 LBPH algorithm work step by step: 
LBPH algorithm work in 5 steps. 
1. Parameters: the LBPH uses 4 parameters: 
● Radius: the radius is used to build the circular local binary pattern and represents the radius around the central pixel. It is usually set to 1. 
● Neighbors: the number of sample points to build the circular local binary pattern. Keep in mind: the more sample points you include, the higher the computational cost. It is usually set to 8. 
● Grid X: the number of cells in the horizontal direction. The more cells, the finer the grid, the higher the dimensionality of the resulting feature vector. It is usually set to 8. 17 
● Grid Y: the number of cells in the vertical direction. The more cells, the finer the grid, the higher the dimensionality of the resulting feature vector. It is usually set to 8.
 2. Training the Algorithm: First, we need to train the algorithm. To do so, we need to use a dataset with the facial images of the people we want to recognize. We need to also set an ID (it may be a number or the name of the person) for each image, so the algorithm will use this information to recognize an input image and give you an output. Images of the same person must have the same ID. With the training set already constructed, let’s see the LBPH computational steps. 
3. Applying the LBP operation: 
The first computational step of the LBPH is to create an intermediate image that describes the original image in a better way, by highlighting the facial characteristics. To do so, the algorithm uses a concept of a sliding window, based on the parameters radius and neighbors
 Based on the image above, let’s break it into several small steps so we can understand it easily: 
● Suppose we have a facial image in grayscale. 
● We can get part of this image as a window of 3x3 pixels. 
● It can also be represented as a 3x3 matrix containing the intensity of each pixel (0~255). 
● Then, we need to take the central value of the matrix to be used as the threshold. 
● This value will be used to define the new values from the 8 neighbors. 
● For each neighbor of the central value (threshold), we set a new binary value. We set 1 for values equal or higher than the threshold and 0 for values lower than the threshold. 
● Now, the matrix will contain only binary values (ignoring the central value). We need to concatenate each binary value from each position from the matrix line by line into a new binary value (e.g. 10001101). Note: some authors use other approaches to concatenate the binary values (e.g. clockwise direction), but the final result will be the same. 
● Then, we convert this binary value to a decimal value and set it to the central value of the matrix, which is actually a pixel from the original image.
 ● At the end of this procedure (LBP procedure), we have a new image which represents better the characteristics of the original image.
 
 It can be done by using bilinear interpolation. If some data point is between the pixels, it uses the values from the 4 nearest pixels (2x2) to estimate the 19 value of the new data point. 
4. Extracting the Histograms:
 Now, using the image generated in the last step, we can use the Grid X and Grid Y parameters to divide the image into multiple grids, as can be seen in the following image:
 
 Based on the image above, we can extract the histogram of each region as follows:
 ● As we have an image in grayscale, each histogram (from each grid) will contain only 256 positions (0~255) representing the occurrences of each pixel intensity. 
● Then, we need to concatenate each histogram to create a new and bigger histogram. Supposing we have 8x8 grids, we will have 8x8x256=16.384 positions in the final histogram. The final histogram represents the characteristics of the image original image. 
5. Performing the face recognition: 
In this step, the algorithm is already trained. Each histogram created is used to represent each image from the training dataset. So, given an input image, we perform the steps again for this new image and creates a histogram which represents the image. 20 
● So to find the image that matches the input image we just need to compare two histograms and return the image with the closest histogram. 
● We can use various approaches to compare the histograms (calculate the distance between two histograms), for example: Euclidean distance, chi-square, absolute value, etc. In this example, we can use the Euclidean distance (which is quite known) based on the following formula: 
 
● So the algorithm output is the ID from the image with the closest histogram. The algorithm should also return the calculated distance, which can be used as a ‘confidence’ measurement. 
● We can then use a threshold and the ‘confidence’ to automatically estimate if the algorithm has correctly recognized the image. We can assume that the algorithm has successfully recognized if the confidence is lower than the threshold defined
  
The main components used in the implementation approach are open source computer vision library (OpenCV). One of OpenCV’s goals is to provide a simpleto-use computer vision infrastructure that helps people build fairly sophisticated vision applications quickly. OpenCV library contains over 500 functions that span many areas in vision. The primary technology behind Face recognition is OpenCV. The user stands in front of the camera keeping a minimum distance of 50cm and his image is taken as an input. The frontal face is extracted from the image then converted to gray scale and stored. The Principal component Analysis (PCA) algorithm is performed on the images and the eigen values are stored in an xml file. When a user requests for recognition the frontal face is extracted from the captured video frame through the camera. The eigen value is re-calculated for the test face and it is matched with the stored data for the closest neighbour.
3.1 Design Requirements
 We used some tools to build the system. Without the help of these tools it would not be possible to make it done. Here we will discuss about the most important one.
Software Implementation: 
1. OpenCV: We used OpenCV 3 dependency for python 3. OpenCV is library where there are lots of image processing functions are available. This is very useful library for image processing. Even one can get expected outcome without writing a single code. The library is cross-platform and free for use under the open-source BSD license. Example of some supported functions are given bellow: 
● Derivation: Gradient/Laplacian computing, contours delimitation 
● Hough transforms: lines, segments, circles, and geometrical shapes detection 
● Histograms: computing, equalization, and object localization with back projection algorithm 
● Segmentation: thresholding, distance transform, foreground/background detection, watershed segmentation 
● Filtering: linear and nonlinear filters, morphological operations 
● Cascade detectors: detection of face, eye, car plates 
● Interest points: detection and matching 
● Video processing: optical flow, background subtraction, camshaft (object tracking) 
● Photography: panoramas realization, high definition imaging (HDR), image inpainting
We copied this script and place it on a directory on our raspberry pi and saved it. Then through terminal we made this script executable and then ran it.
Pip install opencv-python       this is for windows
2 Python IDE: 
There are lots of IDEs for python. Some of them are PyCharm, Thonny, Ninja, Spyder etc. Ninja and Spyder both are very excellent and free but we used Spyder as it feature- rich than ninja. Spyder is a little bit heavier than ninja but still much lighter than PyCharm and Visual Studio code. You can run them in pi and get GUI on your PC.
Install spyder/Visual studio code   this is for  windows/linux.
3.2 Update your system and remove programs to save space 
In this step, we will remove programs we don’t need and update our system. First, let’s set our Nano to use maximum power capacity: 
$ sudo nvpmodel -m 0 
$ sudo jetson_clocks 
The nvpmodel command handles two power options for your Jetson Nano: (1) 5W is mode 1 and (2) 10W is mode 0. The default is the higher wattage mode, but it is always best to force the mode before running the jetson_clocks command. 
After you have set your Nano for maximum power, go ahead and remove LibreOffice — it consumes lots of space, and we won’t need it for computer vision and deep learning: 
$ sudo apt-get purge libreoffice* 
$ sudo apt-get clean 
From there, let’s go ahead and update system level packages: 
$ sudo apt-get update && sudo apt-get upgrade 
In the next step, we’ll begin installing software.
3.3 Install OpenCV system-level dependencies and other development dependencies
 Let’s now install OpenCV dependecies on our system beginning with tools needed to build and compile OpenCV with parallelism: 
$ sudo apt-get install build-essential pkg-config
$ sudo apt-get install libtbb2 libtbb-dev 
Next, we’ll install a handful of codecs and image libraries:
 $ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
 $ sudo apt-get install libxvidcore-dev libavresample-dev
 $ sudo apt-get install libtiff-dev libjpeg-dev libpng-dev 
And then we’ll install a selection of GUI libraries:
 $ sudo apt-get install python-tk libgtk-3-dev 
$ sudo apt-get install libcanberra-gtk-module libcanberra-gtk3-module 
Lastly, we’ll install Video4Linux (V4L) so that we can work with USB webcams and install a library for FireWire cameras: 
$ sudo apt-get install libv4l-dev libdc1394-22-de




3.4 Set up Python virtual environments on your Jetson Nano
 
I can’t stress this enough: Python virtual environments are a best practice when both developing and deploying Python software projects.
 Virtual environments allow for isolated installs of different Python packages. When you use them, you could have one version of a Python library in one environment and another version in a separate, sequestered environment. 
In the remainder of this tutorial, we’ll create one such virtual environment; however, you can create multiple environments for your needs after you complete this Step#6. Be sure to read the RealPython guide on virtual environments if you aren’t familiar with them. 
First, we’ll install the de facto Python package management tool, pip: 
$ wget https://bootstrap.pypa.io/get-pip.py 
$ sudo python3 get-pip.py 
$ rm get-pip. 
And then we’ll install my favorite tools for managing virtual environments, virtualenv and virtualenvwrapper: 
$ sudo pip install virtualenv virtualenvwrapper 
The virtualenvwrapper tool is not fully installed until you add information to your bash profile. Go ahead and open up your ~/.bashrc with the nano ediitor: 
$ nano ~/.bashrc 
And then insert the following at the bottom of the file:
 # virtualenv and virtualenvwrapper export WORKON_HOME=$HOME/.virtualenvs 
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3 
source /usr/local/bin/virtualenvwrapper.sh 
Save and exit the file using the keyboard shortcuts shown at the bottom of the nano editor, and then load the bash profile to finish the virtualenvwrapper installation:
 $ source ~/.bashrc
3.5 Webcam
Specifications: 
• Logitech C270 Web Camera (960-000694) supports for NVIDIA jetson nano developer kit.
 
• The C270 HD Webcam gives you sharp, smooth conference calls (720p/30fps) in a widescreen format. Automatic light correction shows you in lifelike, natural colors. 
• Which is suitable to use with the NVIDIA Jetson Nano and NVIDIA Jetson Xavier NX Development Kits.

3.6 Experimental Results: 
The step of the experiments process are given below: Face Detection: Start capturing images through web camera of the client side: 

Begin: 
● Pre-process the captured image and extract face image 
● calculate the eigen value of the captured face image and compared with eigen values of existing faces in the database. 
● If eigen value does not matched with existing ones,save the new face image information to the face database (xml file). 
● If eigen value matched with existing one then recognition step will done.
End Face 

Recognition: 
Using PCA algorithm the following steps would be followed in for face recognition: 

Begin
● Find the face information of matched face image in from the database. 
● update the log table with corresponding face image and system time that makes completion of attendance for an individua students. 
End

A project work plan allows you to outline the requirements of a project, project planning steps, goals, and team members involved in the project. Within each goal, you're going to outline the necessary Key Action Steps in project planning, the requirements, and who's involved in each action step. 

Key Action Step: 
● Expected Outcome -Add this as a task. The Expected outcome will be the part of Project
● Assignees – Assigning the work to the team members.
● Completion Date -Add a due date and tries to finish the work within the time 

5.2 Work Breakdown Structure:
 In order to develop this system, we gave enormous importance to scheduling because we believed if we want to provide the best of quality in a given period of time then we must give due importance to scheduling which also helped us to achieve a better results.we observe the entire work structure, meaning how the scheduling was maintained throughout the developmental phase. We shall also see the financial foundation of this project and furthermore the feasibility study should be also discussed.
Month	Activity	Status

January	Selection of project area and Study of the related work.
Literature Survey and Study of Journals related to the work	Completed
January	Study on the software implementation works python and image processing.
Study of project related works like face recognition and detection techniques	Completed
February	Study of the Image processing in python and Open Computer Vision	Completed
February	Study of hardware and selection of components	Completed
March	Study of hardware implementation and installation OS	Completed
April	Study related to creating the environments and working platform
Study of packages/tools and installation of packages	Completed
May	Implementation of algorithm in Software.	Completed

We conducted a series of experiments to illustrate the system performance under different situations. By carrying out those tests, we were able to get the graph shown above (Distance vs Confidence Level). We may deduce from the graph that when the face is closer to the camera, the confidence level is higher, and vice versa. Therefore, by keeping a threshold for confidence level, we can mark attendance to the person according to the threshold. 

Analysis:
Here we consider one constant parameter intensity of light . we performed different experiments on different distance and different angles. we observed the confidence level at the different positions by gradually increasing the distance .we plotted the graph using the x and y coordinates by considering the x values as the confidence level or accuracy rate. and y values as the distance (cms).
