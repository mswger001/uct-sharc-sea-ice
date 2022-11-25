 ROS_DISTRO=foxy  
 
 source ./ros2_ws/install/local_setup.sh 
 source ./ws_livox/install/local_setup.sh
 source /opt/ros/foxy/setup.bash
 
 ros2 launch launch_ws/launch/fin_launch.py
