import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/rolandinio/ROS2_Projects/RCS_project/install/test_package'
