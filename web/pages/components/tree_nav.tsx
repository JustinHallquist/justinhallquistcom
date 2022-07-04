export default function TreeNav({ tree, handleSetActivePath }) {
  const dom = []

  const rootNodeEl = (node, active, path, depth) => <div path={path} onClick={() => handleSetActiveNode(node)} key={`${node}.${depth}`} className={`block font-medium hover:underline ${active ? 'dark:text-blue-500' : 'dark:text-gray-300'}`}  >{node}</div>
  const nodeEl = (node, active, path, depth) => {
    const tabs = Array(depth * 2).fill(0).reduce((memo, _) => `${memo}-`, '');
    return <div path={path} onClick={() => handleSetActiveNode(node)} key={`${node}.${depth}`} className={`block font-medium hover:underline ${active ? 'dark:text-blue-500' : 'dark:text-gray-300'}`}  ><span>{tabs} </span>{node}</div>
  }

  const build = (nodes, dom, activeNode = '', path = '', depth = 0) => {
    if (typeof nodes === 'object' && !Array.isArray(nodes)) {
      Object.keys(nodes).map(node => {
        const curPath = path.length ? `${path}.${node}` : node
        const active = activeNode.startsWith(curPath)

        if (node === 'files') return // TODO pass path ignore

        if (nodes[node]) {
          if (depth === 0) {
            dom.push([
              rootNodeEl(node, active, curPath, depth)
              // 
            ])
          } else {
            dom.push([
              nodeEl(node, active, curPath, depth)
            ])
          }

          build(nodes[node], dom, activeNode, curPath, depth + 1)
        } else {
          dom.push([
            nodeEl(node, active, activeNode === path, depth)
          ])
        }
      })
    }
  }

  build(tree, dom, 'usaco.section_1.barn1')

  return <>
    <div className="space-y-3 lg:w-1/5 lg:px-2 lg:space-y-4">
      {dom}
    </div >
  </>
}
