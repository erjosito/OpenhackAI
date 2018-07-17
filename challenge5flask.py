import numpy as np
import os
import sys
import time
import math
import keras
from PIL import Image, ImageOps
from skimage import exposure
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.utils import np_utils
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
from keras import backend as K
from keras.models import load_model
from flask import Flask
from flask import request
from flask import jsonify
import struct
from urllib.request import urlopen
import tensorflow as tf
from tensorflow.python.client import device_lib
from keras import backend as K
import warnings

# Avoiding memory issues with the GPU
config = tf.ConfigProto()
#config = tf.ConfigProto(
#        device_count = {'GPU': 0}
#    )
config.gpu_options.allow_growth = True
#config.device_count={'GPU':0}
#config.gpu_options.per_process_gpu_memory_fraction=0.5
sess = tf.Session(config=config)
K.set_session(sess)

def pad_image(x): #image
    x.shape
    idealSize = 2**( math.floor(np.log2(max(x.shape[0], x.shape[1])))+1 )
    pad = x.shape[0] - x.shape[1]
    padX = idealSize - x.shape[0]
    padY = idealSize - x.shape[1]
    padx_before = padX//2
    padx_after=  idealSize - padx_before - x.shape[0]
    pady_before = padY//2
    pady_after = idealSize - pady_before - x.shape[1]
    newArr = np.pad(x, ((padx_before,padx_after),(pady_before,pady_after),(0,0)),mode='constant', constant_values=255)
    img = Image.fromarray(newArr, 'RGB')
    img2 = img.resize((128,128), Image.ANTIALIAS)
    return img2

def contrast_stretching(img): #img as image
    # Adaptive Equalization
    img_adapteq = exposure.equalize_adapthist(np.asarray(img), clip_limit=0.03)
    return img_adapteq

def preprocess_img(img):
    img1 = pad_image(img)
    img2 = contrast_stretching(img1)
    return img2

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify("Hello World!")


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
          #data = request.get_json()
          #img_data = float(data["image"])

          #data = struct.unpack(str(128*128*3)+'i', request)
          #img_data = np.array(data, dtype=np.float32 )

          #print('Reading JSON data...')
          #data = request.get_json()
          #print('Getting URL...')
          #img_url = str(data["image_url"])
          #img_url = request.args.get('image_url')

          img_url = str(request.data)
          img_url = img_url[2:-1]
          print('URL:', img_url)
          img_file = urlopen(img_url)
          img_data = plt.imread(img_file, 0)
          print('Preprocessing image...')
          img_data_preproc = preprocess_img(img_data)
          img_data_preproc = img_data_preproc.reshape(1, 128, 128, 3)
          print('Image shape:', img_data_preproc.shape)
          print('Predicting...')
          prediction_prob = model.predict(img_data_preproc, batch_size=8)
          print('Predicted probs:', prediction_prob)
          max_pred_index = np.argmax(prediction_prob)
          return jsonify(class_names[max_pred_index])
        except Exception as e:
          return jsonify(str(e))

label_list=['axes',
 'boots',
 'carabiners',
 'crampons',
 'gloves',
 'hardshell_jackets',
 'harnesses',
 'helmets',
 'insulated_jackets',
 'pulleys',
 'rope',
 'tents']
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    encoder = LabelEncoder().fit(y=label_list)
    class_names = [encoder.inverse_transform(i) for i in range(12)]
    #print(class_names)
#load an existing model
model_save_path='challenge4_9153.h5'
print('Loading model', model_save_path)
model = load_model(model_save_path)
print('Model loaded successfully')


app.run(host='0.0.0.0', debug=True, use_reloader=False)
