import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
from keras.models import load_model
import cv2
import numpy as np

new_data_dir = 'Pictures/new/'
predicted_data_dir = 'Pictures/predicted/'
MOVE = True
img_width, img_height = 200, 200




model = load_model('model.h5')
model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

def predict_image(name):
	img = cv2.imread(new_data_dir + name)
	if img is None: return False
	img = cv2.resize(img,(img_width, img_height))
	img = np.reshape(img,[1, img_width, img_height, 3])
	return model.predict(img)[0][0]

# for every image in /new
files = [f for f in os.listdir(new_data_dir) if os.path.isfile(os.path.join(new_data_dir, f))]
for f in files:
	if f[0] == '.': continue

	prediction = predict_image(f)
	if prediction < 0.5:
		print f + ' --> no'
		if MOVE: os.rename(os.path.join(new_data_dir, f), os.path.join(predicted_data_dir + 'no/', f))
	else:
		print f + ' --> yes'
		if MOVE: os.rename(os.path.join(new_data_dir, f), os.path.join(predicted_data_dir + 'yes/', f))


# if class = 0 -> /no, else /yes
