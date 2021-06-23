import cv2

def start_watching(name):
    print(f'Mila is watching you {name}')
    capture = cv2.VideoCapture(0)

    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if not(capture.isOpened()):
        print("Ayes are not opening")
    else:
        while(True):
            ret, frame = capture.read()
            if ret:
                cv2.imshow('I''m watching you', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        capture.release()
        cv2.destroyAllWindows();

if __name__ == '__main__':
    start_watching('Car owner')