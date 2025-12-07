import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  // By default, Docusaurus generates a sidebar from the docs folder structure
  tutorialSidebar: [
    'intro',  // Introduction page
    {
      type: 'category',
      label: 'Physical AI & Humanoid Robotics Textbook',
      items: [
        {
          type: 'category',
          label: 'Module 1: The Robotic Nervous System (ROS 2)',
          items: [
            'modules/module1-the-robotic-nervous-system/outline',
            'modules/module1-the-robotic-nervous-system/chapter-refined',
          ],
        },
        {
          type: 'category',
          label: 'Module 1: ROS 2 Fundamentals',
          items: [
            'modules/module-1-intro',
          ],
        },
      ],
    },
    // Additional categories can be added here
  ],

  // But you can create a sidebar manually
  /*
  tutorialSidebar: [
    'intro',
    'hello',
    {
      type: 'category',
      label: 'Tutorial',
      items: ['tutorial-basics/create-a-document'],
    },
  ],
   */
};

export default sidebars;
