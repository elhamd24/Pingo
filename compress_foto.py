import PIL
from PIL import Image
import tkinter as tk
from tkinter.filedialog import *

file_path = askopenfilename()
img = PIL.Image.open(file_path)
myHeigth, myWidth = img.size

img = img.resize((myHeigth, myWidth) , PIL.Image.ANTIALIAS)
save_path = asksaveasfilename()
img.save(save_path+"_compressed.jpg")