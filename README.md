# SEAICE LIDAR & REALSENSE DEPTH CAMERA on Ubuntu 20:04 lts
Both lidar and realsense data can be simutenously captured and recored by calling one file 

## Installation Prerequesite: ROS2, ROS2 Wrapper for Intel&reg; RealSense&trade; Devices Livox  and Livox ROS2 Driver

1. Follow the instructions outline in the [ROS 2 Foxy installation](https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html) 

### NB one could use the ROS2 installation instructions as guided in step 2 and 3 by realsesne for this step use foxy

2.Follow the instructions outlined in the [ROS2 Wrapper for Intel&reg; RealSense&trade](https://github.com/IntelRealSense/realsense-ros/blob/ros2-development/README.md)

### NB one could use the ROS2 installation instructions as guided in step 3 by livox for this step use dashing

3. Follow the instructions outlined in the [Livox ROS2 Driver installation](https://github.com/Livox-SDK/livox_ros2_driver)

3.2. Refer to the [Livox Avia User Manual](https://www.livoxtech.com/de/avia/downloads) on how to set the IP address of the computer.

4. At this point you should be able to use the launch file in this folder to start recording the data fro the two sensors by calling

```bash
   ./simple.sh
```
5. You should also set up where you would want to keep the recordings otherwise they would be kept whereever you call the launch file, to chage the locatio of the recording you can uncoment [the line with the change of dir](simple.sh?plain=1#L5) in the file [simple.sh](simple.sh)

6. To stop the recording, exit the terminal using `CTL-C`

7. The recorded data can be found where you set them to be or in the same folder as the *simple.sh* recordings directory named and ordered by date and time

