const fs = require('fs')

const res = {}
const max_depth = 50
const exts = ['.py', '.cpp', '.in', '.txt']
const root_dir = "./competitive_programming"

let dir = root_dir

const walk = (path, obj = {}) => {
  const all = fs.readdirSync(path)
  const dirs = all.filter(item => item.indexOf('.') === -1)
  const files = all.filter(item => exts.some(ext => item.includes(ext)))

  if (max_depth > 50) {
    throw new Error('max depth exceeded')
  }

  if (files.length) {
    obj.files = files
  }

  if (dirs.length) {
    dirs.forEach(dir => {
      obj[dir] = {}
      const next_path = `${path}/${dir}`
      const stats = fs.lstatSync(next_path)

      if (stats && stats.isDirectory()) {
        walk(next_path, obj[dir])
      }
    })
  }
}

walk(dir, res)

console.log(JSON.stringify(res, null, 4))
