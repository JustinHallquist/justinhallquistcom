import Nav from "../components/nav"
import Footer from "../components/footer"

export declare interface LayoutProps {
  content: React.ReactNode
}

export default function Layout(props: LayoutProps) {
  return (
    <div className="h-screen">
      <Nav />
      <main>
        {props.content}
      </main>
      <Footer />
    </div>
  )
}

