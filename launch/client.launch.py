from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    hostname = '192.168.0.100'
    buffer_size = 256
    topic_namespace = 'vicon'

    return LaunchDescription([Node(
            package='vicon_receiver', executable='vicon_client', output='screen',
            parameters=[{'hostname': hostname, 'buffer_size': buffer_size, 'namespace': topic_namespace}]
        )])
# =j= = 8`     `  q`1 q`1 `q  `[]q    `]  []    `][ `   `\  `q  `]\ `]\ `]  `q  `   q`1\    `1`q`1` ``  `   ]\
#   ``  ````    `       q`1`    `1` `       `                       `   `   1   `   qqqqq   `       ``