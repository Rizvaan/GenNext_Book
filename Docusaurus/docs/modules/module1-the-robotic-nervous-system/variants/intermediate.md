---
title: ROS 2 کا تعارف - انٹرمیڈیٹ ویرینٹ (معتدل تجربہ)
description: ROS 2 کے اوزار، نوڈز، ٹاپکس، اور سروسز کے بارے میں تفصیلی معلومات کے ساتھ
tags: [ROS2, روبوٹکس, مڈل ویئر, نوڈز، ٹاپکس، سروسز، python, cpp]
difficulty: intermediate
learning_outcomes:
  - ROS 2 کی آرکیٹیکچر کو سمجھنا
  - پبلشر اور سبسکرائبر کو نافذ کرنا
  - خدمات کے استعمال کو سمجھنا
  - ROS 2 کے اوزار کا استعمال کرنا
---

# ROS 2 کا تعارف - انٹرمیڈیٹ ویرینٹ

## ROS 2 کی آرکیٹیکچر

ROS 2 ایک وسیع قسم کے کمپونینٹس کا احاطہ کرتا ہے:

### DDS (ڈیٹا ڈسٹری بیوشن سروس)
- ROS 2 کا مرکزی حصہ ہے
- ڈیٹا کو مختلف نوڈز کے درمیان منتقل کرتا ہے
- اس کے ذریعے متعدد کمپیوٹرز ایک دوسرے سے مواصلت کر سکتے ہیں

### RMW (ROS مڈل ویئر)
- DDS کے اوپر ایک ایب سٹریکشن لیئر
- مختلف DDS ایمپلیمنٹس کے درمیان تبدیلی کی اجازت دیتا ہے

## عملی کوڈ: نوڈ، ٹاپک، اور سروس

### 1. سادہ پبلشر نوڈ (Python)

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello Robot %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

### 2. سبسکرائبر نوڈ (Python)

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

### 3. سروس سرور (Python)

```python
import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))

        return response


def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

## ROS 2 کے اوزار

ROS 2 کے متعدد اوزار ہیں جو ترقی کو آسان بناتے ہیں:

- `ros2 topic list` - تمام ٹاپکس کو دکھاتا ہے
- `ros2 node list` - تمام نوڈز کو دکھاتا ہے
- `ros2 run <package> <executable>` - ایک نوڈ چلاتا ہے
- `ros2 topic echo <topic_name>` - ایک ٹاپک سے آنے والے ڈیٹا کو دکھاتا ہے

## QoS (معیار کی خدمات) کی ترتیبات

- **Reliability**: یقینی ترسیل (RELIABLE) یا بہترین کوشش (BEST_EFFORT)
- **Durability**: متزلزل (VOLATILE) یا عارضی مقامی (TRANSIENT_LOCAL)
- **History**: گزشتہ پیغامات کا اندراج

## مشق: ڈیٹا کا جائزہ

1. دونوں نوڈز (پبلشر اور سبسکرائبر) کو چلائیں اور ڈیٹا کا تبادلہ دیکھیں.
2. QoS کی ترتیبات کو تبدیل کرکے دیکھیں کہ کیا تبدیلی آتی ہے.

یہ ویرینٹ متوسط سطح کے لوگوں کے لیے ہے جن کے پاس کم ویژن کا تجربہ ہے.