export default function TreeNav({ tree, activeNode, activeChild, handleSetActiveNode, handleSetActiveChild }) {
  const nodes = Object.keys(tree)
  const children = Object.keys(tree[activeNode])

  return <>
    <div className="space-y-3 lg:w-1/5 lg:px-2 lg:space-y-4">
      {nodes.map((node, idx) => <>
        <div onClick={() => handleSetActiveNode(node)} key={`${node}.${idx}`} className={`block font-medium hover:underline ${node === activeNode ? 'dark:text-blue-500' : 'dark:text-gray-300'}`} >{node}</div>
        {
          node === activeNode && children.length ?
            children.map((child, idx) => <div key={`${child}.${idx}`} className={`block font-medium hover:underline ${child === activeChild ? 'dark:text-blue-500' : 'dark:text-gray-300'}`} onClick={() => handleSetActiveChild(child)}><span>- </span>{child}</div>) :
            null
        }
      </>)}
    </div >
  </>
}
