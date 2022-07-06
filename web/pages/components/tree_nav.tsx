export default function TreeNav({ tree, activeNode, ignore, handleSetActivePath }) {
  const dom = []

  const rootNodeEl = (node, active, path, depth) => <div path={path} onClick={() => handleSetActivePath(path)} key={`${node}.${depth}`} className={`cursor-pointer block font-medium hover:underline ${active ? 'dark:text-blue-500' : 'dark:text-gray-300'}`}  >{node}</div>
  const nodeEl = (node, active, parentActive, path, depth) => {
    const tabs = Array(depth * 2).fill(0).reduce((memo, _) => `${memo}-`, '');
    return <div path={path} onClick={() => handleSetActivePath(path)} key={`${node}.${depth}`} className={`cursor-pointer block font-medium hover:underline ${active ? 'dark:text-blue-500' : 'dark:text-gray-300'} ${!parentActive ? 'hidden' : ''}`}  ><span>{tabs} </span>{node}</div>
  }

  const build = (nodes, dom, activeNode = '', path = '', depth = 0) => {
    if (typeof nodes === 'object' && !Array.isArray(nodes)) {
      Object.keys(nodes).map(node => {
        const curPath = path.length ? `${path}.${node}` : node
        const active = activeNode.startsWith(curPath)

        const pathParts = curPath.split('.').filter(Boolean)
        const parentActive = pathParts.length && activeNode.startsWith(pathParts.slice(0, pathParts.length - 1).join('.'))

        if (ignore.includes(node)) return

        if (nodes[node]) {
          if (depth === 0) {
            dom.push([
              rootNodeEl(node, active, curPath, depth)
            ])
          } else {
            dom.push([
              nodeEl(node, active, parentActive, curPath, depth)
            ])
          }

          dom.push([
            build(nodes[node], dom, activeNode, curPath, depth + 1)
          ])
        }
      })
    }
  }

  build(tree, dom, activeNode)

  return <div className="mb-5 space-y-3 lg:w-1/5 lg:px-2 lg:space-y-4">
    {dom}
  </div >
}
