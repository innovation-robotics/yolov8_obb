# yolov8_obb
Special thanks for Robot Mania on this great work <br>
https://www.youtube.com/watch?v=7n6gCqC075g&list=PL-GGHj7CdCG6K9yAVe_LiW1ArjP5snOJm&index=2<br>

# Steps
git clone https://github.com/innovation-robotics/labelImg2.git<br>
git clone https://github.com/innovation-robotics/yolov8obb_training.git<br>
git clone https://github.com/innovation-robotics/yolov8_obb_msgs.git<br>
git clone https://github.com/innovation-robotics/yolov8_obb.git<br>
git clone https://github.com/otamajakusi/yolov5-utils<br>

sudo apt-get install pyqt5-dev-tools<br>
sudo pip3 install lxml<br>
pip3 install ultralytics<br>
cd yolov8_obb<br>
python3 capture_gstreamer.py<br>
move the robot and press s for saving<br>
after finishing press q<br>
cd ..<br>
cd labelImg2<br>
in the data directory predefined_classes.txt add screw_driver at the beginning<br>
python3 labelImg.py<br>
make the annotation and press Ctrl+S for every image<br>
cd ..<br>
python3 yolov5-utils/voc2yolo5_obb.py --path yolov8_obb/data_for_training/ --class-file labelImg2/data/predefined_classes.txt<br>
cd ..<br>
cd yolov8obb_training<br>
prepare the datasets/screw_driver_dataset images, labels<br>
python3 format_converter.py<br>
adjust the train_info.yaml<br>
python3 yolov8_obb_train.py<br>
copy the best.pt file from runs/obb/train/weights to the yolov8obb_training directory<br>
for testing run this file<br>
python3 yolov8_obb_webcam.py<br>
cd ..<br>
cd ..<br>
colcon build --event-handlers desktop_notification- status- --cmake-args -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=OFF<br>
ros2 run ros2_opencv publisher_node<br>
in new terminal<br>
ros2 run yolov8_obb yolov8_obb_publisher.py<br>
in new terminal <br>
rviz2<br>

