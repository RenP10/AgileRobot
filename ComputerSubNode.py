
import rospy
from nav_msgs.msg import Odometry

# define the callback function for the odom topic
def car1_odom_callback(data):
    rospy.loginfo("Received odom data: x=%f, y=%f, z=%f", 
                  data.pose.pose.position.x, data.pose.pose.position.y, data.pose.pose.position.z)

def car2_odom_callback(data):
    rospy.loginfo("Received odom data: x=%f, y=%f, z=%f", 
                  data.pose.pose.position.x, data.pose.pose.position.y, data.pose.pose.position.z) 


if __name__ == '__main__':
    # initialize the node
    rospy.init_node('odom_subscriber')
    
    # specify the ROS master URIs of the two cars
    rospy.set_param('car1_uri', 'http://<car1_ip_address>:11311')
    rospy.set_param('car2_uri', 'http://<car2_ip_address>:11311')

     # subscribe to the first car's odom topic
    car1_odom_subscriber = rospy.Subscriber('/car1/odom', Odometry, car1_odom_callback)
    
    # subscribe to the second car's odom topic
    car2_odom_subscriber = rospy.Subscriber('/car2/odom', Odometry, car2_odom_callback)

    
    # spin the node to keep it running
    rospy.spin()