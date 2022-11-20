from djitellopy import Tello
import time
import cv2
#new heights, 73 top row, 58 mid (inches rn), 43 bottom 10 inch gap
import cv2.aruco as aruco
try:
    tags={2,9,14,18,6,11,9,18,2,11,6,14,14,11,18,9,2,6} #lower x-> high x low y->high y
    popped={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}
    def findAruco(img,draw=True):
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        key=getattr(aruco,'DICT_ARUCO_ORIGINAL')
        arucoDict=aruco.Dictionary_get(key)
        arucoParam=aruco.DetectorParameters_create()
        bbox,ids,_=aruco.detectMarkers(gray,arucoDict,parameters=arucoParam)
        #print(ids)
        if draw:
            aruco.drawDetectedMarkers(img,bbox)
        return bbox,ids
    def go_to_height(n):
        m=tello.get_height()
        time.sleep(1)
        tello.go_xyz_speed(0,0,n-m,30)
    def kill():
        tello.go_xyz_speed(-100,0,0,100)
        tello.go_xyz_speed(140,0,0,100)
        tello.go_xyz_speed(-20,0,0,100)
    def snake(a,b,c):
        go_to_height(190)
        time.sleep(2)
        tello.move_forward(270)
        detection=False
        for y in range(100):
            cv2.imwrite("droneread.png",frame_read.frame)
            img=cv2.imread("droneread.png")
            img=cv2.resize(img,(0,0),fx=0.4,fy=0.4)
            bbox,ids=findAruco(img)
            cv2.imshow("img",img)
            if (ids==a or ids==b or ids==c):
                print("located id of",ids)
                detection=True
                break
        if detection:
            kill()
                
        
        time.sleep(1)
        for y in range(5):
            tello.move_left(25)
            print("y:",y)
            #while True:

            detection=False
            for y in range(100):
                cv2.imwrite("droneread.png",frame_read.frame)
                img=cv2.imread("droneread.png")
                img=cv2.resize(img,(0,0),fx=0.4,fy=0.4)
                bbox,ids=findAruco(img)
                cv2.imshow("img",img)
                if (ids==a or ids==b or ids==c):
                    print("located id of",ids)
                    detection=True
                    break
            if detection:
                kill()

            time.sleep(1)
        go_to_height(200)
        time.sleep(1)
        go_to_height(147)
        detection=False
        for y in range(100):
            cv2.imwrite("droneread.png",frame_read.frame)
            img=cv2.imread("droneread.png")
            img=cv2.resize(img,(0,0),fx=0.4,fy=0.4)
            bbox,ids=findAruco(img)
            cv2.imshow("img",img)
            if (ids==a or ids==b or ids==c):
                print("located id of",ids)
                detection=True
                break
        if detection:
            kill()

        for y in range(5):
            tello.move_right(25)
            for y in range(100):
                cv2.imwrite("droneread.png",frame_read.frame)
                img=cv2.imread("droneread.png")
                img=cv2.resize(img,(0,0),fx=0.4,fy=0.4)
                bbox,ids=findAruco(img)
                cv2.imshow("img",img)
                if (ids==a or ids==b or ids==c):
                    print("located id of",ids)
                    detection=True
                    break
            if detection:
                kill()

            time.sleep(1)
        go_to_height(200)
        time.sleep(1)
        go_to_height(109)
        detection=False
        for y in range(100):
            cv2.imwrite("droneread.png",frame_read.frame)
            img=cv2.imread("droneread.png")
            img=cv2.resize(img,(0,0),fx=0.4,fy=0.4)
            bbox,ids=findAruco(img)
            cv2.imshow("img",img)
            if (ids==a or ids==b or ids==c):
                print("located id of",ids)
                detection=True
                break
        if detection:
            kill()
        for y in range(5):
            tello.move_left(25)
            print("y:",y)
            #while True:

            for y in range(100):
                cv2.imwrite("droneread.png",frame_read.frame)
                img=cv2.imread("droneread.png")
                img=cv2.resize(img,(0,0),fx=0.4,fy=0.4)
                bbox,ids=findAruco(img)
                cv2.imshow("img",img)
                if (ids==a or ids==b or ids==c):
                    print("located id of",ids)
                    detection=True
                    break
            if detection:
                kill()

            time.sleep(1)
            
                
    
                
#112 ,145, 165             
    tello=Tello()
    tello.connect()
    tello.streamon()
    frame_read=tello.get_frame_read()
    print("battery:",tello.get_battery())
    tello.takeoff()
    x=int(input("input x"))
    y=int(input("input y"))
    z=int(input("input z"))
    time.sleep(2)
    snake(x,y,z)
    tello.land()
except:
    tello.land()
