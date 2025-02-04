#include<rclcpp/rclcpp.hpp>
#include<geometry_msgs/msg/twist.hpp>
#include<geometry_msgs/msg/twist_stamped.hpp>
#include<std_msgs/msg/header.hpp>

using std::placeholders::_1;

class TwistToStamped :public rclcpp::Node
{
public:
    TwistToStamped(const std::string& name) : Node(name)
    {
        twist_subscriber_ = this->create_subscription<geometry_msgs::msg::Twist>(
            "/cmd_vel", 10, std::bind(&TwistToStamped::twist_callback, this, _1)
        );

        twist_stamped_publisher_ = this->create_publisher<geometry_msgs::msg::TwistStamped>(
            "/bumperbot_controller/cmd_vel", 10);
    }

private:
    void twist_callback(const geometry_msgs::msg::Twist::SharedPtr twist_msg)
    {
        auto twist_stamped_msg = geometry_msgs::msg::TwistStamped();
        twist_stamped_msg.header.stamp = this->get_clock()->now();
        twist_stamped_msg.twist = *twist_msg;

        twist_stamped_publisher_->publish(twist_stamped_msg);
    }

    rclcpp::Subscription<geometry_msgs::msg::Twist>::SharedPtr twist_subscriber_;
    rclcpp::Publisher<geometry_msgs::msg::TwistStamped>::SharedPtr twist_stamped_publisher_;
};

int main(int argc, char* argv[]){
    rclcpp::init(argc, argv);
    auto node = std::make_shared<TwistToStamped>("twist_to_twist_stamped");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
