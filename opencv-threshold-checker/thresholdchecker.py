import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import cv2 
from matplotlib.widgets import Button
import imutils
import mpl_interactions.ipyplot as iplt
import ipywidgets as widgets



fig, ax = plt.subplots()
fig.figsize=(5,5)
# fig.canvas.manager.toolmanager.remove_tool("subplots")

plt.subplots_adjust(bottom=0.2)

img=cv2.imread('license_plate_2.jpg_0_plate.jpg')
ax.imshow(imutils.opencv2matplotlib(img))  

def add_gray_btn_on_clicked(event):
    img=cv2.imread('license_plate_3.jpg_0_plate.jpg')
    ax.imshow(imutils.opencv2matplotlib(img)) 


add_gray_btn = Button(plt.axes([0.1, 0.1, 0.2, 0.05]), 'add gray')
add_gray_btn.on_clicked(add_gray_btn_on_clicked)
add_thresh_btn = Button(plt.axes([0.1, 0.01, 0.2, 0.05]), 'add threshold')
add_thresh_btn.on_clicked(lambda event: print(event))



plt.show()