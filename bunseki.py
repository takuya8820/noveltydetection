# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 13:11:32 2019

@author: takuya
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:55:34 2018

@author: takuya
"""

import pickle
import sys
import os
import pdb
import matplotlib.pyplot as plt
from matplotlib import offsetbox
import numpy as np

if len(sys.argv) > 1:
	# noiseZ
    noisez = int(sys.argv[1])
	# noiseSigma
    if len(sys.argv) > 2:
        noiseSigma = int(sys.argv[2])
        if len(sys.argv) > 3:
            number = int(sys.argv[3])
            if len(sys.argv) > 4:
                trialNo = int(sys.argv[4])
                
        
  
targetChar = 2
jikkenPath3 = 'jikken3'


postFix = "{}_{}".format(targetChar, trialNo)

path1 = os.path.join(jikkenPath3,"noise{}_{}".format(noisez,noiseSigma))
path = os.path.join(path1,"log{}.pickle".format(postFix))
with open(path, "rb") as fp:
    batch_x = pickle.load(fp)
    batch_x_fake = pickle.load(fp)
    encoderR_batch_x_value = pickle.load(fp)
    encoderR_train_value = pickle.load(fp)
    decoderR_train_value = pickle.load(fp)
    encoderR_fake_train_value = pickle.load(fp)
    decoderR_fake_train_value = pickle.load(fp)
    predictFake_train_value = pickle.load(fp)
    predictTrue_train_value = pickle.load(fp)
    test_x = pickle.load(fp)
    test_y = pickle.load(fp)
    decoderR_test_value = pickle.load(fp)
    predictDX_value = pickle.load(fp)
    predictDRX_value = pickle.load(fp)
    recallDXs = pickle.load(fp)
    precisionDXs = pickle.load(fp)
    f1DXs = pickle.load(fp)
    recallDRXs = pickle.load(fp)
    precisionDRXs = pickle.load(fp)
    f1DRXs = pickle.load(fp)
    lossR_values = pickle.load(fp)
    lossRAll_values = pickle.load(fp)
    lossD_values = pickle.load(fp)
    params = pickle.load(fp)


def imscatter(x, y, image, ax=None, zoom=1):
    imagebox = offsetbox.OffsetImage(image, zoom=zoom)
    artists = []
    #for x0,y0 in zip(x,y):
    ab = offsetbox.AnnotationBbox(imagebox, (x,y), xycoords='data', frameon=False)
    artists.append(ax.add_artist(ab)) 
    return artists 





#NAFS異常データ
x1=encoderR_fake_train_value[:,0]
y1=encoderR_fake_train_value[:,1]

#ALOCC異常データ
x2=encoderR_train_value[:,0]
y2=encoderR_train_value[:,1]

#正常データ
x3=encoderR_batch_x_value[:,0]
y3=encoderR_batch_x_value[:,1]


fig, ax = plt.subplots()
plt.gray()

'''
for i in range(number):
    imscatter(encoderR_fake_train_value[i,0], encoderR_fake_train_value[i,1], decoderR_fake_train_value[i,:,:,0], ax=ax, zoom=0.5)
for i in range(number):
    imscatter(encoderR_train_value[i,0], encoderR_train_value[i,1], decoderR_train_value[i,:,:,0], ax=ax, zoom=0.5)
for i in range(number):
    imscatter(encoderR_batch_x_value[i,0], encoderR_batch_x_value[i,1], batch_x[i,:,:,0], ax=ax, zoom=0.5)


'''
imscatter(encoderR_fake_train_value[number,0], encoderR_fake_train_value[number,1], decoderR_fake_train_value[number,:,:,0], ax=ax, zoom=0.5)

imscatter(encoderR_train_value[number,0], encoderR_train_value[number,1], decoderR_train_value[number,:,:,0], ax=ax, zoom=0.5)

imscatter(encoderR_batch_x_value[number,0], encoderR_batch_x_value[number,1], batch_x[number,:,:,0], ax=ax, zoom=0.5)
    


ax.scatter(x1, y1, s=5, c="red")
ax.scatter(x2, y2, s=5, c="green")
ax.scatter(x3 ,y3, s=5, c="blue")
ax.autoscale() 

plt.show()