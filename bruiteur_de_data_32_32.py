# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 14:29:03 2023

@author: maxim
"""

import pickle
import random
import numpy as np
import matplotlib.pyplot as plt
import torch
from torch.utils.data import Dataset
#%%
class MyDataset(Dataset):
    def __init__(self, data, transform=None):
        self.data = data
        self.transform = transform

    def __len__(self):
        return len(self.data['data'])  

    def __getitem__(self, idx):
        image = self.data['data'][idx]
        label = self.data['labels'][idx]

        if self.transform:
            image = self.transform(image)

        return image, label
#%%Importation des données
def unpickle(file):
    with open(file, 'rb') as fo:
        data = pickle.load(fo, encoding='bytes')
    return data


file = "C:/Users/maxim/Desktop/Imagenet32_train/train_data_batch_1"
noisy_path="C:/Users/maxim/Desktop/IMI/TDLOG/Projet_TdLog/image_32_32_brouille/3/image"

loaded_data=unpickle(file)
my_dataset = MyDataset(data=loaded_data, transform=None)

#%%fontion brouillage
alpha=0.1
input_dim=32
def bruit(x):           
    for i in range(3):
        for j in range (input_dim):
            for h in range (input_dim):
                x[i][j][h]=(random.randint(0,255))*alpha+(1-alpha)*x[i][j][h]


image,_ = my_dataset.__getitem__(random.randint(0,10))
image=image.reshape(3,32,32)
print(image)
image = np.transpose(image, (1, 2, 0))
plt.imshow(image)
plt.show()  

image=image.reshape(3,32,32)
bruit(image)
from PIL import Image
image = Image.fromarray(image.transpose(1, 2, 0))
image.save(noisy_path)

#%%copie des images brouillées
u=7070
for k in range (7070,len(my_dataset)):
    image,_ = my_dataset.__getitem__(k)
    u+=1
    image=image.reshape(3,32,32)
    bruit(image)
    from PIL import Image
    image = Image.fromarray(image.transpose(1, 2, 0))
    image.save(noisy_path+f"{u}"+".png")
    