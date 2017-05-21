import os
import cv2

data_dir = 'Pictures/new/'
train_data_dir = 'Pictures/train/'

files = [f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f))]
for f in files:
	if f[0] == '.': continue

	img = cv2.imread(os.path.join(data_dir, f))
	# img = cv2.resize(img, (250, 250))
	if img.shape[0] > 1000: 
		div = img.shape[0] / 1000.0
		img = cv2.resize(img,(int(img.shape[1] / div), int(img.shape[0] / div)))

	cv2.imshow('image', img)
	k = cv2.waitKey()
	
	if k == 27 or k == ord('q'): # Esc or 'q' key to stop
		break
	if k == ord('n'):
		os.rename(os.path.join(data_dir, f), os.path.join(train_data_dir + 'no/', f))
	if k == ord('y'):
		os.rename(os.path.join(data_dir, f), os.path.join(train_data_dir + 'yes/', f))