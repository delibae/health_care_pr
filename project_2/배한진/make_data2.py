import cv2
import numpy as np
import glob
import pickle
import gzip

import json

from matplotlib import pyplot as plt

from PIL import Image



path = "E:/!data/2.Validation/label/*/*/*.json"

path_list = glob.glob(path)

print(len(path_list))

image_path = []
dl_idx = []
dl_name = []
b_box = []
root_path = "E:/!data/2.Validation/data"

cnt = 0
# print(path_list[2])

for p in path_list:
    with open(p, 'r',encoding="UTF-8") as file:
        data = json.load(file)
        data_path = data['images'][0]['file_name']
        bbox = data["annotations"][0]["bbox"]
        if len(bbox) != 0:
            image_path.append(root_path + "/" + data_path.split('_')[0] + "/" + data_path)
            dl_idx.append(data['images'][0]["dl_idx"])
            dl_name.append(data['images'][0]["dl_name"])

            for i in range(len(bbox)):
                bbox[i] = bbox[i]-2
            b_box.append(bbox)
        cnt += 1
    if cnt %100 == 0:
        print(f"{cnt/len(path_list):.2f} %")


# print(image_path)
# print(dl_idx)
# print(dl_name)
# print(b_box)

dl_idx_n = []
dl_name_n = []

def get_img_list(series) :

    cnt = 0
    reshaped_image_list = []

    for i in range(len(series)) :
        try:
            image_path = series[i]
            image = cv2.imread(image_path, cv2.IMREAD_COLOR)
            bbox = b_box[i]
            # print(image_path)
            # print(bbox)
            image = Image.open(image_path)
            image = image.convert('RGB')
            

            left = bbox[0]
            right = bbox[0]+bbox[2]
            top = bbox[1]
            bottom = bbox[1] + bbox[3]
            image = image.crop((left, top, right, bottom))
            image = image.resize((128, 128))
            
            # image.show()
            
            image = np.array(image)
            
            
            # try:
            #     image = cv2.resize(image, dsize=(128, 128), interpolation=cv2.INTER_AREA)
            # except:
            #     try:
            #         image = image[bbox[1]+2:bbox[1]+bbox[3]+2,bbox[0]+2:bbox[0]+bbox[2]+2,:]
            #         image = cv2.resize(image, dsize=(128, 128), interpolation=cv2.INTER_AREA)
            #     except:
            #         image = image[bbox[1]+2:bbox[1]+bbox[3]+2,bbox[0]+2:bbox[0]+bbox[2]+2,:]
            #         image = cv2.resize(image, dsize=(128, 128), interpolation=cv2.INTER_AREA)
            
            reshaped_image_list.append(image)
            dl_idx_n.append(dl_idx[i])
            dl_name_n.append(dl_name[i])
        except:
            pass
        cnt += 1
        if cnt %100 == 0:
            print(f"{cnt/len(series):.2f} %")
    return reshaped_image_list



reshaped_image_list = get_img_list(image_path)

reshaped_image_list_n = np.array(reshaped_image_list)

print(len(dl_idx_n))
print(len(dl_name_n))
print(len(reshaped_image_list))

np.save('../data/dl_idx2', np.array(dl_idx_n))
np.save('../data/dl_name2',np.array(dl_name_n))
np.save('../data/ImageData2',reshaped_image_list_n)

# with gzip.open('ImageData.pickle', 'wb') as f:
#     pickle.dump(reshaped_image_list, f)


# # to define
# file_path_l = []

# data = get_img_list(file_path_l)

