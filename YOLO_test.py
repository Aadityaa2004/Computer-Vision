from ultralytics import YOLO 
import torch
import cv2
import numpy as np
import matplotlib.pyplot as plt

# creates a model from scratch 
model = YOLO("yolov8n.yaml")

# load a pretrained YOLO model (recomended for training)
model = YOLO("yolov8n.pt")

# train the model using the 'coco8.yaml' dataset for 3 epochs
results = model.train(data="coco8.yaml", epochs=3)

# evaluate the model's performance on the validation test 
 
