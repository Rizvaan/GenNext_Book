---
title: ROS 2 کا تعارف - ایڈوانسڈ ویرینٹ (اعلی تجربہ)
description: ROS 2 کے اعلی معیار، کارکردگی کی کارکردگی، اور ایڈوانسڈ تصورات کے ساتھ
tags: [ROS2, روبوٹکس, مڈل ویئر, نوڈز، ٹاپکس، سروسز، python, cpp, performance]
difficulty: advanced
learning_outcomes:
  - ROS 2 کی اعلی معیار کی خدمات کو سمجھنا
  - کارکردگی کو بہتر بنانا
  - کسٹم میسج ٹائپس تیار کرنا
  - ایڈوانسڈ ڈسٹری بیوڈ سسٹم کی ترتیبات
---

# ROS 2 کا تعارف - ایڈوانسڈ ویرینٹ

## DDS کی گہرائی میں جانچ

DDS (ڈیٹا ڈسٹری بیوشن سروس) ایک قابل اعتماد، اعلی کارکردگی، ایجیل، اوپن سٹینڈرڈ کا استعمال کرتا ہے جو چھوٹا ہے اور اس کا استعمال ROS 2 میں کیا جاتا ہے. ROS 2 DDS کو RMW (ROS مڈل ویئر) کے ذریعے استعمال کرتا ہے جو DDS کے اوپر ایک ایب سٹریکشن لیئر ہے.

### DDS ایمپلیمنٹس:
- FastDDS (سابق فاسٹ RTPS)
- Cyclone DDS
- RTI Connext DDS
- Eclipse Zenoh

ہر ایک DDS ایمپلیمنٹ کے اپنے فوائد، کارکردگی کے حوالے، اور استعمال کی ترتیبات ہوتے ہیں.

## کسٹم میسج ٹائپس

ROS 2 میں کسٹم میسج ٹائپس کی اجازت ہے جو ایپلی کیشن کے مطابق ہو.ROS_MSGS_ کے ذریعے یہ کیا جا سکتا ہے. مثال کے طور پر، ایک کسٹم میسج فائل `geometry_msgs/Point32.msg` کی طرح ہو سکتا ہے:

```
float32 x
float32 y
float32 z
```

کمپائل کرنے کے لیے، `CMakeLists.txt` اور `package.xml` کو مندرجہ ذیل کے ساتھ اپ ڈیٹ کرنا ہوتا ہے:

```cmake
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/CustomMessage.msg"
  DEPENDENCIES builtin_interfaces std_msgs
)
```

## QoS (معیار کی خدمات) کی ترتیبات کی گہرائی

### History Policy
- `KEEP_LAST`: ڈسٹری بیوشن کے گزشتہ متعدد پیغامات کو محفوظ رکھیں
- `KEEP_ALL`: تمام پیغامات کو محفوظ رکھیں (احتیاط کے ساتھ استعمال کریں)

### Reliability Policy
- `RELIABLE`: تمام پیغامات کو بھیجنے کی ضمانت دیتے ہیں
- `BEST_EFFORT`: اسٹیلشمنٹ کے لیے ضمانت نہیں، لیکن تیز

### Durability Policy
- `VOLATILE`: نئے سبسکرائبر کو گزشتہ پیغامات نہیں ملتے
- `TRANSIENT_LOCAL`: نئے سبسکرائبر کو گزشتہ پیغامات ملتے ہیں

### Deadline Policy
- اس سے یقینی بنایا جا سکتا ہے کہ ڈیٹا مطلوبہ وقت کے اندر ترسیل ہوتا ہے

### Lifespan Policy
- ایک پیغام کو زندہ رہنے کا وقت متعین کریں

### Liveliness Policy
- اس سے یقینی بنایا جا سکتا ہے کہ ایک نوڈ زندہ ہے

## کارکردگی کی بہتری

### میموری مینجمنٹ
- سٹیٹک میموری الیکشن کو ترجیح دیں
- میموری لیکس کے لیے ٹیسٹس لکھیں

### ڈیٹا سیریلائزیشن
- Fast DDS جیسی کارکردگی کے لیے تیز سیریلائزیشن کا استعمال کریں

### مواصلت کے الگ الگ کمپونینٹس
- مختلف نوڈز کو مختلف پراسیسرز پر چلانا
- تیز کنکشن کے لیے انٹرفیس کو ایڈجسٹ کریں

## ڈسٹری بیوڈ سسٹم کی ترتیبات

### ڈومین آئی ڈی
- ڈسٹری بیوڈ ROS 2 نوڈز کو الگ کرنے کے لیے استعمال ہوتا ہے
- ہر ڈومین میں ایک الگ DDS سسٹم ہوتا ہے

### ملٹی کاسٹ بمقابلہ یونی کاسٹ
- ملٹی کاسٹ بہتر کارکردگی فراہم کرتا ہے لیکن کچھ نیٹ ورکس میں کام نہیں کرتا
- یونی کاسٹ اس کا متبادل ہے

## ایڈوانسڈ کوڈ مثال: میسج فلٹر کرنا

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy


class AdvancedFilterNode(Node):

    def __init__(self):
        super().__init__('advanced_filter_node')
        
        # قابل اعتماد QoS پروفائل تیار کریں
        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.RELIABLE,
            history=HistoryPolicy.KEEP_LAST,
            depth=10
        )
        
        self.subscription = self.create_subscription(
            String,
            'input_topic',
            self.filter_callback,
            qos_profile
        )
        
        self.publisher = self.create_publisher(
            String,
            'filtered_topic',
            qos_profile
        )

    def filter_callback(self, msg):
        # کسٹم فلٹر لاگو کریں
        if self.is_valid_message(msg):
            self.publisher.publish(msg)
            self.get_logger().info(f'Published filtered message: {msg.data}')

    def is_valid_message(self, msg):
        # میسج کی توثیق کریں
        return len(msg.data) > 0 and not msg.data.startswith('_')


def main(args=None):
    rclpy.init(args=args)
    node = AdvancedFilterNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

## مشق: ROS 2 کی کارکردگی کا جائزہ

1. کسٹم QoS پالیسیز کے ساتھ ایک نوڈ لکھیں اور اس کی کارکردگی کا جائزہ لیں.
2. مختلف DDS ایمپلیمنٹس کے درمیان موازنہ کریں.

یہ ویرینٹ اعلی سطح کے لوگوں کے لیے ہے جو ROS 2 کو پیشہ ورانہ سطح پر استعمال کر رہے ہیں.