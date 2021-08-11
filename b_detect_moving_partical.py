import cv2
rec = cv2.VideoCapture('bmoving.mp4')
ret, frame1 = rec.read()
ret, frame2 = rec.read()
while(rec.isOpened()):
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 2)
    _, thres = cv2.threshold(blur, 20,255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thres, None, iterations=5)
    countour, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for con in countour:
        (x, y, w, h)= cv2.boundingRect(con)
        if cv2.contourArea(con)<500:
            continue
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (255,0,0), 3)
    cv2.imshow('moving', frame1)
    frame1=frame2
    ret, frame2= rec.read()
    if cv2.waitKey(200) == ord('q'):
        break
rec.release()
cv2.destroyAllWindows()