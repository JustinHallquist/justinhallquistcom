export default function SectionTabs({ sections, activeSection, handleSetActiveSection }) {
  return <div className="flex">
    {sections.map((section, idx) =>
      <button onClick={() => handleSetActiveSection(section)} key={`${section}.${idx}`} className={`${activeSection === section ? 'dark:text-blue-500' : 'dark:text-gray-300'} ml-2 flex items-center h-12 px-2 py-2 text-center text-gray-700 border border-b-0 border-gray-300 sm:px-4 dark:border-gray-500 rounded-t-md -px-1 dark:text-white whitespace-nowrap focus:outline-none`}>
        <span className="mx-1 text-sm sm:text-base">
          {section}
        </span>
      </button>
    )}
  </div>
}
