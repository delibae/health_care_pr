const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})


const path = require("path");

module.exports = {
  outputDir: path.resolve(__dirname, "../docker/static"),
}
