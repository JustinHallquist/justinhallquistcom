import { ReactNode } from "react";
import { Light as SyntaxHighlighter } from 'react-syntax-highlighter';
import { githubGist } from 'react-syntax-highlighter/dist/cjs/styles/hljs'
import cpp from 'react-syntax-highlighter/dist/cjs/languages/hljs/cpp';

export default function Solution({ children }: { children: ReactNode }) {
  SyntaxHighlighter.registerLanguage('cpp', cpp);

  return <div className="grid grid-cols-12">
    <div className="gap-4 mt-4 col-span-8">
      <SyntaxHighlighter language="cpp" showLineNumbers={true} style={githubGist}>
        {children}
      </SyntaxHighlighter>
    </div>
  </div>
}
