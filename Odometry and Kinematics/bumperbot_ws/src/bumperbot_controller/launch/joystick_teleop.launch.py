from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    # The commented section (only) is for externally connected controller connected either via usb/bluetooth the uncommented section is kor keyboard control
    # joy_node = Node(
    #     package="joy",
    #     executable="joy_node",
    #     name="joystick",
    #     parameters=[os.path.join(get_package_share_directory("bumperbot_controller"), "config", "joy_config.yaml")]
    # )

    # joy_teleop = Node(
    #     package="joy_teleop",
    #     executable="joy_teleop",
    #     parameters=[os.path.join(get_package_share_directory("bumperbot_controller"), "config", "joy_teleop.yaml")]
    # )

    return LaunchDescription([
        # joy_node,
        # joy_teleop

        ExecuteProcess(
            cmd=['gnome-terminal', '--', 'bash', '-c', 'ros2 run teleop_twist_keyboard teleop_twist_keyboard'],
            output='screen'
        ),

        Node(
            package="teleop_twist_keyboard",
            executable="teleop_twist_keyboard",
            name='teleop_twist_keyboard',
            output='screen',
            remappings=[
                ('/cmd_vel', 'bumperbot_controller/cmd_vel')
            ],
        ),

        Node(
            package="bumperbot_controller",
            executable="twist_to_stamped",
            name="twist_to_stamped",
            output="screen",
            remappings=[
                ('/cmd_vel', '/cmd_vel'),
                ('/bumperbot_controller/cmd_vel', '/bumperbot_controller/cmd_vel')
            ],

        ),
    ])