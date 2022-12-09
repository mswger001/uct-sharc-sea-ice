# importing os module 
import os
import json
from launch_ros.actions import Node

def get_nodes():

    dir_path = "/home/uctseaice/Documents/bag_files/"
    count = 0
    bag = "bag_"+str(count)+"_launch.py"
    f = open(bag, "w")
    f.write("from launch import LaunchDescription \nfrom launch_ros.actions import Node\ndef generate_launch_description():") 
    f.write("\n\n\treturn LaunchDescription([")    
    

    for path in os.scandir(dir_path):
        count +=1  
        if count%5 == 0:
            bag = "bag_"+str(count)+"_launch.py"
            f.write("\t ])")   
            f.close()
            f = open(bag, "w")  
            f.write("from launch import LaunchDescription \nfrom launch_ros.actions import Node\ndef generate_launch_description():")           
            f.write("\n\n\treturn LaunchDescription([")  
        for bpath in os.scandir(path.path):                
            if bpath.is_file():                
            # extract the file name and extension
                
                split_tup = bpath.name.split(".")
                file_name = split_tup[0]
                
                file_extension = split_tup[1]
                if file_extension == 'db3':
                    bag_file = path.path
                    f.write("\n\t Node(\n\t\t\tpackage='ros2bag_file_parser',\n\t\t\texecutable='ros2bag_file_parser_node',\n\t\t\tparameters=")
                    parameters=[
                        {"rosbag_directory" :path.path},
                        {"output_directory" :"/home/uctseaice/Documents/PCDS/"+file_name},
                        {"topic":"/camera/depth/color/points"}
                    ]
                    f.write("\n\t\t\t\t"+str(parameters))
                    f.write("\t),\n \n")

    f.write("\t ])")               


if __name__ == "__main__":
	
    get_nodes()
	
           