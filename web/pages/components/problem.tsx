import { ReactNode } from "react";

export default function Problem({ input, output, children, dangerous }: { input: string | void, output: string | void, children: ReactNode, dangerous: Boolean }) {
  const buildInOut = () => {
    if (input && output) {
      return <div className="gap-4 mt-4 col-span-4">
        <span>Example Input:</span>
        <br />
        <br />
        <pre className="overflow-scroll">{input}</pre>
        <br />
        <br />
        <span>Example Output:</span>
        <br />
        <br />
        <pre className="overflow-scroll">{output}</pre>
      </div>
    } else if (input) {
      return <div className="gap-4 mt-4 col-span-4">
        <span>Example Input:</span>
        <br />
        <br />
        <pre className="overflow-scroll">{input}</pre>
      </div>

    } else if (output) {

      return <div className="gap-4 mt-4 col-span-4">
        <span>Example Output:</span>
        <br />
        <br />
        <pre className="overflow-scroll">{output}</pre>
      </div>
    }

    return ""

  }
  if (dangerous) return <div className="grid gap-4 grid-cols-12">
    <div className="gap-4 mt-4 col-span-8">
      <div dangerouslySetInnerHTML={{ __html: children as string }}></div>
    </div>
    {buildInOut()}
  </div>

  return <>
    <div>{children}</div>
    {input ? <pre>{input}</pre> : ''}
    {buildInOut()}
  </>
}
