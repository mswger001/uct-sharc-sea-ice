## Project title
........................

1. required to make an simple inteface with the two given sensors i.e Livox lidar and realsense camera
2. this was achieved using the ros2 (robotic operatig system 2),
 the drivers were taken as created by the respective sensor manufacturer,
 a simple launch file was created to launch nodes to publish the sensor messages, 
 the same launch file also was used to display the topiccs graphically using rviz2, 
 the messages were reored and kept all in one bag file with the default naming convections of using time stamp
3. next was to exctract the data recorded in the bag files, this was done by making use of desirialisers implemented in python and cpp
 the main topics which were to be extracted were the livox/lidar, camera/color/points and camera/color/image_raw 
 these three would then be used later on on the full project scope and hence the need to be able to get them back
4. future ideas include creating a script to start and stop recording at a set time e.g ten secs,
 being able to use a gui instead of cli, 
 being able to get the data desirialised in real time of recording,
 being able to get file info into a csv in real time
