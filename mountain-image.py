import cv2
import numpy as np

#to create plain black image
photo=np.zeros((1000,1000,3))

#to create circles
cv2.circle(photo, (500,70),30,(238,130,238),-1)
cv2.circle(photo, (250,250),70,(51,153,255),-1)
cv2.circle(photo, (250,250),30,(0,255,255),-1)
#cv2.circle(photo, (70,500),30,(250,250,250),-1)
cv2.circle(photo, (800,500),50,(102,0,204),-1)



#to create smaller mountain(triangle)
pts = np.array([[800,750],[1000,1000],[600,1000]])
pts = pts.reshape((-1,1,2))
cv2.polylines(photo,[pts],True,(0, 75, 150),10)
cv2.fillPoly(photo,[pts],(0, 75, 150))

#to create bigger mountain(triangle)
pts = np.array([[375,500],[0,1000],[750,1000]])
pts = pts.reshape((-1,1,2))
cv2.polylines(photo,[pts],True,(0,10,150),10)
cv2.fillPoly(photo,[pts],(0,10,150))

#to print and show image
cv2.imshow("Mountains",photo)
cv2.imwrite("Mountains.jpg",photo)
cv2.waitKey()
cv2.destroyAllWindows()
