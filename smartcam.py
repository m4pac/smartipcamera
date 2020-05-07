import cv2
import time
import playsound

cap = cv2.VideoCapture('rtsp://username:password@ipaddress:port')

frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height =int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')

out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1280,720))

ret, frame1 = cap.read()
ret, frame2 = cap.read()

print(frame1.shape)

while cap.isOpened():
    scr = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(scr, cv2.COLOR_BGR2GRAY)
    gblur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(gblur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 900:
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame1, "Hareket Algilandi!", (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3)
        zmndamga = time.ctime()
        with open("log.txt","r+",encoding="utf8") as file:
            f=file.readlines()
            f.insert(0,"Log: {0}\n".format(zmndamga))
            file.seek(0)
            file.writelines(f)
            file.close()
            playsound.playsound('music.mp3',True) 
        
        #f = open("log.txt", "w")
        #f.write(f"Log: {zamandamga}\n")
        #f.close()
    image = cv2.resize(frame1, (1280,720))
    out.write(image)
    cv2.imshow("Canli - Cam1", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
