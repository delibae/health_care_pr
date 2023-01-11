import cv2
import numpy as np
import glob
import pickle
import gzip

import json

def get_img_list(series) :

    cnt = 0
    reshaped_image_list = []

    for file_name in series :
        image_path = file_name
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)

        image = cv2.resize(image, dsize=(128, 128), interpolation=cv2.INTER_AREA)
        
        # reshaped_image = image.reshape(128,128) #reshape
        # cv2.imshow('image',image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        reshaped_image_list.append(image)
        cnt += 1
        if cnt %100 == 0:
            print(f"{cnt/len(series):.2f} %")
    return reshaped_image_list




path = "E:/!data/label/json/*/*.json"

path_list = glob.glob(path)

print(len(path_list))

image_path = []
dl_idx = []
dl_name = []
root_path = "E:/!data/data/image"

cnt = 0

for p in path_list:
    with open(p, 'r',encoding="UTF-8") as file:
        data = json.load(file)
        data_path = data['images'][0]['file_name']
        image_path.append(root_path + "/" + data_path[:8] + "/" + data_path)
        dl_idx.append(data['images'][0]["dl_idx"])
        dl_name.append(data['images'][0]["dl_name"])
        cnt += 1
    if cnt %100 == 0:
        print(f"{cnt/len(path_list):.2f} %")
        
# print(image_path)
# print(dl_idx)
# print(dl_name)

reshaped_image_list = get_img_list(image_path)

reshaped_image_list_n = np.array(reshaped_image_list)

np.save('../data/dl_idx', np.array(dl_idx))
np.save('../data/dl_name',np.array(dl_name))
np.save('../data/ImageData',reshaped_image_list_n)

# with gzip.open('ImageData.pickle', 'wb') as f:
#     pickle.dump(reshaped_image_list, f)


# # to define
# file_path_l = []

# data = get_img_list(file_path_l)

