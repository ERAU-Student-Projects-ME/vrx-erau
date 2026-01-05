import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def launch_setup(context, *args, **kwargs):
    vehicle = LaunchConfiguration('vehicle').perform(context)

    if vehicle == 'minion':
        parameters_file = os.path.join(
            get_package_share_directory('vrx_gz'),
            'config', 'wamv.yaml'
        )
    elif vehicle == 'mini_minion':
        parameters_file = os.path.join(
            get_package_share_directory('vrx_gz'),
            'config', 'roboboat.yaml'
        )
    else:
        parameters_file = os.path.join(
            get_package_share_directory('vrx_gz'),
            'config', 'wamv.yaml'
        )
        
    print(f"Config File - {parameters_file}")

    return [
        Node(
            package='joy',
            executable='joy_node'
        ),
        Node(
            package='joy_teleop',
            executable='joy_teleop',
            parameters=[parameters_file]
        )
    ]


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'vehicle',
            default_value='minion',
            description='Vehicle name'
        ),
        DeclareLaunchArgument(
            'cmd_vel',
            default_value='cmd_vel'
        ),
        OpaqueFunction(function=launch_setup),
    ])

