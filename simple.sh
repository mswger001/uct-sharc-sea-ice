 ROS_DISTRO=foxy  
 
 source ~/ros2_ws/install/local_setup.sh 
 source ~/ws_livox/install/local_setup.sh
 source /opt/ros/foxy/setup.bash
 
 cd /home/uctseaice/Documents/bag_files
 
 ros2 launch /home/uctseaice/Desktop/launch/dual_launch.py
