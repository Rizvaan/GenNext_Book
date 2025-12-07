---
sidebar_position: 2
---

import { QABot, PersonalizationButton, ProgressTracker, Exercises, TranslationToggle, Curriculum } from '../../src/components';

# Module 1: ROS 2 Fundamentals

<div className="chapter-metadata">
  <h3>Module Overview</h3>
  <p><strong>Learning Objectives:</strong></p>
  <ul>
    <li>Understand the architecture of ROS 2</li>
    <li>Learn about nodes, topics, services, and actions</li>
    <li>Implement basic ROS 2 programs</li>
  </ul>
  <p><strong>Difficulty Level:</strong> Beginner</p>
  <p><strong>Estimated Time:</strong> 4 hours</p>
</div>

## Introduction to ROS 2

Robot Operating System 2 (ROS 2) is a flexible framework for writing robot software. It is a collection of tools, libraries, and conventions that aim to simplify the task of creating complex and robust robot behavior across a wide variety of robot platforms.

ROS 2 differs from the original ROS in that it is designed for:

- Real-time systems
- Deterministic behavior
- Commercial product development
- Multi-robot systems
- Cross-platform compatibility

## Core Concepts

### Nodes

A node is an executable that uses ROS 2 to communicate with other nodes. Nodes can publish or subscribe to messages, provide or use services, and more. In object-oriented terms, a node could be considered a class with a ROS 2 communication interface.

```python
import rclpy
from rclpy.node import Node

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1
```

### Topics and Messages

Topics are named buses over which nodes exchange messages. A node can publish messages to a topic or subscribe to messages from a topic. Messages are data packets that are passed between nodes.

### Services

Services provide a request/reply interaction. A service client sends a request message to a service server and waits for a reply message.

## Practical Exercise: Creating Your First ROS 2 Package

<div className="exercise-block">
  <div className="exercise-title">Exercise: Basic Publisher/Subscriber</div>

  <p>Create a simple publisher and subscriber in ROS 2:</p>

  <h4>Step 1: Create a package</h4>
  <pre><code>ros2 pkg create --build-type ament_python my_robot_tutorials</code></pre>

  <h4>Step 2: Create a publisher</h4>
  <p>In the package directory, create a publisher script that publishes messages every second.</p>

  <h4>Step 3: Create a subscriber</h4>
  <p>Create a subscriber script that listens to the publisher's messages.</p>

  <h4>Step 4: Run the nodes</h4>
  <p>Run both nodes and verify that messages are being exchanged.</p>
</div>

<div className="component-container">
  <h3>Interactive Exercise</h3>
  <p>Complete the following quiz to test your understanding:</p>
  <Exercises />
</div>

<div className="component-container">
  <h3>AI Assistant</h3>
  <p>Ask questions about ROS 2 concepts:</p>
  <QABot />
</div>

<div className="component-container">
  <h3>Translation</h3>
  <p>Switch to Urdu to read this chapter in your preferred language:</p>
  <TranslationToggle />
</div>

<div className="component-container">
  <h3>Progress Tracker</h3>
  <p>Track your progress through this module:</p>
  <ProgressTracker moduleId={1} chapterId={2} userId={1} />
</div>

<div className="component-container">
  <h3>Personalization</h3>
  <p>Adjust the content difficulty using the personalization button:</p>
  <PersonalizationButton />
</div>

This module has introduced you to the fundamentals of ROS 2. In the next section, we'll explore more advanced concepts including services, actions, and parameter management.