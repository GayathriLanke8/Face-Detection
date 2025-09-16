## Face Detection using [OpenCV](https://opencv.org/) and [Matplotlib](https://matplotlib.org/)  

This project demonstrates real-time **face detection** using the [OpenCV](https://opencv.org/) library. It captures video frames from a webcam (or video file), detects **frontal human faces**, and draws **rectangular bounding boxes** around each detected face. The processed frames are then displayed using [Matplotlib](https://matplotlib.org/).

### Model  
The Haar Cascade Frontal Face Detection model is a pre-trained classifier provided by OpenCV.  
It uses Haar-like features to quickly and accurately detect human faces in images or video frames.

The model is available in [this repository](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)

### Project Setup  
* Make an environment with python=3.10 using the following command 
```bash
 create -n facedetection python=3.12.11
```

* Activate the Environment using the following command
```bash
conda activate facedetection
```

* Install the project dependencies using the following command 
```bash
pip install -r requirements.txt
```

* Run the Python Script
```bash
python run.py
```

