import { useState } from 'react';
import Layout from './layouts/layout'
import TreeNav from './components/tree_nav';
import SectionTabs from './components/section_tabs';
import competitiveProgrammingResources from '../competitive_programming/resources.json'

const sites = competitiveProgrammingResources.problems

const sections = ['problem', 'solution', 'explanation']
const defaultSection = 'problem'

export default function CompetitiveProgramming() {
  const [activePath, setActivePath] = useState('');
  const [activeSection, setSection] = useState(defaultSection);

  // TODO: type
  const handleSetActivePath = (path: String) => setActivePath(path)
  const handleSetActiveSection = (section: String) => setSection(section)

  return (
    <Layout content={
      <section className="h-full bg-white dark:bg-gray-900">
        <div className="container px-6 py-8 mx-auto">
          <div className="lg:flex lg:-mx-2">
            <TreeNav tree={sites} activeNode={activePath} handleSetActivePath={handleSetActivePath} ignore={['files']} />
            <SectionTabs sections={sections} activeSection={activeSection} handleSetActiveSection={handleSetActiveSection} />

            <div className="grid grid-cols-1 gap-4 mt-4 md:grid-cols-1 lg:grid-cols-1 xl:grid-cols-1">
              <div className="dark:text-white text-sm tracking-widest">
              </div>
            </div>
          </div>
        </div>
      </section>
    } />
  )
}
