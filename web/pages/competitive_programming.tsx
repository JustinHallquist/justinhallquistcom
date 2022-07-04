import { useState } from 'react';
import Layout from './layouts/layout'
import TreeNav from './components/tree_nav';
import SectionTabs from './components/section_tabs';
import competitiveProgrammingResources from '../competitive_programming/resources.json'

const sites = competitiveProgrammingResources.problems
const defaultSite = Object.keys(sites)[0]
const defaultProblem = Object.keys(sites[defaultSite])[0]

const sections = ['problem', 'solution', 'explanation']
const defaultSection = 'problem'

export default function CompetitiveProgramming() {
  const [activeSite, setSite] = useState(defaultSite);
  const [activeProblem, setProblem] = useState(defaultProblem);
  const [activeSection, setSection] = useState(defaultSection);

  // TODO: type
  const handleSetSite = (site: String) => setSite(site)
  const handleSetProblem = (problem: String) => setProblem(problem)
  const handleSetActiveSection = (section: String) => setSection(section)

  return (
    <Layout content={
      <section className="h-full bg-white dark:bg-gray-900">
        <div className="container px-6 py-8 mx-auto">
          <div className="lg:flex lg:-mx-2">
            <TreeNav tree={sites} activeNode={activeSite} />
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
