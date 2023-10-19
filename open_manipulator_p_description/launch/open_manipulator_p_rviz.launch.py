#!/usr/bin/env python3
#
# Copyright 2019 ROBOTIS CO., LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Ryan Shim

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    # Parameters
    use_gui = LaunchConfiguration('use_gui', default='true')  

    # File Paths
    # if True:
    #     urdf_file = os.path.join(get_package_share_directory('open_manipulator_p_description'), 'urdf', 'open_manipulator_p_robot.urdf.xacro')
    #     rviz_file = os.path.join(get_package_share_directory('open_manipulator_p_description'), 'rviz', 'open_manipulator_p.rviz')
    # else:

    urdf_file = os.path.join(get_package_share_directory('open_manipulator_p_description'), 'urdf', 'open_manipulator_p_with_gripper_robot.urdf.xacro')
    rviz_file = os.path.join(get_package_share_directory('open_manipulator_p_description'), 'rviz', 'open_manipulator_p_with_gripper.rviz')

    return LaunchDescription([
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            arguments=[urdf_file],
            parameters=[{'use_gui': use_gui},
                        {'source_list': ['joint_states']}],
            output='screen'),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            arguments=[urdf_file],
            output='screen'),

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_file],
            output='screen')
    ])
