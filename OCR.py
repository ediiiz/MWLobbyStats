import cv2
import numpy as np
import re
import pytesseract
from PIL import Image
from PIL import ImageEnhance
import configparser

img_path = "./Images"

config = configparser.RawConfigParser()
config.read('./config.ini')
details_dict = dict(config.items('INI'))


pytesseract.pytesseract.tesseract_cmd = details_dict["tesseractexe"]
usernamesOCR = []


def remove_at(i, s):
    return s[:i] + s[i + 1:]

def get_string(img_path):
    img = Image.open(img_path)
    img = img.convert('RGBA')
    img = ImageEnhance.Contrast(img)
    contrast = 1.2
    img = img.enhance(contrast)
    img = ImageEnhance.Sharpness(img)
    sharpness = 0.8
    img = img.enhance(sharpness)
    size = img.size[0] * 3, img.size[1] * 3
    img = img.resize(size, Image.ADAPTIVE)
    #img = img.convert('RGBA')
    img = np.asarray(img)

    n = 865
    for v in range(0, 2):

        n
        x = 1920+1387
        h = 500
        w = 500
        imgview = img[n:n + h, x:x + w]
        y = 417
        n = 1820

        for c in range(0,6):
            y
            x = 0
            h = 83
            w = 500
            img2 = imgview[y:y + h, x:x + w]

            #cv2.imshow('Image', img2)
            #cv2.waitKey(0)

            #Convert to gray
            img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

            # Threshhold
            img2 = cv2.bitwise_not(img2)
            th, img2 = cv2.threshold(img2, 160, 255, cv2.THRESH_BINARY)

            # Apply dilation and erosion to remove some noise
            kernel = np.ones((3, 3), np.uint8)
            img2 = cv2.dilate(img2, kernel, iterations=1)
            img2 = cv2.erode(img2, kernel, iterations=1)

            # Write image after removed noise
            #cv2.imwrite(src_path + "removed_noise.png", img2)

            # Write the image after apply opencv to do some ...
            cv2.imwrite(img_path + "thres.png", img2)

            # Recognize text with tesseract for python
            data = pytesseract.image_to_data(Image.open(img_path + "thres.png"), output_type='data.frame')
            result = pytesseract.image_to_string(Image.open(img_path + "thres.png"))


            data = data[data.conf != -1]
            #lines = result.groupby('block_num')['text'].apply(list)
            conf = data.groupby(['block_num'])['conf'].mean()

            #print(result)
            #print(conf)

            # Text CleanUp
            resultclean = result.replace("J", "]")
            resultclean = resultclean.replace(")", "j")
            resultclean = resultclean.replace(" ", "%20")
            resultclean = re.sub("[\(\[].*?[\)\]]", "", resultclean)
            result = result.replace(" ", "%20")
            result = re.sub("[\(\[].*?[\)\]]", "", result)
            result = result.replace("]", "")
            if resultclean.find("]") == 0:
                if resultclean[0] == "]":
                    resultclean = remove_at(0, resultclean)
                    resultclean = resultclean.replace("]", "J")

            if result.find("]") == 0:
                if result[0] == "]":
                    result = remove_at(0, result)
                    result = result.replace("]", "J")




            #if result[1] == "]":
                #result = remove_at(0,result)





            # Remove template file
            # os.remove(temp)
            y = y - 83
            #cv2.imshow('Image', img2)
            #cv2.waitKey(0)
            if len(result) >= 1:
                #print(result)
                usernamesOCR.append(result)

            if len(resultclean) >= 1:
                #print(resultclean)
                usernamesOCR.append(resultclean)

    usernamesOCR.append("vvvvNextgame")


#get_string("./Images/savage.png")
#print(usernamesOCR)


