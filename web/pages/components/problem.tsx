import { ReactNode } from "react";

export default function Problem({ children, dangerous }: { children: ReactNode, dangerous: Boolean }) {
  return <div className="grid gap-4 grid-cols-12">
    <div className="gap-4 mt-4 col-span-12">
      {dangerous ? <div dangerouslySetInnerHTML={{ __html: children as string }}></div> : <div>{children}</div>}
    </div>
  </div>
}
