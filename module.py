import cv2

class FaceDetection:

    # Class Attribute
    model_path = "haarcascade_frontalface_default.xml"

    # Instance Attribute
    def __init__(self, video): # webcam, video
        if video == '0':
            self.video = int(video)
        else:
            self.video = video 

    # Load the Model
    def load_model(self):
        model = cv2.CascadeClassifier(self.model_path)
        return model

    # Load the Video
    def load_video(self, model):
        source = cv2.VideoCapture(self.video)
        while True:
            ret, frame = source.read()
            if ret:
                results = model.detectMultiScale(frame, 1.3, 4)
                
                if len(results) >= 1:
                    for coordinates in results:
                        x, y, w, h = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
                print(results)

                cv2.imshow("window", frame)
                if cv2.waitKey(30) & 0xFF == ord('q'):
                    break
            else:
                break
        cv2.destroyAllWindows()
        source.release()

    
    def run(self):
        model = self.load_model()
        self.load_video(model)
        
