const fs = require('fs')
const args = require('./arg_parser')

const res = {}
const max_depth = 50
const exts = ['.py', '.cpp', '.in', '.txt', '.out']

const walk = (path, obj = {}) => {
  const all = fs.readdirSync(path)
  const dirs = all.filter(item => item.indexOf('.') === -1)
  const files = all.filter(item => exts.some(ext => item.includes(ext)))

  if (max_depth > 50) {
    throw new Error('max depth exceeded')
  }

  if (files.length) {
    files.forEach(file => {
      obj[file] = `${path}/${file}`
    })
  }

  if (dirs.length) {
    dirs.forEach(dir => {
      obj[dir] = {}
      const next_path = `${path}/${dir}`
      const stats = fs.lstatSync(next_path)

      if (stats && stats.isDirectory()) walk(next_path, obj[dir])
    })
  }

  return obj
}

const write = () => {
  if (!args.in) {
    throw new Error('Missing in path')
  }

  if (!args.out) {
    throw new Error('Missing out path')
  }

  const res = walk(args.in)

  fs.writeFileSync(args.out, JSON.stringify(res, null, 4))
}

if (!module.parent) write()

module.exports = {
  walk,
  write
}
