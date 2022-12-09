from launch import LaunchDescription
from launch_ros.actions import Node
# importing os module 
import os
def get_nodes():

    dir_path = "/home/uctseaice/Documents/bag_files/"
    bag_nodes = []
    

    for path in os.scandir(dir_path):            
        for bpath in os.scandir(path.path):                
            if bpath.is_file():                
            # extract the file name and extension
                
                split_tup = bpath.name.split(".")
                file_name = split_tup[0]
                file_extension = split_tup[1]
                if file_extension == 'db3':
                    bag_file = path.path
                    data = Node(
                                package="ros2bag_file_parser",
                                executable='ros2bag_file_parser_node',
                                name=file_name,
                                parameters=[
                                    {"rosbag_directory" :path.path},
                                    {"output_directory" :"/home/uctseaice/Documents/PCDS/"+file_name},
                                    {"topic":"/camera/depth/color/points"}
                                ]
                            )
                    
                    bag_nodes.append(data)
    print(bag_nodes)
    return bag_nodes


def generate_launch_description():
    nodes = get_nodes
    return LaunchDescription(nodes)