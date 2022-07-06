import Link from "next/link"

export default function Footer() {
  return <footer className="bg-white shadow dark:bg-gray-800">
    <div className="container px-6 py-4 mx-auto md:flex md:justify-between md:items-center">
      <Link href="/about">
        <a className="text-xl font-bold text-gray-800 dark:text-white hover:text-gray-700 dark:hover:text-gray-300">JH</a>
      </Link>

      <a href="mailto:justin.hallquist@gmail.com" className="py-2 text-gray-800 dark:text-white sm:py-0">Contact Me</a>
    </div>
  </footer>
}
