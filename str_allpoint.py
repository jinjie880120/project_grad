from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import cv2
import numpy as np
f=open("perform.txt","r",encoding="utf-8")
word=f.read()
word=word.strip('\n')

maxpoint=0
num=1
for i in range(len(word)):
  str2D="./str_2D/"+str(num)+".txt"
  fs=open(str2D,"w")
  font = ImageFont.truetype("蒙纳繁方点阵.otf",600)
  img=Image.new("RGBA", (600,600),(0,0,0))
  draw = ImageDraw.Draw(img)
  draw.text((0, 0),word[i],(255,255,255),font=font)
  print("處理: %s" % word[i])
  draw = ImageDraw.Draw(img)
  img.save("tmp.png")
  img = cv2.imread("tmp.png")
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
  contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
  centroid = img.copy()
  for c in contours:
    M = cv2.moments(c)

    cx = int(M["m10"]/M["m00"])
    cy = int(M["m01"]/M["m00"])

    cv2.circle(centroid, (cx, cy), 2, (0, 255, 0), -1)
    fs.write("%d, %d\n" %(cx,cy))
  print("共有 %d 個點" % len(contours))
  maxpoint=max(maxpoint,len(contours))
  
  num+=1
  fs.close()
maxpoint=str(maxpoint)
fm=open("max.txt","w")
fm.write(maxpoint)
fm.close()
maxpoint=int(maxpoint)