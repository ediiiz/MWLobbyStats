import os
import sys

import requests
# If you are using a Jupyter notebook, uncomment the following line.
# %matplotlib inline
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
from io import BytesIO
import json



# Add your Computer Vision subscription key and endpoint to your environment variables.

subscription_key = ""

endpoint = "https://westeurope.api.cognitive.microsoft.com/"

ocr_url = endpoint + "vision/v2.1/ocr"

# Set image_url to the URL of an image that you want to analyze.
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/" + \
            "Atomist_quote_from_Democritus.png/338px-Atomist_quote_from_Democritus.png"
src_path = r"C:/Users/Ediz/PycharmProjects/OCR/"

def ocr(image):

    image_path = image

    # data = {'url': image_url}
    # headers = {'Ocp-Apim-Subscription-Key': subscription_key}
    # response = requests.post(ocr_url, headers=headers, params=params, json=data)

    headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
    params = {'language': 'unk', 'detectOrientation': 'true'}

    image_data = open(image_path, "rb").read()
    print(image_data)
    response = requests.post(ocr_url, headers=headers, params=params, data=image_data)

    response.raise_for_status()

    analysis = response.json()

    # Extract the word bounding boxes and text.
    line_infos = [region["lines"] for region in analysis["regions"]]
    word_infos = []
    for line in line_infos:
          for word_metadata in line:
              for word_info in word_metadata["words"]:
                  word_infos.append(word_info)
    word_infos

    # Display the image and overlay it with the extracted text.
    plt.figure(figsize=(5, 5))
    image = Image.open(BytesIO(requests.get(image_url).content))
    ax = plt.imshow(image, alpha=0.5)
    for word in word_infos:
      bbox = [int(num) for num in word["boundingBox"].split(",")]
      text = word["text"]
      origin = (bbox[0], bbox[1])
      patch = Rectangle(origin, bbox[2], bbox[3],
                              fill=False, linewidth=2, color='y')
      ax.axes.add_patch(patch)
      plt.text(origin[0], origin[1], text, fontsize=20, weight="bold", va="top")
      plt.axis("off")

    print(json.dumps(analysis, indent=4))

    # Read the image into a byte array

    # Set Content-Type to octet-stream
    # headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
    # put the byte array into your post request
#ocr(image)