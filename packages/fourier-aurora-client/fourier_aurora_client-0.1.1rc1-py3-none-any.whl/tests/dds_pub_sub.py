import fourier_msgs.msg.AuroraCmd as AuroraCmd
import time
from fourier_aurora_client import DDSInterface, SubscriberQosProfile, PublisherQosProfile

# initialize DDS node
dds_node = DDSInterface(domain_id=28)
topic_name = "whole_body_fsm_state_change_cmd"
topic_data_pub_sub_type = AuroraCmd.WholeBodyFsmStateChangeCmdPubSubType()
topic_data_type = AuroraCmd.WholeBodyFsmStateChangeCmd()

# create publisher and subscriber
subscriber_qos = SubscriberQosProfile.BEST_EFFORT
sub = dds_node.create_subscriber(topic_name, AuroraCmd.WholeBodyFsmStateChangeCmdPubSubType(), topic_data_type,lambda data: print(f"Received data: {data.desired_state()}"), subscriber_qos)
print("Subscriber created")

publisher_qos = PublisherQosProfile.BEST_EFFORT
pub = dds_node.create_publisher(topic_name, AuroraCmd.WholeBodyFsmStateChangeCmdPubSubType(), publisher_qos)
print("Publisher created")

time.sleep(1)

# publish data
data = AuroraCmd.WholeBodyFsmStateChangeCmd()
for _ in range(100):
    data.desired_state(0)
    pub.publish(data)
    print("Data published")
    time.sleep(0.5)

    data.desired_state(1)
    pub.publish(data)
    print("Data published")
