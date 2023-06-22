# This script creates an object of type Robots to controll the Universal Robot UR3 
# To run this script type the following:
#     python -i start_robot.py
# The -i is needed to keep Python running, otherwise it will create the object and exit
from robot.robot import Robot
ts = Robot(["../../db/robot_settings.req","../../db/robot_settings.req"], {"$(P)":"32id:", "$(R)":"Robot:"})
