import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <div className={styles.bookCover}>
          <div className={styles.bookSpine}></div>
          <div className={styles.bookPage}>
            <div className={styles.bookTitle}>
              <Heading as="h1" className="hero__title">
                {siteConfig.title}
              </Heading>
              <p className="hero__subtitle">{siteConfig.tagline}</p>
            </div>

            <div className={styles.bookContent}>
              <div className={styles.bookImage}>
                <div className={styles.robotIcon}></div>
              </div>

              <div className={styles.bookDescription}>
                <p>Learn the fundamentals of Physical AI and Humanoid Robotics with an interactive, AI-powered textbook designed to adapt to your learning style.</p>
              </div>
            </div>

            <div className={styles.bookButtons}>
              <Link
                className="button button--secondary button--lg"
                to="/docs/intro">
                Start Learning - 5min ⏱️
              </Link>
              <Link
                className="button button--primary button--lg margin-left--sm"
                to="/docs/modules/module1-the-robotic-nervous-system/outline">
                Explore Modules
              </Link>
            </div>
          </div>
          <div className={styles.bookBackCover}></div>
        </div>
      </div>
    </header>
  );
}

function AdditionalInfoSection() {
  return (
    <section className={styles.additionalInfo}>
      <div className="container">
        <div className="row">
          <div className="col col--4">
            <div className={styles.infoCard}>
              <h3>Adaptive Content</h3>
              <p>Content adjusts to your skill level - from beginner to advanced - ensuring optimal learning at your pace.</p>
            </div>
          </div>
          <div className="col col--4">
            <div className={styles.infoCard}>
              <h3>AI Assistant</h3>
              <p>Ask questions about the textbook content and get AI-generated answers based on the material.</p>
            </div>
          </div>
          <div className="col col--4">
            <div className={styles.infoCard}>
              <h3>Multi-Language</h3>
              <p>Access content in multiple languages, including English and Urdu, with technical terms preserved.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

function TestimonialSection() {
  return (
    <section className={styles.testimonials}>
      <div className="container">
        <div className="row">
          <div className="col col--12 text--center">
            <h2>What Learners Are Saying</h2>
          </div>
        </div>
        <div className="row">
          <div className="col col--4">
            <div className={styles.testimonialCard}>
              <p>"This textbook made complex robotics concepts accessible through its personalized approach."</p>
              <p className={styles.author}>- Robotics Student</p>
            </div>
          </div>
          <div className="col col--4">
            <div className={styles.testimonialCard}>
              <p>"The AI assistant helped clarify difficult topics instantly, like having a tutor available 24/7."</p>
              <p className={styles.author}>- AI Enthusiast</p>
            </div>
          </div>
          <div className="col col--4">
            <div className={styles.testimonialCard}>
              <p>"The multi-language support made advanced robotics education accessible to a wider audience."</p>
              <p className={styles.author}>- Engineering Professional</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Welcome to ${siteConfig.title}`}
      description="An interactive AI-Native learning experience for Physical AI & Humanoid Robotics">
      <HomepageHeader />
      <main>
        <AdditionalInfoSection />
        <HomepageFeatures />
        <TestimonialSection />
      </main>
    </Layout>
  );
}
