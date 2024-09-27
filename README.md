**General:**
This program utilizes the python programming interface UR-RTDE from SDU to create a graphical user interface that mimics the teach pendant.

**GUI:**
The gui was made in Qt-designer and can be opened and edited. After editing, open a commandprompt in the folder and utilize the command from the Commands.txt file to convert the ui file to a python gui file.

**How to setup:**
The only necessary change to the code should be to change the ip to match the local ip of the robot you're working on.

The gripper conrols work by sending a local script from the pc that tells the gripper to acivate/open/close. If the gripper is of a different
type than the Robotiq gripper that I am working with, you simply need to create new scripts on the robot, and throw them in the localscrips folder on the controlling pc.
