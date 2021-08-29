# MIT License

# Copyright (c) 2020 Hongrui Zheng

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='f1tenth_gym_ros',
            executable='gym_bridge',
            name='bridge',
            parameters=[{
                'ego_scan_topic': 'scan',
                'ego_odom_topic': 'odom',
                'ego_drive_topic': 'drive',
                'opp_scan_topic': 'opp_scan',
                'opp_odom_topic': 'opp_odom',
                'opp_drive_topic': 'opp_drive',
                'scan_distance_to_base_link': 0.275,
                'scan_fov': 4.7,
                'scan_beams': 1080,
                'map_path': '/f1tenth_gym/maps/berlin.yaml',
                'map_img_ext': '.png',
                'num_agent': 1
            }]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz'
        )
    ])