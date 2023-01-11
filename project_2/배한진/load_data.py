import numpy as np

image_data_n = np.load('../data/ImageData.npy')
dl_idx  = np.load('../data/dl_idx.npy')
dl_name = np.load('../data/dl_name.npy')
print(image_data_n.shape)
print(len(dl_idx))
print(len(dl_name))
# import cv2

# from PIL import Image

# inp = image_data_n[0].reshape(128,128,3)
# show_img = Image.fromarray(inp)
