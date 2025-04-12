import cv2
import time
import os
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget

class SilentCameraApp(App):
    def build(self):
        return Widget()  # Trả về 1 Widget trống để không hiển thị gì cả

    def on_start(self):
        # Khi app khởi động, gọi hàm chụp ảnh
        Clock.schedule_once(self.capture_images, 0)

    def capture_images(self, *args):
        cap = cv2.VideoCapture(0)  # 0 = camera sau
        if not cap.isOpened():
            print("Không mở được camera")
            App.get_running_app().stop()
            return

        time.sleep(2)  # Đợi camera ổn định

        for i in range(1, 6):
            ret, frame = cap.read()
            if ret:
                filename = f'/sdcard/DCIM/Camera/opencv_photo_{i}.jpg'
                cv2.imwrite(filename, frame)
                print(f"Đã lưu ảnh: {filename}")
                time.sleep(1)  # Chờ 1 giây giữa mỗi lần chụp
            else:
                print("Chụp ảnh thất bại!")

        cap.release()
        print("Đã chụp xong 5 ảnh.")
        App.get_running_app().stop()  # Thoát app sau khi chụp xong

if __name__ == '__main__':
    SilentCameraApp().run()
