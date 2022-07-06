import { ReactNode } from "react";

export default function Problem({ children, dangerous }: { children: ReactNode, dangerous: Boolean }) {
  if (dangerous) return <div dangerouslySetInnerHTML={{ __html: children as string }}></div>

  return <div>{children}</div>
}
