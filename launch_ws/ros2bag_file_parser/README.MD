## getting started
1. Clone the repo
2. Install [pcl library](https://github.com/PointCloudLibrary/pcl) 
3. Navigate to the file parser and build the parser by running colcon build
4. Soucre it and add it to barshc to reduce repeating this step

  source ./install/local_setup.sh

5. Change directory to the launch folder of the parser
6. Open the parse.pcd.xml, Change the node parameters to fit the location of the bags files you  want to parse for the following 
      
      rosbag_directory
      &
      output_directory

```clojure
        <param name="rosbag_directory" value="/home/uctseaice/Documents/bag_files/rosbag2_2022_12_02-15_12_21"/>
        <param name="output_directory" value="/home/uctseaice/Documents/PCDS"/>
        <param name="topic" value="/camera/depth/color/points"/>
```

7.   and run the launch file

    ros2 launch parse.pcd.xml

