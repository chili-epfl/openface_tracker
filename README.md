# openface_tracker
==================

New version of attention_tracker (https://github.com/chili-epfl/attention-tracker) using OpenFace Project https://github.com/TadasBaltrusaitis/OpenFace


### installation:

1. follow https://github.com/TadasBaltrusaitis/OpenFace/wiki/Unix-Installation for Dependencies

2. openface tracker is a ROS pakage :
```
$ cd (your catkin_ws)/src && git clone https://github.com/chili-epfl/openface_tracker.git in a ROS catkin workspace
$ cd .. && catkin_make
$ catkin_make install
```

### usage: 

you can specify the camera device you yant to use (0 by default). If you want to use an external camera (# 1):
```
$ roslaunch openface_tracker/openface_tracker.launch camera_device_arg:= 1
```
