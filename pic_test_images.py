import os
import cv2
from PIL import Image

data_dir = 'Pictures/train/no/'


files = [f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f))]
for f in files:
	if f[0] == '.': continue

	print f
	img = Image.open(os.path.join(data_dir, f))
	img.load()