import React, { useState, useEffect } from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import useBaseUrl from '@docusaurus/useBaseUrl';
import './ModuleNavigation.css';

const ModuleNavigation = () => {
  const { siteConfig } = useDocusaurusContext();
  const [modules, setModules] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [userProgress, setUserProgress] = useState({});

  // This would normally come from an API call
  useEffect(() => {
    // Mock data for modules - in a real implementation, this would be fetched from the backend
    const mockModules = [
      {
        id: "module1-the-robotic-nervous-system",
        title: "The Robotic Nervous System (ROS 2)",
        description: "Introduction to ROS 2 fundamentals: nodes, topics, services, URDF",
        order: 1,
        chapters: [
          { id: "chapter1-intro-ros2", title: "Introduction to ROS 2", completed: false },
          { id: "chapter2-ros2-nodes", title: "ROS 2 Nodes and Architecture", completed: false },
          { id: "chapter3-ros2-topics", title: "Topics and Message Passing", completed: false },
          { id: "chapter4-urdf-humanoids", title: "URDF for Humanoid Modeling", completed: false }
        ]
      },
      {
        id: "module2-digital-twins",
        title: "Digital Twins (Gazebo + Unity)",
        description: "Physics simulation, sensor simulation, high-fidelity rendering",
        order: 2,
        chapters: [
          { id: "chapter1-gazebo-physics", title: "Gazebo Physics Simulation", completed: false },
          { id: "chapter2-unity-rendering", title: "Unity Rendering for Robots", completed: false },
          { id: "chapter3-sensor-simulation", title: "Sensor Simulation Techniques", completed: false }
        ]
      },
      {
        id: "module3-ai-robot-brain",
        title: "AI-Robot Brain (NVIDIA Isaac)",
        description: "Isaac Sim, Isaac ROS, SLAM, Nav2 path planning",
        order: 3,
        chapters: [
          { id: "chapter1-isaac-sim", title: "Isaac Sim Basics", completed: false },
          { id: "chapter2-isaac-ros", title: "Isaac ROS Integration", completed: false },
          { id: "chapter3-vslam", title: "Visual SLAM Techniques", completed: false }
        ]
      },
      {
        id: "module4-vision-language-action",
        title: "Vision-Language-Action (VLA)",
        description: "Whisper voice commands, LLM cognitive planning, ROS2 action graphs",
        order: 4,
        chapters: [
          { id: "chapter1-whisper-voice", title: "Whisper Voice Input Processing", completed: false },
          { id: "chapter2-llm-planning", title: "LLM-Based Cognitive Planning", completed: false },
          { id: "chapter3-ros2-actions", title: "ROS2 Action Graphs", completed: false }
        ]
      },
      {
        id: "capstone-autonomous-humanoid",
        title: "Capstone: Autonomous Humanoid",
        description: "Complete project integrating all concepts learned",
        order: 5,
        chapters: [
          { id: "chapter1-voice-pipeline", title: "Voice-to-Action Pipeline", completed: false },
          { id: "chapter2-object-recognition", title: "Object Recognition Systems", completed: false },
          { id: "chapter3-navigation", title: "Navigation and Obstacle Avoidance", completed: false },
          { id: "chapter4-final-integration", title: "Final Integration Project", completed: false }
        ]
      }
    ];

    setModules(mockModules);
    setLoading(false);
  }, []);

  // Mock function to simulate getting user progress
  useEffect(() => {
    // In a real implementation, this would fetch user progress from an API
    const mockProgress = {};
    mockProgress["module1-the-robotic-nervous-system"] = {
      completedChapters: 2,
      totalChapters: 4,
      overallCompletion: 50
    };
    // Additional progress data could be populated here

    setUserProgress(mockProgress);
  }, []);

  if (loading) {
    return <div className="module-nav-loading">Loading curriculum...</div>;
  }

  if (error) {
    return <div className="module-nav-error">Error loading curriculum: {error.message}</div>;
  }

  const getModuleStatus = (moduleId) => {
    const progress = userProgress[moduleId];
    if (!progress) return { status: 'not-started', completion: 0 };
    
    if (progress.completedChapters === progress.totalChapters) {
      return { status: 'completed', completion: 100 };
    } else if (progress.completedChapters > 0) {
      return { status: 'in-progress', completion: progress.overallCompletion };
    } else {
      return { status: 'not-started', completion: 0 };
    }
  };

  const getStatusClass = (status) => {
    switch(status) {
      case 'completed': return 'status-completed';
      case 'in-progress': return 'status-in-progress';
      case 'not-started': return 'status-not-started';
      default: return '';
    }
  };

  const getProgressWidth = (completion) => {
    return { width: `${completion}%` };
  };

  return (
    <div className="module-navigation-container">
      <div className="module-nav-header">
        <h2>{siteConfig.title} Curriculum</h2>
        <p>Navigate through the structured robotics curriculum</p>
      </div>

      <div className="module-list">
        {modules.map(module => {
          const moduleStats = getModuleStatus(module.id);
          
          return (
            <div key={module.id} className="module-card">
              <div className="module-header">
                <div className="module-title">
                  <h3>
                    <Link to={useBaseUrl(`/docs/modules/${module.id}`)}>
                      Module {module.order}: {module.title}
                    </Link>
                  </h3>
                  <span className={`module-status ${getStatusClass(moduleStats.status)}`}>
                    {moduleStats.status.replace('-', ' ').toUpperCase()}
                  </span>
                </div>
                <div className="module-meta">
                  <span>{module.chapters.length} Chapters</span>
                </div>
              </div>

              <div className="module-description">
                <p>{module.description}</p>
              </div>

              <div className="module-progress">
                <div className="progress-bar">
                  <div 
                    className={`progress-fill ${getStatusClass(moduleStats.status)}`} 
                    style={getProgressWidth(moduleStats.completion)}
                  ></div>
                </div>
                <div className="progress-text">{moduleStats.completion}% Complete</div>
              </div>

              <div className="module-chapters">
                <h4>Chapters:</h4>
                <ul>
                  {module.chapters.map(chapter => (
                    <li key={chapter.id} className={`chapter-item ${chapter.completed ? 'completed' : ''}`}>
                      <Link to={useBaseUrl(`/docs/modules/${module.id}/${chapter.id}`)}>
                        {chapter.title}
                        {chapter.completed && <span className="completed-badge">✓</span>}
                      </Link>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default ModuleNavigation;