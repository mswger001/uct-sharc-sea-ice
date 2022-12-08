from pypcd import pypcd
import open3d as o3d

from sensor_msgs.msg import PointCloud2
from sensor_msgs.msg import PointField

import sqlite3
from rosidl_runtime_py.utilities import get_message
from rclpy.serialization import deserialize_message

# importing os module 
import os

#import matplotlib.pyplot as plt

class BagFileParser():
    def __init__(self, bag_file):
        self.conn = sqlite3.connect(bag_file)
        self.cursor = self.conn.cursor()

        ## create a message type map
        topics_data = self.cursor.execute("SELECT id, name, type FROM topics").fetchall()
        #print(topics_data)
        self.topic_type = {name_of:type_of for id_of,name_of,type_of in topics_data}
        self.topic_id = {name_of:id_of for id_of,name_of,type_of in topics_data}
        self.topic_msg_message = {name_of:get_message(type_of) for id_of,name_of,type_of in topics_data}
        #print(self.topic_msg_message)
    def __del__(self):
        self.conn.close()

    # Return [(timestamp0, message0), (timestamp1, message1), ...]
    def get_messages(self, topic_name):
        
        topic_id = self.topic_id[topic_name]
        #print(topic_id)
        # Get from the db
        
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        #rint(self.cursor.fetchall())
        rows = self.cursor.execute("SELECT timestamp, data FROM messages WHERE topic_id = {}".format(topic_id)).fetchall()
        # Deserialise all and timestamp them
        return [ (timestamp,deserialize_message(data, self.topic_msg_message[topic_name])) for timestamp,data in rows]



if __name__ == "__main__":
	
	# set bagfile location
        bag_file = 'default'
        dir_path = os.getcwd()
        final_path = ''
   
        for path in os.scandir(dir_path):
            if path.is_file():
                
                # extract the file name and extension
                split_tup = path.name.split(".")
                file_name = split_tup[0]
                file_extension = split_tup[1]
                if file_extension == 'db3':
                    bag_file = path.path
                    final_path = path.name
                
        
       
        if bag_file != "default":
            print("bag file found at "+ bag_file)
            # set output location
            out = "/home/uctseaice/Documents/PCDS/"+ final_path
            isExist = os.path.exists(out)
            if not isExist:
                os.mkdir(out)

            parser = BagFileParser(bag_file)
            pcds = parser.get_messages("/livox/lidar")
        
        
        
        
        

            for i in range(len(pcds)):
                pcd = pcds[i]
                pcd_data =pcd[1]
                
                
                pc = pypcd.PointCloud.from_msg(pcd_data)
                pc.save(out+"/"+final_path+str(i)+'.pcd')
            print("saved "+ str(len(pcds))+ "pcds in the following directory"+ out)
        
        else:
            print("no bag file found in the current location")
                
        
        
