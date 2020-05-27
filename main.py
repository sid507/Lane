import numpy as np
import cv2
import tkinter as tk
root=tk.Tk()

def value():
    global imaging
    imaging=e1.get()
    root.destroy()
    
    


def counter1( counter):
    if counter>0:
        counter=counter-1
    messageVar.config(text=str(counter))
    master.after(1000,lambda:counter1(counter))
    if(counter==5):
        changecolor('red')
    elif(counter==1):
        changecolor('red')
##        master.destroy()
def changecolor(current):
    current=messageVar.cget('bg')
    if current=='green':
        n='orange'
    elif current=='orange':
        n='red'
    messageVar.config(bg=n)
##    master.after(1000,lambda:changecolor(current))
tk.Label(root, text='City1').grid(row=0) 

e1 = tk.Entry(root)
e1.grid(row=0, column=1)
tk.Button(root, text='Show', command=value).grid(row=3, column=1, 
                                                                   sticky=tk.W, 
                                                                  pady=4)

root.mainloop()
img= cv2.imread(imaging)
ii=cv2.imread(imaging)
img=cv2.resize(img,(1918,969),interpolation=cv2.INTER_LINEAR)
ii=cv2.resize(ii,(1918,969),interpolation=cv2.INTER_LINEAR)

r,c,w=img.shape
print(r,c)
for i in range(r):
    for j in range(c):
        ii[i][j]=0
for i in range(800):
    for j in range(c):
        ii[130+i][j]=255


            
p=cv2.bitwise_and(ii,img)
img2=cv2.resize(p,(1000,600),interpolation=cv2.INTER_LINEAR)
def nothing(x):
    print(x)
##    cv2.imshow('oo',img2)
##    cv2.namedWindow('image')
##    cv2.namedWindow('image2')

img = np.zeros((1000,600,3),np.uint8)
cv2.createTrackbar('HLOW','image',0,255,nothing)
cv2.createTrackbar('S_LOW','image',0,255,nothing)
cv2.createTrackbar('V_LOW','image',0,255,nothing)
cv2.createTrackbar('H_HIGH','image2',0,255,nothing)
cv2.createTrackbar('S_HIGH','image2',0,255,nothing)
cv2.createTrackbar('V_HIGH','image2',0,255,nothing)



frame = cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)
HLOW = cv2.getTrackbarPos('HLOW','image')
S_LOW= cv2.getTrackbarPos('S_LOW','image')
V_LOW= cv2.getTrackbarPos('V_LOW','image')
H_HIGH= cv2.getTrackbarPos('H_HIGH','image2')
S_HIGH= cv2.getTrackbarPos('S_HIGH','image2')
V_HIGH= cv2.getTrackbarPos('V_HIGH','image2')
                    
lower = np.array([HLOW,S_LOW,V_LOW])
upper = np.array([178,65,151])

mask = cv2.inRange(frame,lower,upper)
cv2.imshow('e',mask)
res = cv2.bitwise_and(img2,img2,mask=mask)
res1=cv2.Canny(res,150,150)
cv2.line(mask,(0,0),(0,1918),(255,255,255),4)
cv2.line(mask,(0,0),(969,0),(255,255,255),4)
cv2.line(mask,(0,600),(1000,600),(255,255,255),4)
cv2.line(mask,(1000,0),(1000,600),(255,255,255),4)
mask=cv2.bitwise_not(mask)
cv2.imshow('jf',mask)
area=0
c,h= cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img2,c,-1,(0,255,255),1)
for j in range(len(c)):
    area = area + cv2.contourArea(c[j])
r,c=mask.shape
##    print(r,c,area)
    ##area=area-600000
density=area/float(6000)
cv2.imshow('im',mask)
print(density)
if density>19:
    text='Traffic is Max : Time duration=35'
    time =35
elif density>15 and density<19:
    text='Traffic is Moderate : Time duration=25'
    time=25
else:
    text='Traffic is Low : Time duration=15'
    time=15
##    cv2.imshow('image2',mask)
##    cv2.imshow('ima',img2)
counter=time
current='green'
master=tk.Tk()

messageVar=tk.Message(master,text=counter,bg=current,width=50)
messageVar.pack()
##changecolor(current)
counter1(counter)
master.mainloop()
    
if cv2.waitKey(1) & 0xFF ==ord('q'):
    cv2.destroyAllWindows()
      





    


    

    
