module.exports = process.argv.slice(2).reduce((memo, item) => {
  const [k, v] = item.split('=')

  memo[k] = v

  return memo
}, {})
