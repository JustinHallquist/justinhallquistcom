import { useState } from 'react';
import Layout from './layouts/layout'
import TreeNav from './components/tree_nav';
import SectionTabs from './components/section_tabs';
import Solution from './components/solution';
import Problem from './components/problem';
import competitiveProgrammingResources from '../competitive_programming/resources.json'
import competitiveProgrammingContent from '../competitive_programming/content.json'

const sites = competitiveProgrammingResources.problems

const sections = ['problem', 'solution', 'explanation']
const defaultSection = 'problem'

interface ProblemContent {
  problem: string;
  problem_in: string;
  problem_out: string;
  problem_supplement: string;
  solution: string;
  explanation: string;
}

interface Content {
  [index: string]: ProblemContent
}

const content: Content = competitiveProgrammingContent as Content

export default function CompetitiveProgramming() {
  const [activePath, setActivePath] = useState('');
  const [activeSection, setSection] = useState(defaultSection);

  // TODO: type
  const handleSetActivePath = (path: string) => setActivePath(path)
  const handleSetActiveSection = (section: string) => setSection(section)

  const key: string = activePath ? `problems/${activePath.replaceAll('.', '/')}` : ''
  const currentContentParts: ProblemContent = activePath && content[key] && content ? content[key] : {} as ProblemContent;
  const availableSections: Array<string> = sections.filter((section: string) => currentContentParts[section as keyof ProblemContent]).filter(Boolean)
  const currentContent: string = currentContentParts[activeSection as keyof ProblemContent]

  let body = null

  if (activeSection === 'solution') {
    body = <Solution>{currentContent}</Solution>
  } else if (activeSection === 'problem') {
    body = <Problem dangerous={true}>{currentContent}</Problem>
  }

  return (
    <Layout content={
      <section className="h-full bg-white dark:bg-gray-900">
        <div className="container px-6 py-8 mx-auto">
          <div className="lg:flex lg:-mx-2">
            <TreeNav tree={sites} activeNode={activePath} handleSetActivePath={handleSetActivePath} ignore={['files']} />
            <div className="grid">
              <div className="row-span-full">
                <div className="grid grid-cols-1 gap-4 mt-4 md:grid-cols-1 lg:grid-cols-1 xl:grid-cols-1">
                  <SectionTabs sections={availableSections} activeSection={activeSection} handleSetActiveSection={handleSetActiveSection} />
                </div>
              </div>

              <div className="grid grid-cols-1 gap-4 mt-4 md:grid-cols-1 lg:grid-cols-1 xl:grid-cols-1">
                <div className="dark:text-white text-sm tracking-widest">
                  {body}
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    } />
  )
}
