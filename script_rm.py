import numpy as np
import torch
import torch.nn.functional as F
from cv2 import imread
from PIL import Image
from transformers import AutoModelForImageSegmentation
from utilities import preprocess_image, postprocess_image

device = 'cpu'
if torch.cuda.is_available(): #Если есть CUDA
    device = 'cuda' #Используем GPU
#Загружаем модель
model = AutoModelForImageSegmentation.from_pretrained("briaai/RMBG-1.4",trust_remote_code=True) #Загружаем модель
model.to(device) #CPU или GPU


def remove_bg(img_name): #Название картинки (с расширением)   
    img_docs = 'static/downlds/' #Директория с картинками

    model_input_size = [1024, 1024]
    orig_im = imread(img_docs + img_name)
    orig_im_size = orig_im.shape[0:2]
    image = preprocess_image(orig_im, model_input_size).to(device)

    result=model(image)

    result_image = postprocess_image(result[0][0], orig_im_size)

    #Сохранение результата
    pil_im = Image.fromarray(result_image)
    no_bg_image = Image.new("RGBA", pil_im.size, (0,0,0,0))
    orig_image = Image.open(img_docs + img_name)
    no_bg_image.paste(orig_image, mask=pil_im)

    #При сохранении расширение должно быть обязательно .png
    #Новое название
    img_name = "".join(img_name.split(".")[:-1]) + "_no_bg.png" 
    no_bg_image.save(f"static/ready_img/{img_name}")

    return f"static/ready_img/{img_name}" #Возвращаем путь до картинки


