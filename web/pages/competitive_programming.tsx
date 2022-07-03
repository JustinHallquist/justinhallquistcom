import Layout from './layouts/layout'

export default function CompetitiveProgramming() {
  return (
    <Layout content={
      <section className="h-screen bg-white dark:bg-gray-900">
        <div className="container px-6 py-8 mx-auto">
          <div className="lg:flex lg:-mx-2">
            <div className="space-y-3 lg:w-1/5 lg:px-2 lg:space-y-4">
              <a href="#" className="block font-medium text-gray-500 dark:text-gray-300 hover:underline">usaco</a>
              <a href="#" className="block font-medium text-gray-500 dark:text-gray-300 hover:underline">codeforces</a>
            </div>

            <div className="mt-6 lg:mt-0 lg:px-2 lg:w-4/5 ">
              <div className="flex items-center justify-between text-sm tracking-widest uppercase ">
              </div>

              <div className="grid grid-cols-1 gap-8 mt-8 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
              </div>
            </div>
          </div>
        </div>
      </section>
    } />
  )
}
