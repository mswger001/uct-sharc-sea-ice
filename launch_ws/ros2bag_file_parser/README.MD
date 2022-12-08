## getting started
1. Clone the repo
2. Install [pcl library](https://github.com/PointCloudLibrary/pcl) 
3. Navigate to the file parser and build the parser by running colcon build
4. Soucre it and add it to barshc to reduce repeating this step

  source ./install/local_setup.sh

5. change directory to the launch folder of the parser and run the launch file

    ros2 launch parse.pcd.xml

