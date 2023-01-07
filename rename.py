# rename all files
import os

def rename_images(path):
    for i,filename in enumerate(os.listdir(path)):
        os.rename(f"{path}/{filename}",f"{path}/house_{str(i)}.jpg")

rename_images("houses")        