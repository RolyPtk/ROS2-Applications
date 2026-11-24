
# Key Commands to be remembered

Here are some important commands that will always be in need in ROS2 applications:






- to verify if ROS2 Jazzy is installed on your system
```bash
  ls -la /opt/ros/jazzy
```
- the main configuration file that sets up the ROS2 environment. Has to be ran every time you open a new terminal!
```bash
  source /opt/ros/jazzy/setup.bash
```
- to build your ROS2 workspace for python implementation. There is also a C++ version 
```bash
  ros2 pkg create --build-type ament_python pkg_name
```
- a usefull program to check if everything is fine regarding some python dependencies (such as rclpy and std_msgs)
```bash
  sudo apt-get install python3-rosdep
```
```bash
  sudo rosdep init
```
```bash
  rosdep update
```
- build your package using colcon environment
```bash
  colcon build --packages-select pkg_name
```
- to run a node such as publisher or subscriber, or whatever your node is implemented for.
```bash
    ros2 run pkg_name node_name
```

