import cv2
import numpy as np


video_path = "tez.mp4"



class PoligonDrawer:
    def __init__(self):
        self.polygon_coordinates = []
        cv2.namedWindow('ROI')
        cv2.setMouseCallback('ROI', self.mouse_callback)

    def mouse_callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE:
            print("Curren coordinates", x,y)
        elif event == cv2.EVENT_LBUTTONDOWN:
            # Left click
            print(f"""[{x}, {y}] saved to polygon list""")
            self.polygon_coordinates.append([x, y])

    def main(self):

        video_cap=cv2.VideoCapture(video_path)

        counter = 0
        while video_cap.isOpened():
            ret,frame=video_cap.read()
            if ret:
                if len(self.polygon_coordinates) > 1:
                    points = np.array([self.polygon_coordinates])
                    cv2.polylines(frame, np.int32([points]), True, (0,0,255),3)

                cv2.imshow("ROI",frame)

                if cv2.waitKey(120) == ord('q'):
                    break
            else:
                break
        

        video_cap.release()
        cv2.destroyAllWindows()

        print("final coordinates\n", self.polygon_coordinates)

if __name__ == "__main__":
    pd = PoligonDrawer()
    pd.main()
