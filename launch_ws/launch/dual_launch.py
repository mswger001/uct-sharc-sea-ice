import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import launch
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import launch_ros.actions



realsense2_camera_pkg_prefix = get_package_share_directory('realsense2_camera')
livox_driver_pkg_prefix = get_package_share_directory('livox_ros2_driver')

 
def generate_launch_description():
    realsense2_camera_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [realsense2_camera_pkg_prefix, '/launch/rs_launch.py']),
        launch_arguments={'pointcloud.enable':'true','json_file_path':'/home/uctseaice/launch_ws/launch/HighDensityPreset.json'}.items()
    )
    
    livox_driver_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [livox_driver_pkg_prefix, '/launch/livox_lidar_launch.py']),
        launch_arguments={}.items()
    )    
   
    livox_and_realsense2_rviz = Node(
	    package='rviz2',
	    executable='rviz2',
	    output='screen',
	    arguments=['--display-config', "default.rviz" ]
    )
    livox_rviz = Node(
	    package='rviz2',
	    executable='rviz2',
	    output='screen',
	    arguments=['--display-config', livox_driver_pkg_prefix+"/config/livox_lidar.rviz" ]
    )
    
    realsense2_camera_rviz = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        arguments=['--display-config', realsense2_camera_pkg_prefix+"/launch/default.rviz"]
    )

    return LaunchDescription([
        livox_driver_launch,
        livox_rviz ,
        realsense2_camera_launch,
        realsense2_camera_rviz ,
        
        launch.actions.ExecuteProcess(
            cmd=['ros2', 'bag', 'record', '-a'],
            output='screen'
        ),
    ])
