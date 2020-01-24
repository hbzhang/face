from mtcnn import MTCNN
import cv2

axesLength = (20, 10)

angle = 0

startAngle = 0

endAngle = 360

color = (0, 255, 0)

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    #frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2GRAY)
    detector = MTCNN()
    print(detector.detect_faces(frame),"\n")

    result = detector.detect_faces(frame)

    if result is not None:
        if result.__len__() >0:
            result = result[0]

            box = result['box']

            cv2.rectangle(frame, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), (0,0,255),2)

            keypoints = result['keypoints']

            left_eye= keypoints["left_eye"]
            right_eye = keypoints["right_eye"]
            noses = keypoints["nose"]
            mouth_left=keypoints["mouth_left"]
            mouth_right=keypoints["mouth_right"]

            # Blue color in BGR
            color = (255, 0, 0)

            cv2.circle(frame, (keypoints['left_eye']), 2, (0, 155, 255), 2)
            cv2.circle(frame, (keypoints['right_eye']), 2, (0, 155, 255), 2)
            cv2.circle(frame, (keypoints['nose']), 2, (0, 155, 255), 2)
            cv2.circle(frame, (keypoints['mouth_left']), 2, (0, 155, 255), 2)
            cv2.circle(frame, (keypoints['mouth_right']), 2, (0, 155, 255), 2)


            #cv2.rectangle(frame,mouth_left,mouth_right, color, 2)

            #cv2.ellipse(frame, left_eye, axesLength,angle, startAngle, endAngle, color, 2)

            #cv2.ellipse(frame, right_eye, axesLength,
                        #angle, startAngle, endAngle, color, 2)

    cv2.imshow("Test", frame)
    key=cv2.waitKey(1)
    if key& 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()




