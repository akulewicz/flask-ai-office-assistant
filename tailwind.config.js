
module.exports = {
  content: [
    "./aiassistant/templates/**/*.html",
    "./aiassistant/static/src/**/*.js",
    './node_modules/preline/dist/*.js',
    
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('preline/plugin'),
  
  ],
}

