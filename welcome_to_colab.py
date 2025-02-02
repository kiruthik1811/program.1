from google.colab import files
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

imagePath = "/content/besiktas.png"
faceCascadePath = "/content/haarcascade_frontalface_default.xml"
eyeCascadePath = "/content/haarcascade_eye_tree_eyeglasses.xml"

img = np.array(Image.open(imagePath))
plt.imshow(img)
plt.axis('off')
plt.show()

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
faceCascade = cv2.CascadeClassifier(faceCascadePath)
eyeCascade = cv2.CascadeClassifier(eyeCascadePath)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
