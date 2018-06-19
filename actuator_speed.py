import cv2

counter = 0
frame1 = 0
frame2 = 0
distance = 15.5 # inches
framerate = 239.63 # frames/second

cap = cv2.VideoCapture('C:/Users/Jeff/Desktop/drawings/IMG_9629.mov')

while cap.isOpened():
    ret, frame = cap.read()

    frame = cv2.putText(frame, text=str(counter), org=(150, 150), fontFace= cv2.FONT_HERSHEY_PLAIN, fontScale=10, color=(255,255,255))

    cv2.imshow('frame', frame)

    counter += 1

    test = cv2.waitKey(100)

    if test == ord('e'):
        if frame1 == 0:
            frame1 = counter
            print('Start motion at frame %d' % counter)
        elif frame2 == 0:
            frame2 = counter
            print('End motion at frame %d' % counter)
    elif test == ord('q'):
        break

cap.release()

time = (frame2 - frame1) / framerate    # seconds
speed = distance/time                   # inches / second
print('Speed is %d in/s' % speed)