# User Controlled Robot Simulation with ROS 2  🚀  

This project is part of my journey in mastering **Odometry, Kinematics, and Sensor Fusion with ROS 2**. It involves **simulating a user controlled robot, implementing odometry and localization, sensor fusion, and controller development using ROS 2 and Gazebo**.  

### System Setup  

To get started, ensure your system is prepared:  

1. **Install [Ubuntu 22.04.5](https://releases.ubuntu.com/jammy/)** (on a PC or Virtual Machine)  

2. Install either **[ROS Humble](https://docs.ros.org/en/humble/Installation.html)** or **[ROS Iron](https://docs.ros.org/en/iron/Installation.html)** on your Ubuntu 22.04.5

3. **Install Required ROS 2 Libraries**  
   Some dependencies are not included in the default ROS 2 installation. Install them using:  

   ```bash
   sudo apt-get update && sudo apt-get install -y \
       ros-humble-ros2-controllers \
       ros-humble-gazebo-ros \
       ros-humble-gazebo-ros-pkgs \
       ros-humble-ros2-control \
       ros-humble-gazebo-ros2-control \
       ros-humble-joint-state-publisher-gui \
       ros-humble-joy \
       ros-humble-joy-teleop \
       ros-humble-turtlesim \
       ros-humble-robot-localization \
       ros-humble-tf-transformations

## Usage
To Launch the Simulation of the Robot
1. Clone the repo
   ```bash
   git clone https://github.com/SagnikD2004/Bumperbot.git

2. Build the ROS2 workspace
   ```bash
   cd ~/BumperBot/Odometry and Kinematics/bumperbot_ws
   colcon build

3. Source the workspace in a different terminal
   ```bash
   . install/setup.bash

4. Launch the Gazebo Simulation
   ```bash
   ros2 launch bumperbot_description gazebo.launch.py
