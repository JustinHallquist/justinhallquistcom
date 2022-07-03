import Layout from './layouts/layout'

export default function Home() {
  return (
    <Layout content={
      <h1 className="h-screen text-3xl font-bold underline">
        Hello world!
      </h1>
    } />
  )
}

