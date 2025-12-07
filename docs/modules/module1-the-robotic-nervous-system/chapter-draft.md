---
title: Introduction to ROS 2 - The Robotic Nervous System
description: Understanding the fundamentals of ROS 2, the middleware that powers modern robotics applications
tags: [ROS2, robotics, middleware, nodes, topics, services, python, cpp]
difficulty: beginner
learning_outcomes:
  - Understand what ROS 2 is and why it's important for robotics
  - Learn the fundamental concepts of nodes, topics, and services
  - Explore the architecture of a ROS 2 system
  - Begin working with ROS 2 tools and environment
---

# Introduction to ROS 2 - The Robotic Nervous System

## Chapter Overview

Welcome to the exciting world of ROS 2 (Robot Operating System 2)! In this chapter, we'll explore ROS 2 - the middleware that acts as the "nervous system" of modern robots. Just as your nervous system allows your brain to communicate with your limbs and organs, ROS 2 enables different components of a robot to communicate with each other. By the end of this chapter, you'll understand the core concepts of ROS 2 and be ready to start building robotic applications.

## What is ROS 2?

ROS 2 is an open-source framework for developing robotics applications. Think of it as the foundation that allows different parts of a robot to communicate, coordinate, and work together. It's been used to power everything from underwater exploration vehicles to autonomous cars and humanoid robots.

### The Evolution from ROS 1 to ROS 2

ROS 2 evolved from its predecessor, ROS 1, to address key challenges in deploying robotics systems in real-world applications. While ROS 1 was excellent for research and development, it had limitations in areas like:

- Real-time performance
- Security
- Multi-robot systems
- Quality of Service (QoS) controls
- Lifecycle management

ROS 2 addresses these by building on top of DDS (Data Distribution Service), which provides better real-time performance, security, and reliability.

### Key Features of ROS 2

- **Platform Independence**: Works on Linux, macOS, Windows, and even embedded systems
- **Language Agnostic**: Supports Python, C++, Java, and other languages through clients
- **Distributed Computing**: Enables multiple computers to work together seamlessly
- **Rich Ecosystem**: Thousands of packages and tools for perception, navigation, control, and more
- **Industry Adoption**: Used by major companies like Amazon, Google, Toyota, and Airbus

## Core Concepts of ROS 2

Understanding the core concepts of ROS 2 is crucial before diving into implementation. Let's explore the fundamental building blocks.

### Nodes

A **node** is a process that performs computation. In ROS 2, nodes are the fundamental units of computation. Think of nodes as individual agents in a robot's "brain" - each responsible for a specific task.

Nodes can:
- Publish messages to topics
- Subscribe to topics
- Provide services
- Call services
- Execute actions

In a mobile robot, you might have nodes for motor control, sensor processing, navigation planning, and user interface, all communicating through ROS 2.

### Topics

A **topic** is a named channel through which ROS nodes send and receive messages. Topics implement a publish-subscribe communication model where publishers send data to a topic and subscribers receive data from a topic. This allows for asynchronous communication between nodes.

For example, a camera node might publish sensor data to a topic called `/camera/image_raw`, and multiple nodes might subscribe to receive that data - perhaps one for image processing, another for visualization, and another for storage.

### Publishers and Subscribers

**Publishers** send messages to a topic, while **subscribers** receive messages from a topic. This is the most common communication pattern in ROS 2.

- Publishers and subscribers are decoupled: a publisher doesn't know who subscribes to its topic
- Multiple subscribers can listen to the same topic
- Multiple publishers can publish to the same topic (though this is less common)

### Services

Services provide synchronous request-response communication, similar to a function call. A client sends a request to a service and waits for a response.

Services are good for operations that need a response, like:
- Saving a map
- Adding a waypoint to a navigation system
- Asking for the current robot pose

### Actions

Actions are an advanced form of communication for long-running tasks that might need feedback and the ability to cancel. They're useful for tasks like navigation to a goal, moving a robot arm, or performing a complex manipulation task.

## Working with ROS 2

### Installing ROS 2

The most common distribution of ROS 2 is "Humble Hawksbill," which is an LTS (Long Term Support) release. To install it:

For Ubuntu 22.04:
```bash
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository universe
sudo apt update
sudo apt install curl gnupg2 lsb-release
curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key | sudo apt-key add -
sudo sh -c 'echo "deb http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'
sudo apt update
sudo apt install ros-humble-desktop
sudo apt install python3-colcon-common-extensions
```

Don't forget to source your setup:
```bash
source /opt/ros/humble/setup.bash
```

### Creating Your First ROS 2 Workspace

Let's create a workspace where we'll develop our ROS 2 packages:

```bash
# Create a new workspace
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws

# Build the workspace (even though it's empty for now)
colcon build

# Source the workspace to use the packages inside
source install/setup.bash
```

## Practical Example: Creating a Simple Publisher

Let's create a simple ROS 2 package and write a publisher and subscriber.

First, create a new package:
```bash
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_python py_pubsub
```

Now let's create a publisher node. In `~/ros2_ws/src/py_pubsub/py_pubsub/publisher_member_function.py`:

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

    # Destroy the node explicitly
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

And now a subscriber in `~/ros2_ws/src/py_pubsub/py_pubsub/subscriber_member_function.py`:

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

    # Destroy the node explicitly
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

To run these:
Terminal 1:
```bash
cd ~/ros2_ws
source install/setup.bash
ros2 run py_pubsub talker
```

Terminal 2:
```bash
cd ~/ros2_ws
source install/setup.bash
ros2 run py_pubsub listener
```

## Services in Practice

Now let's look at creating a service. Create the service definition file in `~/ros2_ws/src/py_pubsub/py_pubsub/add_three_ints.srv`:

```
int64 a
int64 b
int64 c
---
int64 sum
```

This service takes three integers and returns their sum. Create the service server:

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

## Quality of Service (QoS) Settings

One of the powerful features introduced in ROS 2 is QoS (Quality of Service) settings. QoS allows you to fine-tune communication characteristics, which is crucial for real-time and safety-critical applications.

Common QoS settings include:
- Reliability: RELIABLE (guaranteed delivery) or BEST_EFFORT (delivery not guaranteed)
- Durability: VOLATILE (new subscribers don't receive past messages) or TRANSIENT_LOCAL (new subscribers receive last known value)
- History: Keeping track of how many messages to maintain in history

## Exercises

1. **Modify the Publisher**: Adapt the publisher to send sensor data instead of simple strings. Perhaps simulate a distance sensor with values between 0.1 and 10.0 meters.

2. **Create a Data Logger**: Build a new node that subscribes to the distance sensor topic and logs the data to a file with timestamps.

3. **Service Enhancement**: Create a service that takes a number and returns whether it's prime. Implement both the service server and client.

## Mini-Project: Simple Temperature Monitor

Create a system consisting of:
1. A temperature simulator that publishes random temperatures between 15°C and 35°C
2. A monitor node that subscribes to the temperature topic and prints warnings when temperature goes above 30°C
3. A data logger that records all temperature readings with timestamps
4. A historical data service that, when called, returns the average temperature over the last 10 readings

## Summary

In this chapter, we covered the foundational concepts of ROS 2:
- Nodes as the fundamental computational units
- Topics for asynchronous publish-subscribe communication
- Services for synchronous request-response communication
- How to create and run simple publisher and subscriber nodes
- Quality of Service settings for controlling communication behavior

This knowledge forms the basis for building more complex robotic systems. In the next chapter, we'll dive deeper into ROS 2 tools, parameter management, and more advanced communication patterns.

## Assessment Questions

1. What is the difference between a publisher-subscriber pattern and a service pattern in ROS 2?
2. Explain the role of DDS in ROS 2 architecture.
3. When would you use a service vs. an action in ROS 2?
4. What does the QoS setting "RELIABLE" guarantee in ROS 2 communication?

## Common Challenges and Solutions

Newcomers to ROS 2 often face challenges with:
- Understanding the node-topic relationship
- Managing workspace environments
- Debugging communication issues

Remember to always source your workspace before running ROS 2 commands, and use tools like `ros2 topic list` and `ros2 node list` to debug communication issues.

Now you're ready to explore more complex aspects of ROS 2 and build increasingly sophisticated robotic applications!