import React, { useState, useEffect } from 'react';

const Curriculum = ({ userId }) => {
  const [modules, setModules] = useState([]);
  const [selectedModule, setSelectedModule] = useState(null);
  const [userProgress, setUserProgress] = useState({});

  // Mock data for curriculum
  const mockCurriculum = [
    {
      id: 1,
      title: "ROS 2 Fundamentals",
      description: "Learn the basics of Robot Operating System 2",
      chapters: [
        { id: 1, title: "Introduction to ROS 2", order: 1, difficulty: "beginner" },
        { id: 2, title: "Nodes and Topics", order: 2, difficulty: "beginner" },
        { id: 3, title: "Services and Actions", order: 3, difficulty: "intermediate" },
      ],
      prerequisites: []
    },
    {
      id: 2,
      title: "Digital Twins",
      description: "Simulation and modeling for robotics",
      chapters: [
        { id: 4, title: "Gazebo Physics Simulation", order: 1, difficulty: "intermediate" },
        { id: 5, title: "Unity Rendering", order: 2, difficulty: "intermediate" },
        { id: 6, title: "Sensor Simulation", order: 3, difficulty: "advanced" },
      ],
      prerequisites: [1]
    },
    {
      id: 3,
      title: "AI-Robot Brain",
      description: "NVIDIA Isaac and AI for robotics",
      chapters: [
        { id: 7, title: "Isaac Sim", order: 1, difficulty: "advanced" },
        { id: 8, title: "SLAM and Navigation", order: 2, difficulty: "advanced" },
        { id: 9, title: "Action Planning", order: 3, difficulty: "advanced" },
      ],
      prerequisites: [1, 2]
    },
    {
      id: 4,
      title: "Vision-Language-Action",
      description: "Voice commands and LLM integration",
      chapters: [
        { id: 10, title: "Whisper Voice Processing", order: 1, difficulty: "intermediate" },
        { id: 11, title: "LLM Planning", order: 2, difficulty: "advanced" },
        { id: 12, title: "Action Graphs", order: 3, difficulty: "advanced" },
      ],
      prerequisites: [1, 2, 3]
    }
  ];

  // Simulate loading data
  useEffect(() => {
    setModules(mockCurriculum);
    
    // Load user progress from localStorage (in a real app, this would come from the API)
    const savedProgress = localStorage.getItem(`curriculumProgress_${userId}`);
    if (savedProgress) {
      setUserProgress(JSON.parse(savedProgress));
    } else {
      // Initialize progress for each chapter
      const initialProgress = {};
      mockCurriculum.forEach(module => {
        module.chapters.forEach(chapter => {
          initialProgress[chapter.id] = { completed: false, percentage: 0 };
        });
      });
      setUserProgress(initialProgress);
      localStorage.setItem(`curriculumProgress_${userId}`, JSON.stringify(initialProgress));
    }
  }, [userId]);

  const toggleChapterCompletion = (chapterId) => {
    const newProgress = {
      ...userProgress,
      [chapterId]: {
        ...userProgress[chapterId],
        completed: !userProgress[chapterId].completed,
        percentage: userProgress[chapterId].completed ? 0 : 100
      }
    };
    
    setUserProgress(newProgress);
    localStorage.setItem(`curriculumProgress_${userId}`, JSON.stringify(newProgress));
  };

  const getModuleCompletion = (module) => {
    const completedChapters = module.chapters.filter(chapter => 
      userProgress[chapter.id]?.completed
    ).length;
    
    return Math.round((completedChapters / module.chapters.length) * 100);
  };

  const isPrerequisitesMet = (module) => {
    return module.prerequisites.every(prereqId => {
      const prereqModule = mockCurriculum.find(m => m.id === prereqId);
      return getModuleCompletion(prereqModule) === 100;
    });
  };

  const overallCompletion = () => {
    const totalChapters = mockCurriculum.reduce((sum, module) => sum + module.chapters.length, 0);
    const completedChapters = Object.values(userProgress).filter(p => p.completed).length;
    return totalChapters > 0 ? Math.round((completedChapters / totalChapters) * 100) : 0;
  };

  return (
    <div className="curriculum-container">
      <div className="curriculum-header">
        <h2>Learning Path: Physical AI & Humanoid Robotics</h2>
        <div className="overall-progress">
          <span>Overall Progress: {overallCompletion()}%</span>
          <div className="progress-bar">
            <div 
              className="progress-fill" 
              style={{ width: `${overallCompletion()}%` }}
            ></div>
          </div>
        </div>
      </div>
      
      <div className="curriculum-content">
        {modules.map(module => {
          const moduleCompletion = getModuleCompletion(module);
          const canAccess = isPrerequisitesMet(module);
          
          return (
            <div 
              key={module.id} 
              className={`module ${!canAccess ? 'locked' : ''}`}
            >
              <div 
                className={`module-header ${selectedModule?.id === module.id ? 'expanded' : ''}`}
                onClick={() => canAccess && setSelectedModule(
                  selectedModule?.id === module.id ? null : module
                )}
              >
                <div className="module-info">
                  <h3>{module.title}</h3>
                  <p>{module.description}</p>
                  <div className="module-stats">
                    <span>{module.chapters.length} chapters</span>
                    <span>Completion: {moduleCompletion}%</span>
                  </div>
                </div>
                <div className="module-actions">
                  <div className="progress-bar-small">
                    <div 
                      className="progress-fill" 
                      style={{ width: `${moduleCompletion}%` }}
                    ></div>
                  </div>
                  {!canAccess && <span className="lock-icon">🔒</span>}
                  <span className="toggle-icon">
                    {selectedModule?.id === module.id ? '▲' : '▼'}
                  </span>
                </div>
              </div>
              
              {selectedModule?.id === module.id && (
                <div className="module-content">
                  <div className="chapters-list">
                    {module.chapters.map(chapter => (
                      <div key={chapter.id} className="chapter">
                        <div className="chapter-info">
                          <span className="chapter-order">{chapter.order}.</span>
                          <span className="chapter-title">{chapter.title}</span>
                          <span className={`difficulty ${chapter.difficulty}`}>
                            {chapter.difficulty}
                          </span>
                        </div>
                        <div className="chapter-actions">
                          <span className={`completion-status ${userProgress[chapter.id]?.completed ? 'completed' : 'incomplete'}`}>
                            {userProgress[chapter.id]?.completed ? '✓' : '○'}
                          </span>
                          <button 
                            onClick={(e) => {
                              e.stopPropagation();
                              toggleChapterCompletion(chapter.id);
                            }}
                          >
                            {userProgress[chapter.id]?.completed ? 'Mark Incomplete' : 'Mark Complete'}
                          </button>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          );
        })}
      </div>
      
      <style jsx>{`
        .curriculum-container {
          font-family: Arial, sans-serif;
          max-width: 1000px;
          margin: 0 auto;
          padding: 16px;
        }
        
        .curriculum-header {
          margin-bottom: 24px;
        }
        
        .curriculum-header h2 {
          margin-top: 0;
          color: #333;
        }
        
        .overall-progress {
          margin-top: 16px;
        }
        
        .progress-bar {
          width: 100%;
          height: 20px;
          background-color: #e0e0e0;
          border-radius: 10px;
          overflow: hidden;
          margin-top: 8px;
        }
        
        .progress-fill {
          height: 100%;
          background-color: #4CAF50;
          transition: width 0.3s ease;
        }
        
        .curriculum-content {
          display: flex;
          flex-direction: column;
          gap: 16px;
        }
        
        .module {
          border: 1px solid #ddd;
          border-radius: 8px;
          overflow: hidden;
        }
        
        .module.locked {
          opacity: 0.6;
          border-color: #ff9800;
        }
        
        .module-header {
          background-color: #f5f5f5;
          padding: 16px;
          cursor: pointer;
          display: flex;
          justify-content: space-between;
          align-items: center;
        }
        
        .module-header:hover {
          background-color: #eee;
        }
        
        .module-header.expanded {
          background-color: #e8f5e9;
        }
        
        .module-info {
          flex: 1;
        }
        
        .module-info h3 {
          margin: 0 0 8px 0;
          color: #333;
        }
        
        .module-info p {
          margin: 0 0 8px 0;
          color: #666;
          font-size: 14px;
        }
        
        .module-stats {
          display: flex;
          gap: 16px;
          font-size: 13px;
          color: #777;
        }
        
        .module-actions {
          display: flex;
          align-items: center;
          gap: 8px;
        }
        
        .progress-bar-small {
          width: 100px;
          height: 12px;
          background-color: #e0e0e0;
          border-radius: 6px;
          overflow: hidden;
        }
        
        .module-content {
          padding: 16px;
          background-color: white;
        }
        
        .chapters-list {
          display: flex;
          flex-direction: column;
          gap: 8px;
        }
        
        .chapter {
          display: flex;
          justify-content: space-between;
          align-items: center;
          padding: 12px;
          border: 1px solid #eee;
          border-radius: 4px;
        }
        
        .chapter-info {
          display: flex;
          align-items: center;
          gap: 12px;
          flex: 1;
        }
        
        .chapter-order {
          font-weight: bold;
          color: #777;
        }
        
        .difficulty {
          padding: 2px 6px;
          border-radius: 10px;
          font-size: 11px;
          font-weight: bold;
        }
        
        .difficulty.beginner {
          background-color: #e8f5e9;
          color: #2e7d32;
        }
        
        .difficulty.intermediate {
          background-color: #fff8e1;
          color: #f57f17;
        }
        
        .difficulty.advanced {
          background-color: #ffebee;
          color: #c62828;
        }
        
        .chapter-actions {
          display: flex;
          align-items: center;
          gap: 8px;
        }
        
        .completion-status {
          font-size: 18px;
        }
        
        .completion-status.completed {
          color: #4CAF50;
        }
        
        .completion-status.incomplete {
          color: #999;
        }
        
        button {
          padding: 4px 8px;
          border: 1px solid #4CAF50;
          background-color: white;
          color: #4CAF50;
          border-radius: 4px;
          cursor: pointer;
          font-size: 12px;
        }
        
        button:hover {
          background-color: #e8f5e9;
        }
        
        .lock-icon {
          margin-right: 8px;
          font-size: 18px;
        }
        
        .toggle-icon {
          font-weight: bold;
          margin-left: 8px;
        }
      `}</style>
    </div>
  );
};

export default Curriculum;