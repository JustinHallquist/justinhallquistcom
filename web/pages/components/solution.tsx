import { ReactNode } from "react";
import { ProblemContent } from '../interfaces/competitive_programming_interfaces'

export default function Solution({ children }: { children: ReactNode }) {
  return <div className="grid grid-cols-2">
    <pre>{children}</pre>
  </div>
}
