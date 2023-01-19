import torch
import torchvision

import torchvision.transforms as transforms
import os

from PIL import Image

import io

model = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_efficientnet_b4', pretrained= False)
model._modules['classifier']._modules['fc'].out_features = 4

model.load_state_dict(torch.load(os.path.dirname(os.path.abspath(__file__)) + '/nvidia_efficientnet_b4.pt'))

model.eval()


model_l = []

model_l.append(model)


def get_transform_te():
  transforms_test = transforms.Compose([
    transforms.ToTensor(),
    transforms.ToPILImage(),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize((0.4452, 0.4457, 0.4464), (0.2592, 0.2596, 0.2600)),
])
  return transforms_test


def image_processing(image_bytes):
    tr = get_transform_te()
    image = Image.open(io.BytesIO(image_bytes))
    out =  tr(image)
    out = out.unsqueeze(0)
    # print("---------",out.shape)
    return out



def predictall(image_bytes, val_n):
    # test_in = torch.randn(1,3,224,224)
    # outputs = model(test_in)
    
    # model_use = model_l[val_n]
    
    real_in = image_processing(image_bytes)
    outputs = model(real_in)
    
    

    _, predicted = torch.max(outputs.data, 1)
    
    return predicted.item()


