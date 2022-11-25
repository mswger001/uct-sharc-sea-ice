# SEAICE LIDAR & REALSENSE DEPTH CAMERA on Ubuntu 20:04 lts
Both lidar and realsense data can be simutenously captured and recored by calling one file 

## Installation Prerequesite: ROS2, ROS2 Wrapper for Intel&reg; RealSense&trade; Devices Livox  and Livox ROS2 Driver

1. Follow the instructions outline in the [ROS 2 Foxy installation](https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html) 

### NB one could use the ROS2 installation instructions as guided in step 2 by realsesne

2.Follow the instructions outlined in the [ROS2 Wrapper for Intel&reg; RealSense&trade](https://github.com/IntelRealSense/realsense-ros/blob/ros2-development/README.md)

3. Follow the instructions outlined in the [Livox ROS2 Driver installation](https://github.com/Livox-SDK/livox_ros2_driver)

4. At this point you should be able to use the launch file in this folder to start recording the data fro the two sensors by calling

```bash
   ./simple.sh
```
5. To stop the recording, exit the terminal using `CTL-C`

6. The recorded data can be found on the desktop recordings directory named and ordered by date and time

