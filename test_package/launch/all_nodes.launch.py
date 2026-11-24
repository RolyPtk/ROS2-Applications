from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([
            Node(
                package='test_package',
                executable='first_node',
                name='first_node',
                output='screen',
            ),
            Node(
                package='test_package',
                executable='second_node',
                name='second_node',
                output='screen',
            ),
        #adauga mai multe noduri pe care vrei sa le dai start deodata
])
