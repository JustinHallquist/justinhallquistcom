import Link from "next/link"

export default function Nav() {
  return <nav className="bg-white shadow dark:bg-gray-800">
    <div className="container px-6 py-4 mx-auto md:flex md:justify-between md:items-center">
      <div className="flex items-center justify-between">
        <Link href="/">
          <a className="text-2xl font-bold text-gray-800 transition-colors duration-200 transform dark:text-white lg:text-3xl hover:text-gray-700 dark:hover:text-gray-300">JH</a>
        </Link>

        <div className="flex md:hidden">
          <button type="button" className="text-gray-500 dark:text-gray-200 hover:text-gray-600 dark:hover:text-gray-400 focus:outline-none focus:text-gray-600 dark:focus:text-gray-400" aria-label="toggle menu">
            <svg viewBox="0 0 24 24" className="w-6 h-6 fill-current">
              <path fillRule="evenodd" d="M4 5h16a1 1 0 0 1 0 2H4a1 1 0 1 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2z"></path>
            </svg>
          </button>
        </div>
      </div>

      <div className="items-center md:flex">
        <div className="flex flex-col md:flex-row md:mx-6">
          <Link href="about">
            <a className="my-1 text-sm font-medium text-gray-700 transition-colors duration-200 transform dark:text-gray-200 hover:text-blue-500 dark:hover:text-blue-400 md:mx-4 md:my-0">About</a>
          </Link>
          <Link href="competitive_programming">
            <a className="my-1 text-sm font-medium text-gray-700 transition-colors duration-200 transform dark:text-gray-200 hover:text-blue-500 dark:hover:text-blue-400 md:mx-4 md:my-0" >Competitive Programming</a>
          </Link>
        </div>
      </div>
    </div>
  </nav>
}
