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
        img_array = np.fromfile(image_path, np.uint8)
        image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        image = cv2.resize(image, dsize=(128, 128), interpolation=cv2.INTER_AREA)
        
        reshaped_image = image.reshape(3,128,128) #reshape
        # cv2.imshow('image',image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        reshaped_image_list.append(reshaped_image)
        cnt += 1
        if cnt %100 == 0:
            print(f"{cnt*100/len(series):.2f} %")
    return reshaped_image_list




path = "E:/!data/유형별 두피 이미지/data/label/모낭사이홍반/*/*.json"

path_list = glob.glob(path)

print(len(path_list))

image_path = []
target = []

root_path = "E:/!data/유형별 두피 이미지/data/data/모낭사이홍반"

cnt = 0

for p in path_list:
    with open(p, 'r',encoding="UTF-8") as file:
        data = json.load(file)
        data_path = data['image_file_name']
        value = data["value_3"]
        image_path.append(root_path + "/" + value + "/" + data_path)
        target.append(value)
        cnt += 1
    if cnt %1000 == 0:
        print(f"{cnt*100/len(path_list):.2f}%")

print(len(image_path))
print(len(target))





reshaped_image_list = get_img_list(image_path)
print(len(reshaped_image_list))
reshaped_image_list_n = np.array(reshaped_image_list)

np.save('../data2/target', np.array(target))
np.save('../data2/ImageData',reshaped_image_list_n)

# with gzip.open('ImageData.pickle', 'wb') as f:
#     pickle.dump(reshaped_image_list, f)


# # to define
# file_path_l = []

# data = get_img_list(file_path_l)

