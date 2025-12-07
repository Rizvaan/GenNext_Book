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

Welcome to the fascinating world of ROS 2 (Robot Operating System 2)! This chapter introduces you to ROS 2, which serves as the "nervous system" that connects different components of a robot, enabling seamless communication and coordination. By the end of this chapter, you'll understand the core concepts of ROS 2 and be prepared to start building robotic applications.

<details>
<summary>For Advanced Learners</summary>

If you're already familiar with basic ROS 2 concepts, you can skip ahead to the section on Quality of Service (QoS) settings or jump directly to the exercises.
</details>

<details>
<summary>For Intermediate Learners</summary>

Focus on understanding the practical examples and try to run them yourself. Pay special attention to the differences between publishers/subscribers and services.
</details>

<details>
<summary>For Beginners</summary>

Take your time to understand each concept. Don't worry if everything isn't perfectly clear on the first read - robotics is complex! Focus on grasping the high-level idea before diving into the code.
</details>

## What is ROS 2?

ROS 2 is an open-source framework for developing robotics applications. If you think of a robot as a living organism, ROS 2 functions like the nervous system, allowing different parts to communicate and coordinate with each other.

### Why ROS 2 Matters

ROS 2 has become the de facto standard for robotics development because it solves several key problems:

1. **Communication**: It allows different parts of a robot to easily share information
2. **Modularity**: It enables components to be developed separately and integrated later
3. **Tooling**: It provides tools for visualization, debugging, and simulation
4. **Community**: It offers thousands of pre-built solutions and packages

### From ROS 1 to ROS 2

ROS 2 evolved from its predecessor, ROS 1, to address real-world challenges in deploying robotics systems. The key improvements include:

- **Real-time performance**: Better timing guarantees for safety-critical applications
- **Security**: Built-in security features for applications requiring access control
- **Multi-robot systems**: Better support for coordinating multiple robots
- **Industry standards**: Compliance with industrial communication protocols

### Key Features of ROS 2

- **Platform Independence**: Works across Linux, macOS, Windows, and embedded systems
- **Language Agnostic**: Supports Python, C++, Java, and other languages
- **Distributed Computing**: Enables multiple computers to collaborate seamlessly
- **Rich Ecosystem**: A vast collection of packages for perception, navigation, control, and more
- **Industry Adoption**: Trusted by leading companies in robotics and automation

## Core Concepts of ROS 2

Understanding these fundamental concepts will lay a strong foundation for your robotics journey.

### Nodes - The Building Blocks

A **node** is a process that performs computation. Think of nodes as individual workers in a factory - each responsible for a specific task.

**Key characteristics:**
- Each node performs a specific function
- Nodes communicate with each other through topics, services, or actions
- A robot typically has many nodes working together

**Examples of nodes in a mobile robot:**
- Motor controller node (controls wheels)
- Camera processing node (processes visual data)
- Navigation planner node (plans paths)
- User interface node (handles user commands)

### Topics - Communication Channels

A **topic** is a named channel for communication between nodes. Think of it as a radio frequency - publishers broadcast on it, and subscribers tune in to receive updates.

**How topics work:**
- Publishers send data to a topic
- Subscribers receive data from a topic
- Communication is asynchronous (no direct connection between publisher and subscriber)

**Example:** A camera node might publish sensor data to `/camera/image_raw`, which can be consumed by multiple other nodes - one for image processing, another for storage, and another for visualization.

### Publishers and Subscribers - The Communication Pattern

This is the most common communication pattern in ROS 2:

- **Publishers** continuously send messages to a topic
- **Subscribers** receive messages from a topic
- The publisher and subscriber are decoupled - they don't need to know about each other

<details>
<summary>Analogy: Newspaper Delivery</summary>

Think of publishers like newspapers being printed (published) and subscribers like readers who receive the newspaper (subscribe). The newspaper publisher doesn't know who specifically reads it, and readers don't need to know who published it.
</details>

### Services - Request-Response Communication

Services provide synchronous communication - you request something and get a response immediately, like asking a question and getting an answer.

**When to use services:**
- Operations that need a definitive response
- Saving a map
- Calculating values
- Checking robot status

**Service vs. Topic:**
- Services: One request, one response, synchronous
- Topics: Continuous data flow, asynchronous

### Actions - Advanced Communication

Actions are for long-running tasks that might need feedback or cancellation. Examples include:
- Navigating to a destination
- Moving a robot arm to a position
- Performing a complex manipulation task

Unlike services, actions can provide ongoing feedback and can be interrupted mid-operation.

## Working with ROS 2

### Installing ROS 2

The most recommended distribution is "Humble Hawksbill," which is a Long Term Support (LTS) release. Here's how to install it on Ubuntu 22.04:

```bash
# Update package lists
sudo apt update

# Add ROS repository key
curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key | sudo apt-key add -

# Add ROS repository
sudo sh -c 'echo "deb http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'

# Install ROS 2 Humble
sudo apt update
sudo apt install ros-humble-desktop
sudo apt install python3-colcon-common-extensions

# Install additional dependencies
sudo apt install python3-rosdep python3-vcstool
```

Source your ROS 2 installation:
```bash
source /opt/ros/humble/setup.bash
```

For convenience, add this to your `~/.bashrc` file so it's sourced automatically:
```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
```

### Creating Your First ROS 2 Workspace

A workspace is where you'll develop your ROS 2 packages. Let's create one:

```bash
# Create a new workspace directory
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws

# Build the workspace (even though it's empty for now)
colcon build

# Source the workspace to use the packages inside
source install/setup.bash
```

## Practical Example: Creating a Simple Publisher and Subscriber

Let's create a simple ROS 2 package to see these concepts in action.

### Step 1: Create a New Package

```bash
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_python py_pubsub
```

### Step 2: Create the Publisher Node

Create a publisher node at `~/ros2_ws/src/py_pubsub/py_pubsub/publisher_member_function.py`:

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

### Step 3: Create the Subscriber Node

Create a subscriber node at `~/ros2_ws/src/py_pubsub/py_pubsub/subscriber_member_function.py`:

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

### Step 4: Update Setup Files

Update the package setup file at `~/ros2_ws/src/py_pubsub/setup.py`:

```python
from setuptools import setup

package_name = 'py_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='Simple publisher subscriber example',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = py_pubsub.publisher_member_function:main',
            'listener = py_pubsub.subscriber_member_function:main',
        ],
    },
)
```

### Step 5: Run the Publisher and Subscriber

Open two terminal windows:

**Terminal 1** (Run the publisher):
```bash
cd ~/ros2_ws
source install/setup.bash
ros2 run py_pubsub talker
```

**Terminal 2** (Run the subscriber):
```bash
cd ~/ros2_ws
source install/setup.bash
ros2 run py_pubsub listener
```

You should see the publisher sending messages and the subscriber receiving them. Press `Ctrl+C` to stop the nodes.

## Services in Practice

Now let's explore services with another example. Create a service definition file at `~/ros2_ws/src/py_pubsub/py_pubsub/add_two_ints.srv`:

```
int64 a
int64 b
---
int64 sum
```

This service takes two integers and returns their sum.

### Service Server

Create the service server at `~/ros2_ws/src/py_pubsub/py_pubsub/service_member_function.py`:

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

### Service Client

Create the service client at `~/ros2_ws/src/py_pubsub/py_pubsub/client_member_function.py`:

```python
import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = AddTwoInts.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def main(args=None):
    rclpy.init(args=args)

    minimal_client = MinimalClientAsync()
    response = minimal_client.send_request(1, 2)
    minimal_client.get_logger().info(
        'Result of add_two_ints: for %d + %d = %d' %
        (1, 2, response.sum))

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

### Run the Service Example

**Terminal 1** (Start the service):
```bash
cd ~/ros2_ws
source install/setup.bash
ros2 run py_pubsub add_server
```

**Terminal 2** (Call the service):
```bash
cd ~/ros2_ws
source install/setup.bash
ros2 run py_pubsub add_client
```

## Quality of Service (QoS) Settings

One of the powerful features in ROS 2 is QoS (Quality of Service) settings, which allow fine-tuning of communication characteristics.

Common QoS settings include:

1. **Reliability**: 
   - `RELIABLE`: Guarantees delivery of messages
   - `BEST_EFFORT`: No guarantee of delivery, but faster

2. **Durability**:
   - `VOLATILE`: New subscribers don't receive past messages
   - `TRANSIENT_LOCAL`: New subscribers receive the last known value

3. **History Policy**:
   - `KEEP_LAST`: Keep the last N messages
   - `KEEP_ALL`: Keep all messages (use with caution)

This is crucial for real-time and safety-critical applications where you need to guarantee certain performance characteristics.

## Understanding the Big Picture

Now that you've seen the code examples, let's understand how these pieces fit together:

1. **Nodes** run separately but communicate through ROS 2's middleware
2. **Topics** enable asynchronous communication - data flows from publishers to subscribers
3. **Services** enable synchronous communication - a request is made, and a response is returned
4. **QoS settings** allow you to fine-tune communication behavior based on application requirements

This architecture allows for highly modular and reusable robot software components.

## Exercises for Understanding

1. **Modify the Publisher**: Adapt the publisher to simulate a distance sensor by publishing random values between 0.1 and 10.0 meters.

2. **Create a Data Logger**: Build a new node that subscribes to the distance sensor topic and logs the data to a file with timestamps.

3. **Service Enhancement**: Create a service that determines if a number is prime. Implement both the service server and client.

## Mini-Project: Simple Temperature Monitoring System

Apply your knowledge by building a temperature monitoring system:

**Components needed:**
1. A temperature simulator that publishes random temperatures between 15°C and 35°C
2. A monitor node that subscribes to the temperature topic and prints warnings when temperature exceeds 30°C
3. A data logger that records all temperature readings with timestamps
4. A historical data service that, when called, returns the average temperature over the last 10 readings

<details>
<summary>Starter Code for Temperature Simulator</summary>

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import random


class TemperatureSimulator(Node):

    def __init__(self):
        super().__init__('temperature_simulator')
        self.publisher_ = self.create_publisher(Float64, 'temperature', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Float64()
        # Generate random temperature between 15 and 35 degrees Celsius
        msg.data = random.uniform(15.0, 35.0)
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing temperature: %.2f°C' % msg.data)


def main(args=None):
    rclpy.init(args=args)
    temp_simulator = TemperatureSimulator()
    rclpy.spin(temp_simulator)
    temp_simulator.destroy_node()
    rclpy.shutdown()
```
</details>

## Summary

In this chapter, you've learned:
- **Nodes** as the fundamental computational units of ROS 2
- **Topics** for asynchronous publish-subscribe communication
- **Services** for synchronous request-response communication
- How to create and run publisher and subscriber nodes
- Basic understanding of Quality of Service settings
- Practical experience with ROS 2 tools and workflows

These concepts form the foundation for building more sophisticated robotic systems. Each component can be developed, tested, and maintained independently, then easily integrated with other components through ROS 2.

## Assessment Questions

1. **Conceptual Understanding**: What is the difference between a publisher-subscriber pattern and a service pattern in ROS 2? When would you use each?

2. **Practical Application**: Explain how DDS contributes to ROS 2's ability to work in distributed systems.

3. **Problem Solving**: When would you use a service vs. an action in ROS 2? Give a specific example for each.

4. **Analysis**: What advantages does the QoS setting "RELIABLE" provide, and when might you choose "BEST_EFFORT" instead?

## Common Challenges and Solutions

Newcomers to ROS 2 often face these challenges:

1. **Understanding Decoupling**: The publisher-subscriber model decouples nodes. Remember that publishers and subscribers don't need to know about each other.

2. **Environment Setup**: Always source your workspace (`source install/setup.bash`) before running ROS 2 commands. Consider adding this to your `~/.bashrc` file.

3. **Debugging Communication**: Use tools like `ros2 topic list`, `ros2 node list`, and `ros2 topic echo <topic_name>` to debug communication issues.

4. **Package Structure**: Follow the ROS 2 package structure and conventions. This ensures compatibility with build tools and other packages.

## Looking Forward

Now that you have a solid understanding of ROS 2 fundamentals, you're ready to explore:
- More complex message types
- Parameter management
- Advanced tools like Rviz for visualization
- Working with real sensors and actuators
- Robot simulation with Gazebo

The concepts you've learned here will continue to be relevant as you advance in your robotics journey!

---

## Glossary

- **Node**: A process that performs computation in ROS 2
- **Topic**: A named channel through which nodes exchange messages
- **Publisher**: A node that sends messages on a topic
- **Subscriber**: A node that receives messages from a topic
- **Service**: Synchronous request-response communication pattern
- **Action**: Advanced communication for long-running tasks with feedback
- **DDS**: Data Distribution Service - the middleware underlying ROS 2
- **RMW**: ROS Middleware - abstraction layer over DDS implementations
- **QoS**: Quality of Service - settings that control communication characteristics