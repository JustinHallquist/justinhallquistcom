const fs = require('fs')
const dirToTree = require('./dir_to_tree')
const args = require('./arg_parser')

const lang_exts = ['js', 'cpp', 'py']
const problem_exts = ['html', 'md']
const supplemental_exts = ['txt']
const explanation_exts = ['exp']
const ignore_dirs = ['lib']

if (!args.out) {
  throw new Error('Missing out path')
}

const tree = dirToTree.walk('./competitive_programming')

const flatten = (obj, path = '') => {
  if (!(obj instanceof Object)) return { [path.replace(/\/$/g, '')]: obj };

  return Object.keys(obj).reduce((output, key) => {
    return { ...output, ...flatten(obj[key], path + key + '/') };
  }, {});
}

const grouped_files = Object.entries(flatten(tree)).reduce((memo, [key, val]) => {
  const key_parts = key.split('/')
  const file = key_parts.pop()
  const parent_dir = key_parts.join('/')

  if (!memo[parent_dir]) {
    memo[parent_dir] = []
  }

  memo[parent_dir].push(val)

  return memo;
}, {})

const createProblemSnippet = path => {
  return fs.readFileSync(path)
}

const createSolutionSnippet = (path, ext) => {
  let str = ""
  let comment_char = ""
  if (ext === 'cpp' || ext === 'js') {
    comment_char = "//"
  } else if (ext === 'py') {
    comment_char = "#"
  }

  str += comment_char + " " + ext + "\n"
  str += fs.readFileSync(path)
  str += "\n\n\n"

  return str;
}

const createExplanationSnippet = path => {
  return fs.readFileSync(path)
}

const output = {}

Object.entries(grouped_files).forEach(([path, files]) => {
  const contentParts = {
    problem: '',
    problem_supplement: '',
    solution: '',
    explanation: ''
  }

  if (ignore_dirs.includes(path)) return

  files.forEach(file => {
    const ext = file.split('.').pop()

    if (problem_exts.includes(ext)) {
      contentParts.problem += createProblemSnippet(file)
    } else if (supplemental_exts.includes(ext)) {
      // contentParts.problem_supplement += createProblemSnippet(file)
    } else if (lang_exts.includes(ext)) {
      contentParts.solution += createSolutionSnippet(file, ext)
    } else if (explanation_exts.includes(ext)) {
      contentParts.explanation += createExplanationSnippet(file)
    }
  })

  output[path] = contentParts
})

// TODO: write each file to avoid loading mega json
fs.writeFileSync(`${args.out}`, JSON.stringify(output, null, 4))
