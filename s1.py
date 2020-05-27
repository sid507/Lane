##import cv2
##import numpy as np
##def mouse(event,x,y,flags,params):
##    if event==cv2.EVENT_LBUTTONDOWN:
##        print(x,y)
##img=cv2.imread('final.png')
##r,c,p=img.shape

##cv2.namedWindow('frame')
##cv2.setMouseCallback('frame',mouse)
##mask2=cv2.bitwise_and(img,img,mask=mask2)
##cv2.imshow('frame',mask2)
import numpy as np
import cv2
import array
import tkinter as tk
global img
global arr
arr=array.array('i',[])


##cv2.imshow('f',img)
def mouse(event ,x,y,flags,params):
    
    if event==cv2.EVENT_LBUTTONDOWN:
        arr.append(x)
        arr.append(y)
        print(x,y)
        for i in range(len(arr)//2):
            cv2.rectangle(img,(arr[2*i],arr[2*i+1]),(arr[2*i]+50,arr[2*i+1]+25),(255,0,0),-1)
        
cv2.namedWindow('frame')
cv2.setMouseCallback('frame',mouse)

tt=2
while True:

    img=cv2.imread('final.png')
    img2=cv2.imread('final.png')
##    _,th=cv2.threshold(img,127,255,0)
    
    r,c,z=img.shape

    mask1=np.zeros((r,c),np.uint8)
    mask2=np.zeros((r,c),np.uint8)
    mask3=np.zeros((r,c),np.uint8)
    mask4=np.zeros((r,c),np.uint8)
    for i in range(176,308):
        for j in range(556):
            mask1[i][j]=255
            mask3[i][j]=255
    for i in range(320,440):
        for j in range(840,c):
            mask2[i][j]=255
            mask4[i][j]=255
    
    

    


    ##moving the block
    time=0
    while True:
        cv2.imshow('frame',img)
        img=img2.copy()
        for i in range(len(arr)//2):
            cv2.rectangle(img,(arr[2*i],arr[2*i+1]),(arr[2*i]+50,arr[2*i+1]+25),(255,0,0),-1)
        if tt-time>0.5:
            cv2.circle(img,(884,149),8,(0,255,0),-1)
            cv2.circle(img,(532,478),8,(0,0,255),-1)
        elif tt-time<=0.5 and tt-time>0:
            cv2.circle(img,(884,149),8,(0,165,255),-1)
            cv2.circle(img,(532,478),8,(0,165,255),-1)
        cv2.waitKey(10)
        time=time+0.01
        
        for i in range(len(arr)-1):
            if(arr[i+1]>176 and arr[i+1]<315 and i%2==0):
                x=arr[i]
                arr[i]=x+2
            elif arr[i+1]>316 and arr[i+1]<440 and i%2==0:
                x=arr[i]
                arr[i]=x-2
        if time>tt:
            break
    im=cv2.bitwise_and(img,img,mask=mask1)
    im=cv2.bitwise_not(im)
    im=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    _,th=cv2.threshold(im,160,255,cv2.THRESH_BINARY)
    th=cv2.bitwise_and(th,th,mask=(mask3))
    mask3,contour=cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img,mask3,-1,(0,255,0),3)
    
    area1=0
    for j in range(len(mask3)):
        area1=area1+cv2.contourArea(mask3[j])
    density1=area1/733
    im=cv2.bitwise_and(img,img,mask=mask2)
    im=cv2.bitwise_not(im)
    im=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    _,th=cv2.threshold(im,160,255,cv2.THRESH_BINARY)
    th=cv2.bitwise_and(th,th,mask=(mask4))
    mask4,contour=cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img,mask4,-1,(0,255,0),3)
    
    area2=0
    for j in range(len(mask4)):
        area2=area2+cv2.contourArea(mask4[j])
    density2=area2/733
    print(density2)
##    cv2.imshow('frame',th)
    if(density1<density2):
        density1=density2
    density1=(density1*100)/733
    print("density")
    print(density1)
    if(density1>0.9):
        cv2.waitKey(3000)
    elif(density1>0.5 and density1<0.9):
        cv2.waitKey(2000)
    else:
        cv2.waitKey(400)
        
    



    ##taking the cars before zebra crossing
    ar=array.array('i',[])
    ar2=array.array('i',[])
    for i in range(len(arr)-1):
        if arr[i]>441 and arr[i+1]>176 and arr[i+1]<308 and i%2==0:
            ar.append(arr[i])
            ar.append(arr[i+1])
        elif arr[i]<840 and arr[i+1]>320 and arr[i+1]<440 and i%2==0:
            ar2.append(arr[i])
            ar2.append(arr[i+1])
    for i in range(len(ar)):
        p=ar[i]
        arr.remove(ar[i])
    for i in range(len(ar2)):
        p=ar2[i]
        arr.remove(ar2[i])
    img=cv2.imread('final.png')
    for i in range(len(arr)//2):
            cv2.rectangle(img,(arr[2*i],arr[2*i+1]),(arr[2*i]+50,arr[2*i+1]+25),(255,0,0),-1)
    cv2.circle(img,(884,149),8,(0,0,255),-1)
    cv2.circle(img,(532,478),8,(0,255,0),-1)
    ima=img.copy()
    ##the cars before zebra crossing is in "ima"
    
    
    

    ##moving block after the zebracrossing
    time=0
    p=array.array('i',[])
    p1=array.array('i',[])
    p.append(597)
    p.append(63)
    p.append(658)
    p.append(72)
    p.append(570)
    p.append(19)
    p1.append(726)
    p1.append(535)
    p1.append(812)
    p1.append(533)
    p1.append(698)
    p1.append(639)
    while True:
        cv2.imshow('frame',img)
        img=ima.copy()
        for i in range(len(p)//2):
            cv2.rectangle(img,(p[2*i],p[2*i+1]),(p[2*i]+25,p[2*i+1]+50),(255,0,255),-1)
            cv2.rectangle(img,(p1[2*i],p1[2*i+1]),(p1[2*i]+25,p1[2*i+1]+50),(255,0,90),-1)
        for i in range(len(ar)//2):
            cv2.rectangle(img,(ar[2*i],ar[2*i+1]),(ar[2*i]+50,ar[2*i+1]+25),(255,0,0),-1)
        for i in range(len(ar2)//2):
            cv2.rectangle(img,(ar2[2*i],ar2[2*i+1]),(ar2[2*i]+50,ar2[2*i+1]+25),(255,0,0),-1)
        time=time+0.01
        cv2.waitKey(10)
        if(time>1.5):
            for i in range(len(p)):
                if(i%2!=0):
                    p[i]=p[i]+4
                    p1[i]=p1[i]-4
            
        for i in range(len(ar)):
            if(i%2==0):
                x=ar[i]
                ar[i]=x+2
        for i in range(len(ar2)):
            if(i%2==0):
                x=ar2[i]
                ar2[i]=x-2
##        print(time)
        
        if(time>4):
            break
        
##cv2.destroyAllWindows()
