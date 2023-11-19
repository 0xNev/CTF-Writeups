from websocket import create_connection
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

def calcArea():

    im_in = cv2.imread("image.png", cv2.IMREAD_GRAYSCALE)
    th, im_th = cv2.threshold(im_in, 220, 250, cv2.THRESH_BINARY_INV)
    im_floodfill = im_th.copy()
    h, w = im_th.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    cv2.floodFill(im_floodfill, mask, (0,0), 255)
    im_floodfill_inv = cv2.bitwise_not(im_floodfill)
    img = im_th | im_floodfill_inv
    #imagem = (255-im_out) 
    cv2.imwrite("image_filled.png", img)


    img = cv2.imread('image_filled.png')

    # convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # apply thresholding to convert the grayscale image to a binary image
    ret,thresh = cv2.threshold(gray,50,255,0)

    # find the contours
    contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
       area = cv2.contourArea(cnt)
       print()
       approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
       (x,y)=cnt[0,0]

       if len(approx) >= 5:
          img = cv2.drawContours(img, [approx], -1, (0,255,255), 3)
          cv2.putText(img, 'Polygon', (x, y),
    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

    if area / 400 < 1:
        return str(1)
    return str(area / 400)  


flag = None


while not flag:

    ws = create_connection("ws://172.86.96.174:8000/echo")
    ws.send("0")

    for x in range(100):
        try:
            print(ws.recv())
            image = ws.recv()

            if "vsctf" in str(image):
                flag = image
                break

            image = Image.open(BytesIO(image))
            image.save('image.png')
            print("Area: " + calcArea())
            
            ws.send(calcArea())
        except:
            print("Connection closed")
            break
    
print(flag)