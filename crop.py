import os, os.path
import cv2
import sys
import numpy as np


# 0:400 0:500
def crop(img, x, y, h, w):
    crop_img = img[y:y+h, x:x+w]
    return crop_img

def getMoments(img):
    grey_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image, contours, hierarchy = cv2.findContours(grey_scale,1 ,2)
    cnt = contours[0]
    return cv2.moments(cnt)

def getFileNames(path):
    f = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        f.extend(filenames)
        break
    return f

def loadImages(files):
    imgs = []
    for f in files:
        img = cv2.imread(f)
        imgs.append(img)
    return imgs

def main(args):
    if os.path.exists(args[1]):
        for img in loadImages(getFileNames(sys.argv[1])):
            crop_img = crop(img, 0, 0, 400, 500)
            cv2.imwrite(img+'_crop', crop_img)
        
if __name__ == "__main__":
    main(sys.argv)