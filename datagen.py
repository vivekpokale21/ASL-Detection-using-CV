#we simply record an approximately 3.3 second video at 30fps for each hand gesture and capture each frame
#(out of 100 total frames in one video) as an image, we are automatically supplied with a
#hundred still images for each letter in the American Sign Language.

import os
import cv2

data_directory = './data'
if not os.path.exists(data_directory):
    os.makedirs(data_directory)

num_classes = 24
dataset_size = 100

cap = cv2.VideoCapture(0)
for j in range(num_classes):
    if not os.path.exists(os.path.join(data_directory, str(j))):
        os.makedirs(os.path.join(data_directory, str(j)))

    print('Collecting data for class {}'.format(j))

    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(data_directory, str(j), '{}.jpg'.format(counter)), frame)

        counter += 1

cap.release()
cv2.destroyAllWindows()