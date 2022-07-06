import { useState } from 'react';
import { ProblemContent, Content } from './interfaces/competitive_programming_interfaces'
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
    body = <Solution >{currentContent}</Solution>
  } else if (activeSection === 'problem') {
    body = <Problem input={currentContentParts.problem_in} output={currentContentParts.problem_out} dangerous={true}>{currentContent}</Problem>
  }

  return (
    <Layout content={
      <section className="h-full bg-white dark:bg-gray-900">
        <div className="container px-6 py-8 mx-auto">
          <div className="grid grid-cols-12 grid-rows-1 gap-4 grid-flow-row">
            <TreeNav className="box col-span-2 row-end-auto" tree={sites} activeNode={activePath} handleSetActivePath={handleSetActivePath} ignore={['files']} />

            <div className="grid col-span-10 grid-cols-1 grid-rows-12 gap-4">
              <div className="box row-span-1">
                <SectionTabs sections={availableSections} activeSection={activeSection} handleSetActiveSection={handleSetActiveSection} />
              </div>

              <div className="box row-end-auto row-span-11 gap-4 col-span-1 dark:text-white text-sm tracking-widest">
                {body}
              </div>
            </div>
          </div>
        </div>
      </section>
    } />
  )
}
