from module import *
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--video", type=str, required=True, help="Enter 0 for webcam of path for the video")

args = parser.parse_args()
video = args.video


pipeline = FaceDetection(video = video)
pipeline.run()